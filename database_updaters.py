import clan.models as mods
import confidential

HEADERS = {"X-API-Key":confidential.bungie_api_key}

base_path = 'http://www.bungie.net/Platform/'
pgcr_uri = 'Destiny2/Stats/PostGameCarnageReport/'


def clan_updater():
    from django.core.exceptions import ObjectDoesNotExist
    from django.db.utils import OperationalError
    import pickle, requests

    def get_clan_id(clan):
        print("\nRetrieving data for clan", str(clan), end="\n\n")
        r1 = requests.get(base_path+"GroupV2/Name/"+str(clan)+"/1", headers=HEADERS)
        group_id = r1.json()["Response"]["detail"]["groupId"]
        return group_id


    def get_clan_members(cln):
        print("Retrieving members for clan", str(cln))

        # Might need to set this to do multiple pages at some point, but at the time it's not relevant
        payload = {"currentpage": 1}
        r2 = requests.get(base_path+"GroupV2/"+cln.clan_id+"/Members/", params=payload, headers=HEADERS)
        members = r2.json()

        for mem in members["Response"]["results"]:
            print("Building database entry for", mem["destinyUserInfo"]["displayName"])

            if not mods.Player.objects.filter(membership_id=mem["destinyUserInfo"]["membershipId"], membership_type=mem["destinyUserInfo"]["membershipType"]).exists():
                player = mods.Player(
                    membership_id=mem["destinyUserInfo"]["membershipId"],
                    membership_type=mem["destinyUserInfo"]["membershipType"],
                    display_name=mem["destinyUserInfo"]["displayName"],
                    )
                player.save()

        for mem in members["Response"]["results"]:
            player = mods.Player.objects.get(membership_id=mem["destinyUserInfo"]["membershipId"])

            if not mods.ClanMember.objects.filter(clan=cln, player=player).exists():
                clan_member = mods.ClanMember(clan=cln, player=player)
                clan_member.save()

        print("\nAll members retrieved for clan", str(cln))


    def get_characters(member, manifest):
        print("\nRetrieving characters for", str(member))

        get_user_data_uri = 'Destiny2/'+str(member.membership_type)+'/Profile/'+str(member.membership_id)+'/'
        payload = {'components': '200'}
        r1 = requests.get(base_path+get_user_data_uri, params=payload, headers=HEADERS)
        user_data = r1.json()
        find_main = {}

        print("Building entry for", str(member)+"'s characters")

        for char_id, char_info in user_data["Response"]["characters"]["data"].items():
            find_main[char_id] = char_info["minutesPlayedTotal"]

            if not member.Characters.filter(char_id=char_id).exists():
                ch_race = manifest["DestinyRaceDefinition"][char_info["raceHash"]]["displayProperties"]["name"]
                ch_gender = manifest["DestinyGenderDefinition"][char_info["genderHash"]]["displayProperties"]["name"]
                ch_class = manifest["DestinyClassDefinition"][char_info["classHash"]]["displayProperties"]["name"]
                ch_type = ch_race+" "+ch_gender+" "+ch_class

                member.Characters.create(
                    char_id=char_id,
                    char_race=ch_race,
                    char_gender=ch_gender,
                    char_class=ch_class,
                    char_type=ch_type,
                    minutes_played=char_info["minutesPlayedTotal"],
                    is_main=False,
                    emblem=char_info["emblemPath"],
                    emblem_background=char_info["emblemBackgroundPath"]
                    )
            else:
                charr = member.Characters.get(char_id=char_id)
                charr.minutes_played = char_info["minutesPlayedTotal"]
                charr.emblem = char_info["emblemPath"]
                charr.emblem_background = char_info["emblemBackgroundPath"]
                charr.save()

        for k, v in find_main.items():
            if v == max(find_main.values()):
                main = member.Characters.get(char_id=k)
                main.is_main = True
                main.save()

        print(str(member)+"'s characters saved.\n")


    def update_db():
        try:
            cName = "Omega"
            clan = mods.Clan.objects.get(name=cName)
        except OperationalError:
            clan = mods.Clan(name=cName)
            clan.save()
        except ObjectDoesNotExist:
            clan = mods.Clan(name=cName)
            clan.save()

        clan.clan_id = get_clan_id(clan)
        get_clan_members(clan)

        with open("/home/jamtime/clansite/d2manifest.pickle", "rb") as mani:
            manifest = pickle.load(mani)

        for mem in clan.ClanMembers.all():
            plyr = mem.player
            get_characters(plyr, manifest)

    update_db()
    message = 'Clan, players, clan member relationships, and player characters created; processes complete.'
    return message



