from django.contrib import admin
from .models import Search, CityClass, Post, Profile

# Register your models here.

admin.site.register(Search)
admin.site.register(CityClass)
admin.site.register(Post)
admin.site.register(Profile)