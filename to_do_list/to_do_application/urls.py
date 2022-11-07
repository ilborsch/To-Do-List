from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path


urlpatterns = [
    path('', views.get_welcome_page, name='main_page'),
    path('registration/', views.get_registration_page, name='registration'),
    path('login/', views.UserLoginView.as_view(), name='authorisation'),
    path('about/', views.get_about_page, name='about_us'),  # about us page
    path('profile/<str:user_name>/', views.get_user_profile_page, name='user_profile'),
    path('logout_successful/', views.logout_user, name='logout'),   # logout redirect page
    path('tasks/<int:task_id>/', views.get_user_tasks_page, name='tasks'),  # \/

    #  /\ /\ /\ Redirect link from DELETE TASK button. Deletes the task by its unique id. POST method.

    path('tasks/<str:user_name>/', views.get_user_tasks_page, name='tasks'),  # \/

    #  /\ /\ /\ List of user tasks. GET method url.

    path('create_new_task/<str:user_name>/', views.create_new_task, name='create_new_task'),  # create task form
    path('change_task/<str:user_name>/<int:task_id>/', views.get_change_task_page, name='change_task'),
    path('completed_task/<str:user_name>/<int:task_id>/', views.get_completed_task, name='completed_task'),
    path('search_for_people/', views.get_search_page, name='search_users'),
    path('change-password/<str:user_name>', views.get_change_user_password_page, name='change_password'),

    # path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # MEDIA images url include.