def activity_updater():
    from django.core.exceptions import ObjectDoesNotExist
    from time import sleep
    import requests
    from datetime import datetime as dt
    from dateutil.parser import parse

    def get_member_activities(member, total_activity_count):
        print("Retrieving activity history for "+member.display_name+"...")
        modeIdentities = [5]

        for char in member.Characters.all():
            print("Starting activity retrieval for", char.char_type+"...")

            for gameMode in modeIdentities:
                payload = {"count":"100", "mode": gameMode, "page":0}

                try:
                    lastEntry = char.Activities.latest()
                    time_stamp = lastEntry.period.timestamp()

                except ObjectDoesNotExist:
                    time_stamp = 0

                while True:
                    page_activity_count = 0
                    activity_history_uri = 'Destiny2/'+str(member.membership_type)+'/Account/'+str(member.membership_id)+'/Character/'+char.char_id+'/Stats/Activities/'

                    try:
                        print("Current page: "+str(payload["page"]))

                        while True:
                            try:
                                r2 = requests.get(base_path+activity_history_uri, params=payload, headers=HEADERS)
                                history = r2.json()
                                payload["page"]+=1
                                errEnum = int(history["ErrorCode"])
                                throttle = float(history["ThrottleSeconds"])
                                sleep(throttle)
                                endActs = False

                            except Exception as err:
                                print("Encountered error. "+str(err))
                                continue

                            else:
                                break

                        if errEnum != 1:
                            print(history["ErrorStatus"])
                            print(history["Message"])
                            print("Number of pages: " + str(payload["page"]))
                            break

                        for act in history["Response"]["activities"]:
                            inst_id = act["activityDetails"]["instanceId"]
                            t = parse(act["period"]).timestamp()

                            if t > time_stamp:
                                if mods.Activity.objects.filter(instanceId=inst_id).exists():
                                    print('Model already exists for '+str(inst_id)+', adding relation to current character.')
                                    activity = mods.Activity.objects.get(instanceId=inst_id)
                                    activity.characters.add(char)
                                    activity.save()

                                else:
                                    print('Creating new model instance...')
                                    activity = char.Activities.create(
                                        instanceId=inst_id,
                                        period=dt.utcfromtimestamp(t),
                                        referenceId=act["activityDetails"]["referenceId"],
                                        mode=act["activityDetails"]["mode"]
                                        )

                                page_activity_count+=1
                                total_activity_count+=1

                            else:
                                print("End of new activities.")
                                endActs = True
                                break

                        else:
                            print(str(page_activity_count), "activities added. Continuing to page", str(payload['page']))

                    except KeyError:
                        print("End of new activities for", member.display_name+"'s", char.char_type+".")
                        break

                else:
                    if endActs:
                        break

        else:
            print("All activities retrieved for", member.display_name+". Total retrieved =", str(total_activity_count))
            return total_activity_count

    def updateDB():
        clan = mods.Clan.objects.get(name="Omega")
        total_activity_number = mods.Activity.objects.count()

        for i in range(1, clan.ClanMembers.count()+1):
            member = clan.ClanMembers.get(pk=i)
            player = member.player
            total_activity_number = get_member_activities(player, total_activity_number)
            print('Running total: '+str(total_activity_number))

        print("All activity instance IDs updated!")
        print("Number of newly collected IDs:", str(total_activity_number))
        print("Total ID count:", str(mods.Activity.objects.count()))

    updateDB()
    message = 'Activity Instance IDs collected. All processes complete.'
    return message



