from django.contrib.auth.models import User
from django.db import models

# Directory where profile pictures will be uploaded
UPLOAD_TO = 'profile_pics/'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to=UPLOAD_TO)
