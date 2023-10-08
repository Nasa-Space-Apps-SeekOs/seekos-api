from django.db import models
from enum import Enum

class RepositoryComment(models.Model):

    class Meta:
        db_table = 'repository_comment'
        
    repository = models.ForeignKey('Repository', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    comment = models.CharField(max_length=300)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
