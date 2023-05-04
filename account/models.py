from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import User
from PIL import Image
from datetime import datetime
from django.urls import reverse
from django.contrib import admin
from manager.models import Edition
from django.shortcuts import get_object_or_404

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)

        if img.height > 300 or img.width >300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Post(models.Model):
    # auto_increment_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    edition = models.ForeignKey(Edition, null=True, blank=True, on_delete=models.SET_NULL, related_name='choose_edition')
    title = models.CharField(max_length=100)
    date_post = models.DateField()
    video_url = models.CharField(max_length=100, blank=True, null=True)
    mar_text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='act_img/%Y%m%d/', blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    qrcode = models.ImageField(default='', upload_to='act_qr', blank=True,null=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # super().save()
        created = not self.pk
        super().save()
        if created:
            PostPay.objects.create(act_name=self)

    def get_absolute_url(self):
        return reverse("account:post-detail", kwargs={"pk": self.pk})
    
class PostPay(models.Model):
    act_name = models.ForeignKey(Post, null=True, blank=True, on_delete=models.SET_NULL, related_name='title_set')
    edition = models.ForeignKey(Edition, null=True, blank=True, on_delete=models.SET_NULL, related_name='edititon_set')
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.act_name}'
    
    def save(self, *args, **kwargs):
        super().save()
    
    def get_absolute_url(self):
        return reverse("manager:notpay-list")

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class Customized(models.Model):
    contact = models.ForeignKey(User, on_delete=models.CASCADE)
    field = models.TextField()
    charge = models.IntegerField()
    note = models.TextField(null=True, blank=True,)
    date = models.DateField()

    def __str__(self):
        return f'{self.contact}'

    def save(self, *args, **kwargs):
            super().save()

    def get_absolute_url(self):
        return reverse('account:user-home')