from django.db import models
from enum import Enum
REPOSITORY_TYPE = (
    ('idea', 'Idea'),
    ('project', 'Project'),
)

REPOSITORY_STATUS = (
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
    keys = models.ManyToManyField('Keys', related_name='keys_repositories')
    name = models.CharField(max_length=100)
    resume = models.CharField(max_length=250)
    url_image = models.CharField(max_length=500, null=True, blank=True)
    url_project = models.CharField(max_length=500, null=True, blank=True)
    body = models.TextField(default='Default Body Text', null=True, blank=True)
    type = models.CharField(
        max_length=100,
        choices=REPOSITORY_TYPE,
        default=REPOSITORY_TYPE[0][0]
    )
    status = models.CharField(
        max_length=100,
        choices=REPOSITORY_STATUS,
        default=REPOSITORY_STATUS[0][0],
        null=True,
    )
    ranking = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
