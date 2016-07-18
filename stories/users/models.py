from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):

    user = models.OneToOneField(User, related_name='profile')

    facebook_id = models.BigIntegerField(null=True, blank=True, unique=True)
    facebook_access_token = models.CharField(max_length=300, blank=True, null=True)
