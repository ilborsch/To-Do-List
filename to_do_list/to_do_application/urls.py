from django.conf.urls.static import static
from django.conf import settings

from . import views
from django.urls import path


urlpatterns = [
    path('', views.get_welcome_page, name='main_page'),
    path('registration/', views.get_registration_page, name='registration'),
    path('login/', views.UserLoginView.as_view(), name='authorisation'),
    path('about/', views.get_about_page, name='about_us'),
    path('profile/<str:user_name>/', views.get_user_profile_page, name='user_profile'),
    path('logout_successful/', views.logout_user, name='logout'),
    path('tasks/<int:task_id>/', views.get_user_tasks_page, name='tasks'),
    path('tasks/<str:user_name>/', views.get_user_tasks_page, name='tasks'),
    path('create_new_task/<str:user_name>/', views.create_new_task, name='create_new_task'),
    path('change_task/<str:user_name>/<int:task_id>/', views.get_change_task_page, name='change_task'),
    path('completed_task/<str:user_name>/<int:task_id>/', views.get_completed_task, name='completed_task'),
    path('search_for_people/', views.get_search_page, name='search_users')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)