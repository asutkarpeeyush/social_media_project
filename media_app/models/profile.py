from django.db import models
from django.contrib.auth.models import User
from .common import MetaInfo


class Profile(MetaInfo):
    user = models.ForeignKey(
        User, related_name='profile', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = "profile"
