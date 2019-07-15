from django.db import models
from django.contrib.auth.models import  User
from django.conf import settings
class Posts(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=255)
    #we can use User instead but when you switch to a Custom User Model. the method AUTH_USER_MODEL is the best practice for long term development.
    author = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE ,blank=True , null=True)
    def __str__(self):
        return self.title





class Comments(models.Model):
    text = models.CharField(max_length=255)
    related_post = models.ForeignKey(Posts,on_delete=models.CASCADE)
    related_user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)

    def __str__(self):
        return 'comment for : %s' %(self.related_post)


# Create your models here.


