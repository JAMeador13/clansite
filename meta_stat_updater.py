import stats.models as mods


all_fields = [
'allMedalsScore', 'allMedalsEarned', 'score', 'activityDurationSeconds',
'secondsPlayed', 'orbsGathered', 'orbsDropped', 'assists', 'assistsAgainstPlayerHunter',
'assistsAgainstPlayerTitan', 'assistsAgainstPlayerWarlock', 'kills', 'offensiveKills',
'precisionKills', 'precisionKillOfPlayerHunter', 'precisionKillOfPlayerTitan', 'precisionKillOfPlayerWarlock',
'killsOfPlayerHunter', 'killsOfPlayerTitan', 'killsOfPlayerWarlock', 'totalKillDistance',
'deaths', 'suicides', 'deathsFromPlayerTitan', 'deathsFromPlayerHunter', 'deathsFromPlayerWarlock',
'resurrectionsPerformed', 'resurrectionsReceived', 'sparksCaptured', 'slamDunks',
'dunkKills', 'carrierKills', 'styleDunks', 'objectivesCompleted', 'zonesCaptured',
'tagCaptures', 'capturedYourOwnKill', 'recoveredTeammateTags', 'lostTagToOpponent',
'recoveredOwnDeadTag', 'defensiveKills', 'zonesNeutralized', 'relicsCaptured', 'gatesHit',
'averageKillDistance', 'averageScorePerKill', 'averageScorePerLife', 'averageLifespan',
'combatRating', 'longestKillSpree', 'longestSingleLife', 'killsDeathsRatio', 'killsDeathsAssists',
'tagsCapturedPerTagLost', 'raceCompletionMilliseconds', 'weaponPrecisionKillsMachinegun',
'weaponPrecisionKillsScoutRifle', 'weaponPrecisionKillsSideArm', 'weaponKillsGrenade',
'weaponKillsMachinegun', 'weaponKillsScoutRifle', 'weaponKillsSuper', 'weaponKillsSideArm',
'weaponKillsPrecisionKillsMachinegun', 'weaponKillsPrecisionKillsScoutRifle', 'weaponKillsPrecisionKillsSideArm',
'weaponPrecisionKillsHandCannon', 'weaponKillsHandCannon', 'weaponKillsMelee', 'weaponKillsPrecisionKillsHandCannon',
'weaponPrecisionKillsSniper', 'weaponKillsRocketLauncher', 'weaponKillsSniper', 'weaponKillsPrecisionKillsSniper',
'weaponPrecisionKillsAutoRifle', 'weaponKillsAutoRifle', 'weaponKillsPrecisionKillsAutoRifle',
'weaponKillsFusionRifle', 'weaponKillsShotgun', 'weaponPrecisionKillsPulseRifle',
'weaponKillsPulseRifle', 'weaponKillsPrecisionKillsPulseRifle', 'weaponKillsSword',
'weaponPrecisionKillsFusionRifle', 'weaponKillsPrecisionKillsFusionRifle', 'weaponPrecisionKillsShotgun',
'weaponKillsPrecisionKillsShotgun', 'weaponPrecisionKillsRocketLauncher', 'weaponKillsPrecisionKillsRocketLauncher',
'weaponKillsRelic', 'medalsActivityCompleteHighestScoreWinning', 'medalsActivityCompleteVictory',
'medalsCloseCallTalent', 'medalsGrenadeKillStick', 'medalsKillSpree1', 'medalsSingularityFlagCaptureMulti',
'medalsPaybackKill', 'medalsAvenger', 'medalsFirstPlaceKillSpree', 'medalsFirstBlood',
'medalsKillAssistSpree', 'medalsKillMulti2', 'medalsKillPostmortem', 'medalsActivityCompleteCycle',
'medalsKillHeadshot', 'medalsKilljoy', 'medalsComebackKill', 'medalsSingularityRunnerDefenseMulti',
'medalsAbilityHavocKillMulti', 'medalsKillMulti3', 'medalsWinningScore', 'medalsKillSpree2',
'medalsActivityCompleteVictoryMercy', 'medalsActivityCompleteSingularityPerfectRunner',
'medalsWeaponScoutRifleKillSpree', 'medalsSingularityFlagHolderKilledClose', 'medalsActivityCompleteVictoryBlowout',
'medalsKillSpreeNoDamage', 'medalsMeleeKillHunterThrowingKnifeHeadshot', 'medalsAbilityShadowStrikeKillMulti',
'medalsHunterKillInvisible', 'medalsWeaponSidearmKillSpree', 'medalsSingularityFlagHolderKilledMulti',
'medalsWeaponSniperRifleHeadshotSpree', 'medalsAbilityVoidBowKillMulti', 'medalsWeaponPulseRifleKillSpree',
'medalsWeaponFusionRifleKillSpree', 'medalsWeaponHandCannonHeadshotSpree', 'medalsRescue',
'medalsAbilityArcLightningKillMulti', 'medalsTeamKillSpree', 'medalsAbilityNovaBombKillMulti',
'medalsAbilityGhostGunKillMulti', 'medalsActivityCompleteLonewolf', 'medalsKillMulti4',
'medalsAbilityWardDeflect', 'medalsAbilityThermalHammerKillMulti', 'medalsActivityCompleteHighestScoreLosing',
'medalsWeaponShotgunKillSpree', 'medalsWeaponMachineGunKillSpree', 'medalsBuddyResurrectionMulti',
'medalsActivityCompleteVictoryElimination', 'medalsEliminationLastStandRevive', 'medalsEliminationLastStandKill',
'medalsEliminationWipeSolo', 'medalsEliminationWipeQuick', 'medalsActivityCompleteVictoryEliminationShutout',
'medalsActivityCompleteVictoryExtraLastSecond', 'medalsKillMulti5', 'medalsKillMulti6',
'medalsSupremacyMostSelfConfirms', 'medalsSupremacyMostConfirms', 'medalsSupremacyMostDenies',
'medalsSupremacy', 'medalsSupremacyConfirmStreakLarge', 'medalsSupremacySelfDeny',
'medalsSupremacyMulti', 'medalsHazardKill', 'medalsActivityCompleteVictoryRumbleBlowout',
'medalsActivityCompleteControlMostCaptures', 'medalsZoneCapturedBInitial', 'medalsActivityCompleteVictoryRumble',
'medalsActivityCompleteVictoryLastSecond', 'medalsRadianceShutdown', 'medalsWeaponAutoRifleKillSpree',
'medalsDominationKill', 'medalsTeamDominationHold1m', 'medalsVehicleInterceptorKillSplatter',
'medalsVehicleInterceptorKillSpree', 'medalsDominionZoneCapturedSpree', 'medalsKillSpree3',
'medalsKilljoyMega', 'medalsActivityCompleteVictoryRumbleLastSecond', 'medalsSupremacyNeverCollected',
'medalsActivityCompleteSalvageMostCancels', 'medalsSalvageProbeCanceled', 'medalsSalvageProbeCompleteSpree',
'medalsSalvageProbeDefenseKill', 'medalsSalvageZoneCapturedSpree', 'medalsActivityCompleteSalvageShutout',
'medalsDominionZoneOffenseKillSpree', 'medalsActivityCompleteDeathless', 'medalsKillAssistSpreeFfa',
'medalsDominionZoneDefenseKillSpree', 'medalsVehiclePikeKillSpree', 'medalsSupremacyDenyMulti',
'medalsWeaponRocketLauncherKillSpree', 'medalsAbilityRadianceGrenadeKillMulti', 'medalsBuddyResurrectionSpree',
'medalsActivityCompleteVictoryEliminationPerfect', 'medalsVehicleSparrowKillSplatter',
'medalsWeaponSwordKillSpree', 'medalsActivityCompleteVictorySuddenDeath', 'medalsSalvageProbeOffenseKillMulti',
'medalsActivityCompleteVictoryRumbleSuddenDeath', 'medalsVehiclePikeKillSplatter',
'medalsKillSpreeAbsurd', 'medalsVehicleFotcTurretKillSpree', 'medalsKillMulti7'
]


