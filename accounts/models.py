from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class Role(models.Model):
    ADMIN = 'admin'
    ADMIN_ASSISTANT = 'admin_assistant'
    NORMAL_USER = 'normal_user'
    INTERMEDIATE_USER = 'intermediate_user'
    CHOICES_ROLES = (
                    (ADMIN, 'admin'),
                    (ADMIN_ASSISTANT, 'admin assistant'),
                    (NORMAL_USER, 'normal user'),
                    (INTERMEDIATE_USER, 'intermediate user'),
                  )
    name = models.CharField(choices=CHOICES_ROLES, max_length=20, default=NORMAL_USER)
    permission = models.CharField(max_length=7, validators=[RegexValidator('[01]{7}',
                                                                           message='this permission is invalid')])

    @classmethod
    def get_default_for_permission_user(cls):
        role, created = cls.objects.get_or_create(name=cls.NORMAL_USER, permission="0000011")
        return role.pk

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):

    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=11, validators=[RegexValidator(regex='09[0-9]{9}',
                                                                       message='This phone number is incorrect!')])
    permission = models.ForeignKey(Role, on_delete=models.CASCADE,
                                   related_name='users', default=Role.get_default_for_permission_user)
