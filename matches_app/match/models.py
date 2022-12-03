from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        abstract=True


class Team(BaseModel):
    name = models.CharField(primary_key=True, max_length=25, unique=True)


class Stadium(BaseModel):
    name = models.CharField(primary_key=True, max_length=25, unique=True)
    capacity = models.IntegerField(null=True, blank=True)


class Match(BaseModel):
    local = models.ForeignKey(Team, related_name='local', on_delete=models.CASCADE)
    away = models.ForeignKey(Team, related_name='away', on_delete=models.CASCADE)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    local_goals = models.IntegerField()
    away_goals = models.IntegerField()

    class Meta:
        unique_together = ('local', 'away')