 # pyright: ignore[reportMissingImports]
from djongo import models

# User model
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username

# Team model
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ArrayReferenceField(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Activity model
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField(help_text="Duration in minutes")
    calories_burned = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} on {self.date}"

# Workout model
class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Leaderboard model
class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    total_points = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.team.name} - Rank {self.rank}"
