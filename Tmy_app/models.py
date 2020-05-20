from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.search

    class Meta:
        verbose_name_plural = 'Searches'


class CityClass(models.Model):
    created = models.DateTimeField(auto_now=True)
    city_name = models.CharField(
        null=False,
        max_length=300
    )

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name_plural = 'City Classes'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    user_info = models.TextField(blank=True)


    def __str__(self):
        return f"{self.user.username} Profile"
