from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings


def dome_directory_path_banner(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    banner_pic_name = 'user_{0}/domebanner_{1}'.format(instance.user.id, filename)
    full_path = os.path.join(settings.MEDIA_ROOT, banner_pic_name)

    if os.path.exists(full_path):
        os.remove(full_path)
    return banner_pic_name

def dome_directory_path_picture(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    picture_pic_name = 'user_{0}/domepicture_{1}'.format(instance.user.id, filename)
    full_path = os.path.join(settings.MEDIA_ROOT, picture_pic_name)

    if os.path.exists(full_path):
        os.remove(full_path)
    return picture_pic_name


class Dome(models.Model):
    picture = models.ImageField(upload_to=dome_directory_path_picture, null=False)
    banner = models.ImageField(upload_to=dome_directory_path_banner, null=False)
    title = models.CharField(max_length=25, null=False, blank=False)
    description = models.CharField(max_length=144, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='server_owner')
    members = models.ManyToManyField(User, related_name='server_members')
    moderators = models.ManyToManyField(User, related_name='server_moderators')
    # categories = models.ManyToManyField(Category)
    PRIVACY_CHOICES = ((1,'Public'), (0,'Private'),)
    privacy = models.IntegerField(choices=PRIVACY_CHOICES, default=1)
        
    def __str__(self):
        return self.title
    
class Category(models.Model):
    title = models.CharField(max_length=35)
    # text_channels = models.ManyToManyField(TextChannels)
    Dome = models.ForeignKey(Dome,related_name='categories',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

