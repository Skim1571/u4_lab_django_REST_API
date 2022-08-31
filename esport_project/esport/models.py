from django.db import models

# Create your models here.
# tunr/models.py
class Team(models.Model):
  name = models.CharField(max_length=100)
  nationality = models.CharField(max_length=100)
  team_logo_url = models.TextField(null=True)

  def __str__(self):
    return self.name

class Player(models.Model):
  team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
  name = models.CharField(max_length=100)
  handle = models.CharField(max_length=100, null=True)

  def __str__(self):
    return self.name