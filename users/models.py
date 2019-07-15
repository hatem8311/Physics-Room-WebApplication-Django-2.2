from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
class User_Profile(models.Model):
    HIGHSCHOOL = 'HIGHSCHOOL'
    UNIVERSITY = 'UNIVERSITY'
    GRADUATED = 'GRADUATED'
    EDUCATION_STATUS = [
        (HIGHSCHOOL,'HIGHSCHOOL'),
        (UNIVERSITY , 'UNIVERSITY'),
        (GRADUATED , 'GRADUATED')
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name =models.CharField(max_length=255)
    age = models.PositiveIntegerField(default=0)
    phone_number = models.PositiveIntegerField(default=0)
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=255)
    education = models.CharField(max_length=255,choices=EDUCATION_STATUS , default=GRADUATED)
    profile_picture = models.ImageField(upload_to='profiles/images/'  , null=True,blank=True)





@receiver(post_save , sender=User)
def createprofile(sender , instance , created, **kwargs):
	if created:
		User_Profile.objects.create(user = instance)
# Create your models here.
