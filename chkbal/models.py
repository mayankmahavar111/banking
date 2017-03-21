from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from django.core.urlresolvers import reverse


class account(models.Model):
    name=models.CharField(max_length=100,default='')
    accountno = models.CharField(max_length=16, default=0)
    IFSC_Code = models.CharField(max_length=16, default=0)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='unknown')
    phone = models.CharField(max_length=10, default=00000000)

    def get_absolute_url(self):
        return reverse('chkbal:profile',kwargs={'pk':self.pk})

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user= models.OneToOneField(User)
    accountno=models.CharField(max_length=16,default='')
    IFSC_Code = models.CharField(max_length=16, default='')
    name=models.CharField(max_length=100,default='')
    description= models.CharField(max_length=100,default='')
    city=models.CharField(max_length=100,default='')
    phone=models.CharField(max_length=10,default='')
    address=models.CharField(max_length=100,default='')
    balance=models.CharField(max_length=100,default=500)

    def __str__(self):
        return self.name

def create_profile(sender ,**kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])



post_save.connect(create_profile, sender=User)