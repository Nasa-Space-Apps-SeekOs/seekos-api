from django.db import models
from django.contrib.auth.models import AbstractUser


class Country(models.Model):
    class Meta:
        db_table = "country"
        verbose_name = ("Country")
        verbose_name_plural = ("Countries")
    
    name = models.CharField(max_length=100, null=False, blank=False)
    code = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):   
    location = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username
