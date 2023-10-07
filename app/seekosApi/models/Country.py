from django.db import models

class Country(models.Model):
    class Meta:
        db_table = "country"
        verbose_name = ("Country")
        verbose_name_plural = ("Countries")
    
    name = models.CharField(max_length=100, null=False, blank=False)
    code = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.name