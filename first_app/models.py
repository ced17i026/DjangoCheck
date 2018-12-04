from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)
    def __str__(self):
        return self.top_name
class webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)
    def __str__(self):
        return self.name
class AccessRecord(models.Model):
    name = models.ForeignKey(webpage,on_delete=models.CASCADE)
    date = models.DateField()
    def __str__(self):
        return str(self.date)
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #another fields 
    url_site = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pic',blank=True)
    def __str__(self):
        return self.user.username