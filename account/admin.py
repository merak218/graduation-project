from django.contrib import admin
from .models import (Profile, Post, PostAdmin, PostPay)
# Register your models here.

admin.site.register(Profile)
admin.site.register(Post, PostAdmin)
admin.site.register(PostPay)