def pgcr_updater():
    from time import sleep
    import requests

    def get_pgcr(activity):
        inst_id = activity.instanceId
        pgcr_uri = 'Destiny2/Stats/PostGameCarnageReport/'

        while True:
            try:
                r4 = requests.get(base_path+pgcr_uri+inst_id, headers=HEADERS)
                pgcr = r4.json()
                response = pgcr["Response"]

            except Exception as err:
                print("Encountered an error in return from Bungie. "+str(err))
                sleep(3)
                continue

            else:
                break

        throttle = float(pgcr["ThrottleSeconds"])
        errCode = pgcr["ErrorCode"]
        errStatus = pgcr["ErrorStatus"]

        print("Throttle: "+str(throttle))
        print("Status: "+str(errCode)+" - "+str(errStatus))
        sleep(throttle)

        activity.pgcr = response
        activity.save()


    def update_db():
        if mods.Cursor.objects.filter(operating_model='Activity').exists():
            cursor = mods.Cursor.objects.get(operating_model='Activity')
        else:
            cursor = mods.Cursor(operating_model='Activity')

        cur = cursor.pgcr_cursor
        collected = cur-1

        for i in range(cur, mods.Activity.objects.count()+1):
            activity = mods.Activity.objects.get(pk=i)
            cur+=1
            collected+=1
            get_pgcr(activity)

            cursor.pgcr_cursor = cur
            cursor.save()
            print("PGCR retrieved; count: "+str(collected))

    update_db()
    message = 'PGCRs updated. Processes complete.'
    return message



def team_updater():
    from dateutil.parser import parse
    import datetime

    def update_db():
        if mods.Cursor.objects.filter(operating_model='Team').exists():
            cursor = mods.Cursor.objects.get(operating_model='Team')
        else:
            cursor = mods.Cursor(operating_model='Team')

        cur = cursor.pgcr_cursor
        tcur = cursor.team_cursor
        team_count = tcur-1

        for i in range(cur, mods.Activity.objects.count()+1):
            activity = mods.Activity.objects.get(pk=i)
            js = activity.pgcr

            period = js["period"]
            period = parse(period).timestamp()
            period = datetime.datetime.utcfromtimestamp(period)
            refID = str(js["activityDetails"]["referenceId"])
            mode = js["activityDetails"]["mode"]
            teams = js["teams"]

            activity.period = period
            activity.referenceId = refID
            activity.mode = mode
            activity.save()

            for team in teams:
                team_count += 1

                if team["standing"]["basic"]["value"] == 0.0:
                    win = True
                else:
                    win = False

                if not activity.Teams.filter(teamName=team["teamName"]).exists():
                    activity.Teams.create(
                        teamName=team["teamName"],
                        teamId=float(team["teamId"]),
                        score=float(team["score"]["basic"]["value"]),
                        is_winner=win
                        )
                    print("Team object created.")

                print("\nCurrent team count: "+str(team_count))

                tcur += 1
                cursor.team_cursor = tcur

            print("\nActivity count: "+str(cur))

            cur += 1
            cursor.pgcr_cursor = cur
            cursor.save()

        else:
            print("All activities parsed. Total team count: "+str(team_count))

    update_db()
    message = 'Teams updated. Processes complete.'
    return message



