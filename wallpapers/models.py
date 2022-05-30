from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=35)
    caption = models.TextField(default='caption')
    photo = CloudinaryField('image',default='photo.jpeg')
    username = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    posted_on = models.DateTimeField(default=timezone.now)


class Meta:
    ordering = ['posted_on']

def __str__(self):
    return self.name

def save_image(self):
    self.save()

def delete_image(self):
    self.delete()

def get_absolute_url(self):
    return reverse('image-detail')

# def update_image(self):
#   fetched_object = Image.objects.filter(author=current_value).update(author=new_value)
#   return fetched_object