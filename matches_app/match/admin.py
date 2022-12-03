from django.contrib import admin

# Register your models here.
from match.models import Team, Stadium, Match

admin.site.register(Team)
admin.site.register(Stadium)
admin.site.register(Match)