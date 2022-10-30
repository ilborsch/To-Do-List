from . import views
from django.urls import path


urlpatterns = [
    path('', views.get_welcome_page, name='main_page'),
    path('registration/', views.get_registration_page, name='registration'),
    path('authorisation/', views.get_authorisation_page, name='authorisation'),
    path('about/', views.get_about_page, name='about_us'),
    path('profile/<slug:user_slug>', views.get_user_profile_page, name='user_profile'),
]