def participant_updater():
    from django.core.exceptions import ObjectDoesNotExist
    import pickle, json

    def generate_player(p_dict):
        fields = {
            "standing": p_dict["standing"],
            "score": p_dict["score"]["basic"]["value"],
            "characterId": p_dict["characterId"]
            }

        for k, v in p_dict["player"]["destinyUserInfo"].items():
            fields[k] = v

        for k, v in p_dict["values"].items():
            fields[k] = v["basic"]["value"]

        for k, v in p_dict["extended"]["values"].items():
            fields[k] = v["basic"]["value"]

        return fields


    def update_db():
        if mods.Cursor.objects.filter(operating_model='Participant').exists():
            cursor = mods.Cursor.objects.get(operating_model='Participant')
        else:
            cursor = mods.Cursor(operating_model='Participant')

        tcursor = mods.Cursor.objects.get(operating_model='Team')
        tcur = tcursor.team_cursor

        acur = cursor.pgcr_cursor
        pcur = cursor.participant_cursor
        activity_count = mods.Activity.objects.count()

        with open("/home/jamtime/clansite/d2manifest.pickle", "rb") as mani:
            manifest = pickle.load(mani)

        for i in range(acur, activity_count+1):
            activity = mods.Activity.objects.get(pk=i)
            print(str(activity)+"...")

            try:
                p_entries = activity.pgcr["entries"]

                for p in p_entries:
                    p_fields = generate_player(p)

                    if not activity.private: # can insert mode separation here
                        try:
                            team = activity.Teams.get(teamId=p_fields["team"])

                        except ObjectDoesNotExist:
                            if int(p_fields["team"]) == -1:
                                print("Creating deserter team...")
                                team = activity.Teams.create(
                                    teamName="Deserters",
                                    teamId=p_fields["team"],
                                    score=p_fields["score"],
                                    )
                        """
                    elif not activity.private:
                        if int(p_fields["standing"]) == 0:
                            win = True
                        else:
                            win = False

                        print("Creating rumble pseudo team...")
                        team = activity.Teams.create(
                            teamName="FFA",
                            teamId=-2.0,
                            score=p_fields["score"],
                            victor=win
                            )

                        tcur += 1
                        tcursor.team_cursor = tcur
                        tcursor.save()
                        """"""
                    else:
                        try:
                            team = activity.Teams.get(teamId=p_fields["team"])

                        except ObjectDoesNotExist:
                            try:
                                team = activity.Teams.get(teamId=p_fields["team"])

                            except ObjectDoesNotExist:
                                if int(p_fields["team"]) == -1:
                                    print("Creating deserter team...")
                                    team = activity.Teams.create(
                                        teamName="Deserters",
                                        teamId=p_fields["team"],
                                        score=p_fields["score"],
                                        )

                        except KeyError:
                            if int(p_fields["standing"]) == 0:
                                win = True
                            else:
                                win = False

                            print("Creating rumble pseudo team...")
                            team = activity.Teams.create(
                                teamName="FFA",
                                teamId=-2.0,
                                score=p_fields["score"],
                                victor=win
                                )

                            tcur += 1
                            tcursor.team_cursor = tcur
                            tcursor.save()
                        """
                    try:
                        if not team.Participants.filter(displayName=p_fields["displayName"]).exists():
                            if mods.Player.objects.filter(membership_id=p_fields["membershipId"]).exists():
                                p_obj = mods.Player.objects.get(membership_id=p_fields["membershipId"])
                            else:
                                p_obj = mods.Player(
                                    membership_id=p_fields["membershipId"],
                                    membership_type=p_fields["membershipType"],
                                    display_name=p_fields["displayName"]
                                    )

                            if p_obj.Characters.filter(char_id=p_fields["characterId"]).exists():
                                char_obj = p_obj.Characters.get(char_id=p_fields["characterId"])
                            else:
                                ch_race = manifest["DestinyRaceDefinition"][p_fields["player"]["raceHash"]]["displayProperties"]["name"]
                                ch_gender = manifest["DestinyGenderDefinition"][p_fields["player"]["genderHash"]]["displayProperties"]["name"]
                                ch_class = manifest["DestinyClassDefinition"][p_fields["player"]["classHash"]]["displayProperties"]["name"]
                                ch_type = ch_race+" "+ch_gender+" "+ch_class

                                char_obj = p_obj.Characters.create(
                                    char_id=p_fields["characterId"],
                                    char_race=ch_race,
                                    char_gender=ch_gender,
                                    char_class=ch_class,
                                    char_type=ch_type
                                    )

                            new_p = team.Participants.create(
                                displayName=p_fields["displayName"],
                                character=char_obj
                                )

                            for k, v in p_fields.items():
                                if isinstance(v, str):
                                    f = 'new_p.'+k+'="'+str(v)+'"'
                                else:
                                    f = 'new_p.'+k+'='+str(v)
                                exec(f)

                            new_p.save()

                    except KeyError:
                        continue

                    print("\nParticipant count: "+str(pcur))
                    pcur+=1
                    cursor.participant_cursor = pcur
                    cursor.save()

            except KeyError as err:
                print(str(activity), str(err))
                print(json.dumps(activity.pgcr, indent=4))
                break

            print("\nActivity count: "+str(acur))
            print(str("Percentage of activities parsed: %.4f" % ((acur / activity_count) * 100))+"%\n")
            activity.pgcr = []
            activity.save()
            acur += 1
            cursor.pgcr_cursor = acur
            cursor.save()

        else:
            print("All PGCRs parsed. Total player count: "+str(pcur-1))

    update_db()
    message = 'Participants updated. Processes complete.'
    return message



