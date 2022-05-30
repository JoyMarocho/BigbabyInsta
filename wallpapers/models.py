from django.db import models
from django.utils import timezone
from location_field.models.plain import PlainLocationField
from cloudinary.models import CloudinaryField

# Create your models here.
class Photo(models.Model):
    photo_name = models.CharField(max_length = 255)
    description = models.TextField(default=1)
    image = CloudinaryField('image', default='/media/default.jpg')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)
    city = models.ForeignKey('City', on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.photo_name

    def save_photo(self):
        self.save()

    def delete_photo(self):
        self.delete()