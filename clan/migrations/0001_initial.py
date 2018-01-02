# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-21 21:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instanceId', models.CharField(db_index=True, max_length=30, unique=True)),
                ('period', models.DateTimeField(verbose_name='time period of activity')),
                ('private', models.BooleanField(default=False)),
                ('referenceId', models.CharField(max_length=30)),
                ('mode', models.CharField(max_length=30)),
                ('pgcr', jsonfield.fields.JSONField(default=list)),
            ],
            options={
                'ordering': ['instanceId'],
                'get_latest_by': 'period',
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_id', models.CharField(max_length=30)),
                ('char_race', models.CharField(max_length=30)),
                ('char_gender', models.CharField(max_length=30)),
                ('char_class', models.CharField(max_length=30)),
                ('char_type', models.CharField(max_length=120)),
                ('minutes_played', models.FloatField(default=0.0)),
                ('is_main', models.BooleanField(default=False)),
                ('emblem', models.CharField(default='', max_length=255)),
                ('emblem_background', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Clan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('clan_id', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Cursor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operating_model', models.CharField(default='', max_length=30)),
                ('pgcr_cursor', models.IntegerField(default=1)),
                ('team_cursor', models.IntegerField(default=1)),
                ('participant_cursor', models.IntegerField(default=1)),
                ('weapon_cursor', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activitiesCleared', models.FloatField(default=0.0)),
                ('activitiesEntered', models.FloatField(default=0.0)),
                ('activitiesWon', models.FloatField(default=0.0)),
                ('assists', models.FloatField(default=0.0)),
                ('averageDeathDistance', models.FloatField(default=0.0)),
                ('averageKillDistance', models.FloatField(default=0.0)),
                ('averageLifespan', models.FloatField(default=0.0)),
                ('averageScorePerKill', models.FloatField(default=0.0)),
                ('averageScorePerLife', models.FloatField(default=0.0)),
                ('bestSingleGameKills', models.FloatField(default=0.0)),
                ('bestSingleGameScore', models.FloatField(default=0.0)),
                ('completed', models.BooleanField(default=None)),
                ('fastestCompletionMsForActivity', models.FloatField(default=0.0)),
                ('activityCompletions', models.FloatField(default=0.0)),
                ('activityDeaths', models.FloatField(default=0.0)),
                ('activityKills', models.FloatField(default=0.0)),
                ('activitySecondsPlayed', models.FloatField(default=0.0)),
                ('activityWins', models.FloatField(default=0.0)),
                ('activityGoalsMissed', models.FloatField(default=0.0)),
                ('activityCompletedFailures', models.FloatField(default=0.0)),
                ('activitySpecialActions', models.FloatField(default=0.0)),
                ('activityBestGoalsHit', models.FloatField(default=0.0)),
                ('activityGoalsHit', models.FloatField(default=0.0)),
                ('activitySpecialScore', models.FloatField(default=0.0)),
                ('activityFastestObjectiveCompletionMs', models.FloatField(default=0.0)),
                ('activityBestSingleGameScore', models.FloatField(default=0.0)),
                ('activityKillsDeathsRatio', models.FloatField(default=0.0)),
                ('activityKillsDeathsAssists', models.FloatField(default=0.0)),
                ('deaths', models.FloatField(default=0.0)),
                ('kills', models.FloatField(default=0.0)),
                ('killsDeathsRatio', models.FloatField(default=0.0)),
                ('killsDeathsAssists', models.FloatField(default=0.0)),
                ('lbSingleGameKills', models.FloatField(default=0.0)),
                ('lbPrecisionKills', models.FloatField(default=0.0)),
                ('lbAssists', models.FloatField(default=0.0)),
                ('lbDeaths', models.FloatField(default=0.0)),
                ('lbKills', models.FloatField(default=0.0)),
                ('lbObjectivesCompleted', models.FloatField(default=0.0)),
                ('lbSingleGameScore', models.FloatField(default=0.0)),
                ('maximumPowerLevel', models.FloatField(default=0.0)),
                ('medalAbilityDawnbladeAerial', models.FloatField(default=0.0)),
                ('medalAbilityDawnbladeSlam', models.FloatField(default=0.0)),
                ('medalAbilityFlowwalkerMulti', models.FloatField(default=0.0)),
                ('medalAbilityFlowwalkerQuick', models.FloatField(default=0.0)),
                ('medalAbilityGunslingerMulti', models.FloatField(default=0.0)),
                ('medalAbilityGunslingerQuick', models.FloatField(default=0.0)),
                ('medalAbilityJuggernautCombo', models.FloatField(default=0.0)),
                ('medalAbilityJuggernautSlam', models.FloatField(default=0.0)),
                ('medalAbilityNightstalkerLongRange', models.FloatField(default=0.0)),
                ('medalAbilityNightstalkerTetherQuick', models.FloatField(default=0.0)),
                ('medalAbilitySentinelCombo', models.FloatField(default=0.0)),
                ('medalAbilitySentinelWard', models.FloatField(default=0.0)),
                ('medalAbilityStormcallerLandfall', models.FloatField(default=0.0)),
                ('medalAbilityStormcallerMulti', models.FloatField(default=0.0)),
                ('medalAbilitySunbreakerLongRange', models.FloatField(default=0.0)),
                ('medalAbilitySunbreakerMulti', models.FloatField(default=0.0)),
                ('medalAbilityVoidwalkerDistance', models.FloatField(default=0.0)),
                ('medalAbilityVoidwalkerVortex', models.FloatField(default=0.0)),
                ('medalAvenger', models.FloatField(default=0.0)),
                ('medalControlAdvantageHold', models.FloatField(default=0.0)),
                ('medalControlAdvantageStreak', models.FloatField(default=0.0)),
                ('medalControlCaptureAllZones', models.FloatField(default=0.0)),
                ('medalControlMostAdvantage', models.FloatField(default=0.0)),
                ('medalControlPerimeterKill', models.FloatField(default=0.0)),
                ('medalControlPowerPlayWipe', models.FloatField(default=0.0)),
                ('medalCountdownDefense', models.FloatField(default=0.0)),
                ('medalCountdownDefusedLastStand', models.FloatField(default=0.0)),
                ('medalCountdownDefusedMulti', models.FloatField(default=0.0)),
                ('medalCountdownDetonated', models.FloatField(default=0.0)),
                ('medalCountdownPerfect', models.FloatField(default=0.0)),
                ('medalCountdownRoundAllAlive', models.FloatField(default=0.0)),
                ('medalCycle', models.FloatField(default=0.0)),
                ('medalDefeatHunterDodge', models.FloatField(default=0.0)),
                ('medalDefeatTitanBrace', models.FloatField(default=0.0)),
                ('medalDefeatWarlockSigil', models.FloatField(default=0.0)),
                ('medalDefense', models.FloatField(default=0.0)),
                ('medalMatchBlowout', models.FloatField(default=0.0)),
                ('medalMatchComeback', models.FloatField(default=0.0)),
                ('medalMatchMostDamage', models.FloatField(default=0.0)),
                ('medalMatchNeverTrailed', models.FloatField(default=0.0)),
                ('medalMatchOvertime', models.FloatField(default=0.0)),
                ('medalMatchUndefeated', models.FloatField(default=0.0)),
                ('medalMulti2x', models.FloatField(default=0.0)),
                ('medalMulti3x', models.FloatField(default=0.0)),
                ('medalMulti4x', models.FloatField(default=0.0)),
                ('medalMultiEntireTeam', models.FloatField(default=0.0)),
                ('medalPayback', models.FloatField(default=0.0)),
                ('medalQuickStrike', models.FloatField(default=0.0)),
                ('medalStreak10x', models.FloatField(default=0.0)),
                ('medalStreak5x', models.FloatField(default=0.0)),
                ('medalStreakAbsurd', models.FloatField(default=0.0)),
                ('medalStreakCombined', models.FloatField(default=0.0)),
                ('medalStreakShutdown', models.FloatField(default=0.0)),
                ('medalStreakTeam', models.FloatField(default=0.0)),
                ('medalSuperShutdown', models.FloatField(default=0.0)),
                ('medalSupremacyCrestCreditStreak', models.FloatField(default=0.0)),
                ('medalSupremacyFirstCrest', models.FloatField(default=0.0)),
                ('medalSupremacyNeverCollected', models.FloatField(default=0.0)),
                ('medalSupremacyPerfectSecureRate', models.FloatField(default=0.0)),
                ('medalSupremacyRecoverStreak', models.FloatField(default=0.0)),
                ('medalSupremacySecureStreak', models.FloatField(default=0.0)),
                ('medalSurvivalComeback', models.FloatField(default=0.0)),
                ('medalSurvivalKnockout', models.FloatField(default=0.0)),
                ('medalSurvivalQuickWipe', models.FloatField(default=0.0)),
                ('medalSurvivalTeamUndefeated', models.FloatField(default=0.0)),
                ('medalSurvivalUndefeated', models.FloatField(default=0.0)),
                ('medalSurvivalWinLastStand', models.FloatField(default=0.0)),
                ('medalWeaponAuto', models.FloatField(default=0.0)),
                ('medalWeaponFusion', models.FloatField(default=0.0)),
                ('medalWeaponGrenade', models.FloatField(default=0.0)),
                ('medalWeaponHandCannon', models.FloatField(default=0.0)),
                ('medalWeaponPulse', models.FloatField(default=0.0)),
                ('medalWeaponRocket', models.FloatField(default=0.0)),
                ('medalWeaponScout', models.FloatField(default=0.0)),
                ('medalWeaponShotgun', models.FloatField(default=0.0)),
                ('medalWeaponSidearm', models.FloatField(default=0.0)),
                ('medalWeaponSmg', models.FloatField(default=0.0)),
                ('medalWeaponSniper', models.FloatField(default=0.0)),
                ('medalWeaponSword', models.FloatField(default=0.0)),
                ('medalUnknown', models.FloatField(default=0.0)),
                ('allMedalsEarned', models.FloatField(default=0.0)),
                ('objectivesCompleted', models.FloatField(default=0.0)),
                ('precisionKills', models.FloatField(default=0.0)),
                ('resurrectionsPerformed', models.FloatField(default=0.0)),
                ('resurrectionsReceived', models.FloatField(default=0.0)),
                ('score', models.FloatField(default=0.0)),
                ('heroicPublicEventsCompleted', models.FloatField(default=0.0)),
                ('adventuresCompleted', models.FloatField(default=0.0)),
                ('secondsPlayed', models.FloatField(default=0.0)),
                ('activityDurationSeconds', models.FloatField(default=0.0)),
                ('standing', models.BooleanField(default=None)),
                ('suicides', models.FloatField(default=0.0)),
                ('team', models.CharField(max_length=30)),
                ('totalDeathDistance', models.FloatField(default=0.0)),
                ('totalKillDistance', models.FloatField(default=0.0)),
                ('weaponPrecisionKillsAutoRifle', models.FloatField(default=0.0)),
                ('weaponPrecisionKillsFusionRifle', models.FloatField(default=0.0)),
                ('weaponPrecisionKillsGrenade', models.FloatField(default=0.0)),
                ('weaponPrecisionKillsGrenadeLauncher', models.FloatField(default=0.0)),
                ('weaponPrecisionKillsHandCannon', models.FloatField(default=0.0)),
                ('weaponPrecisionKillsMachinegun', models.FloatField(default=0.0)),
                ('weaponPrecisionKillsMelee', models.FloatField(default=0.0)),
                ('weaponPrecisionKillsPulseRifle', models.FloatField(default=0.0)),
                ('weaponPrecisionKillsRocketLauncher', models.FloatField(default=0.0)),
                ('weaponPrecisionKillsScoutRifle', models.FloatField(default=0.0)),
                ('weaponPrecisionKillsShotgun', models.FloatField(default=0.0)),
                ('weaponPrecisionKillsSniper', models.FloatField(default=0.0)),
                ('weaponPrecisionKillsSubmachinegun', models.FloatField(default=0.0)),
                ('weaponPrecisionKillsSuper', models.FloatField(default=0.0)),
                ('weaponPrecisionKillsRelic', models.FloatField(default=0.0)),
                ('weaponPrecisionKillsSideArm', models.FloatField(default=0.0)),
                ('weaponKillsAutoRifle', models.FloatField(default=0.0)),
                ('weaponKillsFusionRifle', models.FloatField(default=0.0)),
                ('weaponKillsGrenade', models.FloatField(default=0.0)),
                ('weaponKillsGrenadeLauncher', models.FloatField(default=0.0)),
                ('weaponKillsHandCannon', models.FloatField(default=0.0)),
                ('weaponKillsMachinegun', models.FloatField(default=0.0)),
                ('weaponKillsMelee', models.FloatField(default=0.0)),
                ('weaponKillsPulseRifle', models.FloatField(default=0.0)),
                ('weaponKillsRocketLauncher', models.FloatField(default=0.0)),
                ('weaponKillsScoutRifle', models.FloatField(default=0.0)),
                ('weaponKillsShotgun', models.FloatField(default=0.0)),
                ('weaponKillsSniper', models.FloatField(default=0.0)),
                ('weaponKillsSubmachinegun', models.FloatField(default=0.0)),
                ('weaponKillsSuper', models.FloatField(default=0.0)),
                ('weaponKillsRelic', models.FloatField(default=0.0)),
                ('weaponKillsSideArm', models.FloatField(default=0.0)),
                ('weaponKillsSword', models.FloatField(default=0.0)),
                ('weaponKillsAbility', models.FloatField(default=0.0)),
                ('weaponBestType', models.CharField(max_length=30)),
                ('weaponKillsPrecisionKillsAutoRifle', models.FloatField(default=0.0)),
                ('weaponKillsPrecisionKillsFusionRifle', models.FloatField(default=0.0)),
                ('weaponKillsPrecisionKillsGrenade', models.FloatField(default=0.0)),
                ('weaponKillsPrecisionKillsGrenadeLauncher', models.FloatField(default=0.0)),
                ('weaponKillsPrecisionKillsHandCannon', models.FloatField(default=0.0)),
                ('weaponKillsPrecisionKillsMachinegun', models.FloatField(default=0.0)),
                ('weaponKillsPrecisionKillsMelee', models.FloatField(default=0.0)),
                ('weaponKillsPrecisionKillsPulseRifle', models.FloatField(default=0.0)),
                ('weaponKillsPrecisionKillsRocketLauncher', models.FloatField(default=0.0)),
                ('weaponKillsPrecisionKillsScoutRifle', models.FloatField(default=0.0)),
                ('weaponKillsPrecisionKillsShotgun', models.FloatField(default=0.0)),
                ('weaponKillsPrecisionKillsSniper', models.FloatField(default=0.0)),
                ('weaponKillsPrecisionKillsSubmachinegun', models.FloatField(default=0.0)),
                ('weaponKillsPrecisionKillsSuper', models.FloatField(default=0.0)),
                ('weaponKillsPrecisionKillsRelic', models.FloatField(default=0.0)),
                ('weaponKillsPrecisionKillsSideArm', models.FloatField(default=0.0)),
                ('winLossRatio', models.FloatField(default=0.0)),
                ('uniqueWeaponAssists', models.FloatField(default=0.0)),
                ('uniqueWeaponAssistDamage', models.FloatField(default=0.0)),
                ('uniqueWeaponKills', models.FloatField(default=0.0)),
                ('uniqueWeaponPrecisionKills', models.FloatField(default=0.0)),
                ('uniqueWeaponKillsPrecisionKills', models.FloatField(default=0.0)),
                ('allParticipantsCount', models.FloatField(default=0.0)),
                ('allParticipantsScore', models.FloatField(default=0.0)),
                ('allParticipantsTimePlayed', models.FloatField(default=0.0)),
                ('activityAssists', models.FloatField(default=0.0)),
                ('completionReason', models.FloatField(default=0.0)),
                ('fireteamId', models.CharField(max_length=30)),
                ('longestKillSpree', models.FloatField(default=0.0)),
                ('longestSingleLife', models.FloatField(default=0.0)),
                ('mostPrecisionKills', models.FloatField(default=0.0)),
                ('orbsDropped', models.FloatField(default=0.0)),
                ('orbsGathered', models.FloatField(default=0.0)),
                ('startSeconds', models.FloatField(default=0.0)),
                ('timePlayedSeconds', models.FloatField(default=0.0)),
                ('playerCount', models.FloatField(default=0.0)),
                ('activityPrecisionKills', models.FloatField(default=0.0)),
                ('publicEventsCompleted', models.FloatField(default=0.0)),
                ('remainingTimeAfterQuitSeconds', models.FloatField(default=0.0)),
                ('teamScore', models.FloatField(default=0.0)),
                ('totalActivityDurationSeconds', models.FloatField(default=0.0)),
                ('dailyMedalsEarned', models.FloatField(default=0.0)),
                ('combatRating', models.FloatField(default=0.0)),
                ('lbMostPrecisionKills', models.FloatField(default=0.0)),
                ('lbLongestKillSpree', models.FloatField(default=0.0)),
                ('lbLongestKillDistance', models.FloatField(default=0.0)),
                ('lbFastestCompletionMs', models.FloatField(default=0.0)),
                ('lbLongestSingleLife', models.FloatField(default=0.0)),
                ('dailyfastestCompletionMs', models.FloatField(default=0.0)),
                ('fastestCompletionMs', models.FloatField(default=0.0)),
                ('longestKillDistance', models.FloatField(default=0.0)),
                ('highestCharacterLevel', models.FloatField(default=0.0)),
                ('highestLightLevel', models.FloatField(default=0.0)),
                ('highestSandboxLevel', models.FloatField(default=0.0)),
                ('controlZonesCaptured', models.FloatField(default=0.0)),
                ('controlZonesNeutralized', models.FloatField(default=0.0)),
                ('controlZoneDefensiveKills', models.FloatField(default=0.0)),
                ('controlZoneOffensiveKills', models.FloatField(default=0.0)),
                ('supremacyOwnKillEnemyTagsCaptured', models.FloatField(default=0.0)),
                ('supremacyAllyKillEnemyTagsCaptured', models.FloatField(default=0.0)),
                ('supremacyOwnTagsRecovered', models.FloatField(default=0.0)),
                ('supremacyAllyTagsRecovered', models.FloatField(default=0.0)),
                ('completedTrialsLostTicket', models.BooleanField(default=None)),
                ('completedTrialsPerfectTicket', models.BooleanField(default=None)),
                ('completedTrialsWonTicket', models.BooleanField(default=None)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ParticipationInstances', to='clan.Character')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=30)),
                ('membership_id', models.CharField(max_length=30)),
                ('membership_type', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamName', models.CharField(max_length=30)),
                ('teamId', models.CharField(max_length=30)),
                ('score', models.FloatField(default=0)),
                ('is_winner', models.BooleanField(default=None)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Teams', to='clan.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='UpdateIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activities', models.BooleanField(default=False)),
                ('pgcrs', models.BooleanField(default=False)),
                ('teams', models.BooleanField(default=False)),
                ('participants', models.BooleanField(default=False)),
                ('weapons', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referenceId', models.CharField(max_length=30)),
                ('kills', models.FloatField(default=0)),
                ('precisionKills', models.FloatField(default=0)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Weapons', to='clan.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='ClanMember',
            fields=[
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='ClanMember', serialize=False, to='clan.Player')),
                ('clan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ClanMembers', to='clan.Clan')),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='related_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Participants', to='clan.Team'),
        ),
        migrations.AddField(
            model_name='character',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Characters', to='clan.Player'),
        ),
        migrations.AddField(
            model_name='activity',
            name='characters',
            field=models.ManyToManyField(related_name='Activities', to='clan.Character'),
        ),
    ]
