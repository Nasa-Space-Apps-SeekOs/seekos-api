from django.db import models
from enum import Enum
REPOSITORY_TYPE = (
    ('idea', 'Idea'),
    ('project', 'Project'),
)

REPOSITORY_PHASES = (
    ('init', 'Init'),
    ('development', 'Development'),
    ('test', 'Test'),
    ('concluded', 'Concluded'),
)

class Repository(models.Model):

    class Meta:
        db_table = 'repository'

    members = models.ManyToManyField('User', through='RUserRepositoryMember', related_name='member_repositories')
    likes = models.ManyToManyField('User', related_name='liked_repositories')
    
    name = models.CharField(max_length=100)
    resume = models.CharField(max_length=100)
    body = models.TextField(default='Default Body Text')
    type = models.CharField(
        max_length=100,
        choices=REPOSITORY_TYPE,
        default=REPOSITORY_TYPE[0][0]
    )
    phases = models.CharField(
        max_length=100,
        choices=REPOSITORY_PHASES,
        default=REPOSITORY_PHASES[0][0]
    )
    ranking = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
