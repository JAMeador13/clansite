import requests, zipfile, os, pickle, json, sqlite3


HEADERS = {"X-API-Key":"be18f1d3b5674727b073af7dd46f5a75"}


def get_manifest():
    manifest_url = 'http://www.bungie.net/Platform/Destiny2/Manifest/'
    r = requests.get(manifest_url, headers=HEADERS)
    manifest = r.json()
    mani_url = 'http://www.bungie.net'+manifest['Response']['mobileWorldContentPaths']['en']
    r = requests.get(mani_url)

    with open("MANZIP", "wb") as zip:
        zip.write(r.content)

    with zipfile.ZipFile('MANZIP') as zip:
        name = zip.namelist()
        zip.extractall()

    os.rename(name[0], 'd2Manifest.content')

hashes = [
    "DestinyEnemyRaceDefinition",
    "DestinyPlaceDefinition",
    "DestinyActivityDefinition",
    "DestinyActivityTypeDefinition",
    "DestinyClassDefinition",
    "DestinyGenderDefinition",
    "DestinyInventoryBucketDefinition",
    "DestinyRaceDefinition",
    "DestinyStatDefinition",
    "DestinyTalentGridDefinition",
    "DestinyUnlockDefinition",
    "DestinySandboxPerkDefinition",
    "DestinyStatGroupDefinition",
    "DestinyFactionDefinition",
    "DestinyVendorCategoryDefinition",
    "DestinyRewardSourceDefinition",
    "DestinyItemCategoryDefinition",
    "DestinyDamageTypeDefinition",
    "DestinyActivityModeDefinition",
    "DestinyMedalTierDefinition",
    "DestinyActivityGraphDefinition",
    "DestinyItemTierTypeDefinition",
    "DestinyBondDefinition",
    "DestinyDestinationDefinition",
    "DestinyInventoryItemDefinition",
    "DestinyLocationDefinition",
    "DestinyLoreDefinition",
    "DestinyObjectiveDefinition",
    "DestinyProgressionDefinition",
    "DestinyProgressionLevelRequirementDefinition",
    "DestinySackRewardItemListDefinition",
    "DestinySocketCategoryDefinition",
    "DestinySocketTypeDefinition",
    "DestinyVendorDefinition",
    "DestinyMilestoneDefinition",
    "DestinyActivityModifierDefinition",
    "DestinyHistoricalStatsDefinition"
]

def build_dict(hash_list):
    con = sqlite3.connect('d2Manifest.content')
    cur = con.cursor()
    all_data = {}

    for table_name in hash_list:
        cur.execute('SELECT json from '+table_name)
        items = cur.fetchall()
        item_jsons = [json.loads(item[0]) for item in items]

        item_dict = {}

        for item in item_jsons:
            if table_name == 'DestinyHistoricalStatsDefinition':
                item_dict[item["statId"]] = item
            else:
                item_dict[item["hash"]] = item

        all_data[table_name] = item_dict

    return all_data

def mani_update():
    get_manifest()
    all_data = build_dict(hashes)
    with open('d2manifest.pickle', 'wb') as data:
        pickle.dump(all_data, data)