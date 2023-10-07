from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):   
    class Meta:
        db_table = "user"
        verbose_name = ("User")
        verbose_name_plural = ("Users")
    location = models.ForeignKey('Country', on_delete=models.CASCADE, null=True, blank=True)
    keys = models.ManyToManyField('Keys', related_name='users_keys')

    def __str__(self):
        return self.username