# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Client(models.Model):

    #__Client_FIELDS__
    client_id = models.IntegerField(null=True, blank=True)
    client_name = models.TextField(max_length=255, null=True, blank=True)
    client_location = models.TextField(max_length=255, null=True, blank=True)
    client_added = models.DateTimeField(blank=True, null=True, default=timezone.now)
    client_last_seen = models.DateTimeField(blank=True, null=True, default=timezone.now)
    client_status = models.DateTimeField(blank=True, null=True, default=timezone.now)
    client_vendor = models.TextField(max_length=255, null=True, blank=True)
    client_changed = models.BooleanField()

    #__Client_FIELDS__END

    class Meta:
        verbose_name        = _("Client")
        verbose_name_plural = _("Client")


class Tokens(models.Model):

    #__Tokens_FIELDS__
    client_id = models.ForeignKey(client, on_delete=models.CASCADE)

    #__Tokens_FIELDS__END

    class Meta:
        verbose_name        = _("Tokens")
        verbose_name_plural = _("Tokens")



#__MODELS__END
