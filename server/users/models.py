from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='user/', default='default.png')

    def __str__(self):
        return self.username
