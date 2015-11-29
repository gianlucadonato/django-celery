from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models

class User(AbstractBaseUser):
    username                = models.CharField(max_length=42, unique=True)
    email                   = models.EmailField(unique=True, null=True, blank=False)
    first_name              = models.CharField(max_length=42, null=True, blank=False)
    last_name               = models.CharField(max_length=42, null=True, blank=False)
    profile_image_url       = models.URLField(max_length=255, null=True, blank=False)
    
    facebook_id             = models.CharField(max_length=255, null=True, blank=False)
    facebook_access_token   = models.CharField(max_length=255, null=True, blank=False)
    twitter_id              = models.CharField(max_length=255, null=True, blank=False)
    twitter_access_token    = models.CharField(max_length=255, null=True, blank=False)

    is_admin    = models.BooleanField(default=False)

    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['username']

    def __unicode__(self):
        return self.username

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])
