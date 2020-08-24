from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
from django.utils.timezone import now

class User(AbstractUser):
    pass

class History(models.Model):
    playerid = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gameplayer")
    playeridnumber = models.CharField(max_length=10,default="N/A")
    difficulitylevel = models.CharField(max_length=10)
    guessnumber= models.CharField(max_length=100, default="No Record")
    date = models.DateTimeField(default=now)
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.playerid} -  {self.difficulitylevel} - {self.guessnumber} - {self.date} - {self.status}"
