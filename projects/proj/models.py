from typing import Text
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

class Project(models.Model):
    tittle = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=CASCADE, default=0)


class Chore(models.Model):
    project = models.ForeignKey(Project, on_delete=CASCADE)
    tittle = models.CharField(max_length=200)
    text = models.CharField(max_length=500, default="")
    done = models.BooleanField(default=False)