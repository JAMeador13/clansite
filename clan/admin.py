from django.contrib import admin
from .models import Clan, Player, ClanMember, Character, Activity, Team, Participant, Weapon, Cursor


class ClanAdmin(admin.ModelAdmin):
    pass
admin.site.register(Clan, ClanAdmin)



class PlayerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Player, PlayerAdmin)



class ClanMemberAdmin(admin.ModelAdmin):
    pass
admin.site.register(ClanMember, ClanMemberAdmin)



class CharacterAdmin(admin.ModelAdmin):
    raw_id_fields = ['player']
admin.site.register(Character, CharacterAdmin)



class ActivityAdmin(admin.ModelAdmin):
    raw_id_fields = ['characters']
    exclude = ('pgcr',)
admin.site.register(Activity, ActivityAdmin)



class TeamAdmin(admin.ModelAdmin):
    raw_id_fields = ['activity']
admin.site.register(Team, TeamAdmin)



class ParticipantAdmin(admin.ModelAdmin):
    raw_id_fields = ['related_team']
    exclude = ('weapons',)
admin.site.register(Participant, ParticipantAdmin)



class WeaponAdmin(admin.ModelAdmin):
    raw_id_fields = ['participant']
admin.site.register(Weapon, WeaponAdmin)



class CursorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cursor, CursorAdmin)
