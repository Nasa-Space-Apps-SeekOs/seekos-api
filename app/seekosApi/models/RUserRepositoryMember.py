from django.db import models

class RUserRepositoryMember(models.Model):
    class Meta:
        db_table = "r_user_repository_member"
        verbose_name = ("r_user_repository_members")
        verbose_name_plural = ("r_user_repository_members")

    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True)
    repository = models.ForeignKey('Repository', on_delete=models.CASCADE, null=True, blank=True)
    is_property = models.BooleanField(default=False)

    def __str__(self):
        return self.name