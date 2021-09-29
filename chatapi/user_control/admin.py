from django.contrib import admin

from user_control.models import CustomUser, Jwt

# Register your models here.

admin.site.register((CustomUser, Jwt, ), )
