from django.contrib import admin

# Register your models here.
from blog.models import Team, Stadium, Match

admin.site.register(Team)
admin.site.register(Stadium)
admin.site.register(Match)