mode_fields = [
'offensiveKills','resurrectionsPerformed', 'resurrectionsReceived', 'sparksCaptured', 'slamDunks',
'dunkKills', 'carrierKills', 'styleDunks', 'objectivesCompleted', 'zonesCaptured',
'tagCaptures', 'capturedYourOwnKill', 'recoveredTeammateTags', 'lostTagToOpponent',
'recoveredOwnDeadTag', 'defensiveKills', 'zonesNeutralized', 'relicsCaptured', 'gatesHit',
'tagsCapturedPerTagLost', 'raceCompletionMilliseconds', 'medalsSingularityFlagCaptureMulti',
'medalsSingularityRunnerDefenseMulti', 'medalsActivityCompleteSingularityPerfectRunner',
'medalsSingularityFlagHolderKilledClose', 'medalsSingularityFlagHolderKilledMulti','medalsBuddyResurrectionMulti',
'medalsActivityCompleteVictoryElimination', 'medalsEliminationLastStandRevive', 'medalsEliminationLastStandKill',
'medalsEliminationWipeSolo', 'medalsEliminationWipeQuick', 'medalsActivityCompleteVictoryEliminationShutout',
'medalsSupremacyMostSelfConfirms', 'medalsSupremacyMostConfirms', 'medalsSupremacyMostDenies',
'medalsSupremacy', 'medalsSupremacyConfirmStreakLarge', 'medalsSupremacySelfDeny',
'medalsSupremacyMulti', 'medalsActivityCompleteVictoryRumbleBlowout',
'medalsActivityCompleteControlMostCaptures', 'medalsZoneCapturedBInitial', 'medalsActivityCompleteVictoryRumble',
'medalsDominationKill', 'medalsTeamDominationHold1m', 'medalsVehicleInterceptorKillSplatter',
'medalsVehicleInterceptorKillSpree', 'medalsDominionZoneCapturedSpree', 'medalsActivityCompleteVictoryRumbleLastSecond', 'medalsSupremacyNeverCollected',
'medalsActivityCompleteSalvageMostCancels', 'medalsSalvageProbeCanceled', 'medalsSalvageProbeCompleteSpree',
'medalsSalvageProbeDefenseKill', 'medalsSalvageZoneCapturedSpree', 'medalsActivityCompleteSalvageShutout',
'medalsDominionZoneOffenseKillSpree', 'medalsKillAssistSpreeFfa', 'medalsDominionZoneDefenseKillSpree',
'medalsVehiclePikeKillSpree', 'medalsSupremacyDenyMulti', 'medalsBuddyResurrectionSpree',
'medalsActivityCompleteVictoryEliminationPerfect', 'medalsVehicleSparrowKillSplatter',
'medalsSalvageProbeOffenseKillMulti', 'medalsActivityCompleteVictoryRumbleSuddenDeath',
'medalsVehiclePikeKillSplatter', 'medalsVehicleFotcTurretKillSpree'
]


def meta_stat_updater():
    if mods.Cursor.objects.filter(operating_model="Meta Stats"):
        cursor = mods.Cursor.objects.get(operating_model="Meta Stats")
    else:
        cursor = mods.Cursor(operating_model="Meta Stats")

    cur = cursor.pgcr_cursor
    activity_count = mods.Activity.objects.count()

    for x in range(cur, activity_count+1):
        activity = mods.Activity.objects.get(pk=x)

        for character in activity.characters.all():
            participant = activity.Participants.filter(displayName=character.member.gamertag)[0]

            for field in all_fields:
                if field not in mode_fields:
                    exec('character.'+field+'={game_count:0; total:0; max:0; min:0; avg:0} if character.'+field+'==[]')
                    exec('character.'+field+'[game_count]+=1')
                    exec('character.'+field+'[total]+=participant.'+field)
                    exec('character.'+field+'[max]=participant.'+field+' if participant.'+field+'>character.'+field+'[max]')
                    exec('character.'+field+'[min]=participant.'+field+' if participant.'+field+'<character.'+field+'[min]')
                    exec('character.'+field+'[avg]=((character.'+field+'[avg]*(character.'+field+'[game_count]-1))+participant.'+field+')/character.'+field+'[game_count]')

                else:





