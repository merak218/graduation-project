from django.db import models
from django.urls import reverse


# Create your models here.
class Edition(models.Model):
    edit_name = models.CharField(max_length=100)
    edit_img = models.ImageField(upload_to='edition_img', blank=True)
    charge = models.IntegerField()

    def __str__(self):
        return self.edit_name

    def save(self, *args, **kwargs):
        super().save()
    
    def get_absolute_url(self):
        return reverse("manager:edit-list")

class User(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super().save()
    
    def get_absolute_url(self):
        return reverse("manager:user-list")



    