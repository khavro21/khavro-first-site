
from django.contrib import admin
from django.urls import path, include
from Tmy_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Tmy_app.urls')),
]
