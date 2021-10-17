from django.contrib import admin

# Register your models here.

#Registering the class model djangoClasses here and then migrated into the project
from .models import djangoClasses

admin.site.register(djangoClasses)