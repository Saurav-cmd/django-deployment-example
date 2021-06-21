from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserprofileDetail(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to = 'profile_pics',blank = True)
    site_protifilo = models.URLField(blank = True)

    def __str__(self):
        return self.user.username
