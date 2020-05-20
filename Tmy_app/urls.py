from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('new_search', views.SearchView.as_view(), name='new_search'),
    path('Moscow_info', views.moscow_info, name='moscow_info'),
    path('Nuremberg_info', views.nuremberg_info, name='nuremberg_info'),
    path('Lisbon_info', views.lisbon_info, name='lisbon_info'),
    path('Madeira_info', views.madeira_info, name='madeira_info'),
    path('contacts', views.contacts, name='contacts'),
    path('about_us', views.about_us, name='about_us'),

    # Users
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('login', auth_views.LoginView.as_view(template_name='Tmy_app/users/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='Tmy_app/users/logout.html'), name='logout'),
    path('feedback_page', PostListView.as_view(), name='feedback_page'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
