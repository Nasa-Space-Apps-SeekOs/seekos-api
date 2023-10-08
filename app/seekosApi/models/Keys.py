from django.db import models

class Keys(models.Model):
    class Meta:
        db_table = "keys"
    
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name