def weapon_updater():
    import json
    import re
    import time

    def updateDB():
        if mods.Cursor.objects.filter(operating_model='Weapon').exists():
            cursor = mods.Cursor.objects.get(operating_model='Weapon')
        else:
            cursor = mods.Cursor(operating_model='Weapon')

        p_cursor = mods.Cursor.objects.get(operating_model='Participant')

        pcur = cursor.participant_cursor
        wcur = cursor.weapon_cursor
        participant_count = p_cursor.participant_cursor
        start_time = time.time()
        now = start_time
        t_count = 0
        avg = 0

        for i in range(pcur, participant_count):
            print("\nParticipant #", pcur, "\n")

            if mods.Participant.objects.filter(pk=i).exists():
                p = mods.Participant.objects.get(pk=(i))

                try:
                    p_weapons = json.loads(re.sub(r"'", '"', p.weapons))

                    if len(p_weapons) != 0:
                        for w in p_weapons:
                            print("Weapon count:", wcur)
                            p.Weapons.create(
                                referenceId=str(w["referenceId"]),
                                kills=w["values"]["uniqueWeaponKills"]["basic"]["value"],
                                precisionKills=w["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
                                )
                            wcur += 1
                            cursor.weapon_cursor = wcur
                            cursor.save()
                    else:
                        print(p.__str__(), p.weapons)

                    remaining_participants = participant_count - pcur
                    time_of_last = now
                    now = time.time()
                    duration_of_one = now - time_of_last
                    t_count += 1
                    avg = ((t_count * avg) + duration_of_one) / (t_count + 1)

                    def to_hms(seconds):
                        m, s = divmod(seconds, 60)
                        h, m = divmod(m, 60)
                        return ("%d:%02d:%.4f" % (h, m, s))

                    last_p_time = to_hms(duration_of_one)
                    average_time = to_hms(avg)
                    total_req_time = to_hms(avg * participant_count)
                    remaining_time = to_hms(avg * remaining_participants)

                    print("Duration of last participant:", last_p_time)
                    print("Average time per participant:", average_time)
                    print("Sample size for average:", t_count+1, "\n")

                    print("Estimated total required time:", total_req_time)
                    print("Estimated time remaining:", remaining_time, "\n")

                    print(str("Percentage of participants parsed: %.4f" % ((pcur / participant_count) * 100))+"%\n")
                    p.weapons = []
                    p.save()
                    pcur += 1
                    cursor.participant_cursor = pcur
                    cursor.save()

                except TypeError:
                    print("No weapons for participant.")
                    pcur += 1
                    cursor.participant_cursor = pcur
                    cursor.save()

            else:
                pcur += 1
                cursor.participant_cursor = pcur
                cursor.save()


        else:
            a="All weapons collected.\n"
            b="\nTotal team count:         "+str(mods.Cursor.objects.get(operating_model='Team').team_cursor)
            c="\nTotal participant count:  "+str(pcur)
            d="\nTotal weapon count:       "+str(wcur)
            message = a+b+c+d
            return message

    message = updateDB()
    return message

