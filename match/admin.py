from django.contrib import admin
from .models import Match, Team, TeamPlayer, PlayerMatch


admin.site.register(Team)
admin.site.register(Match)
admin.site.register(TeamPlayer)
admin.site.register(PlayerMatch)
