from django.contrib import admin
from .models import UserModel, Task


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    """
    .models.UserModel ADMIN PANEL.
    CHANGE FIELDS == 'email', 'profile_photo'.
    READONLY FIELDS == 'username'.
    """

    list_display = ('username', 'email', 'profile_photo')
    empty_value_display = 'unknown'
    ordering = ['username', 'email']
    readonly_fields = ['username']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    .models.Task ADMIN PANEL.
    CHANGE FIELDS == 'title', 'description'.
    READONLY FIELDS == 'user', 'is_completed', 'is_public'.
    """

    list_display = ('user', 'title', 'description', 'is_completed', 'is_public')
    empty_value_display = 'unknown'
    ordering = ['user', 'title', 'description']
    readonly_fields = ['user', 'is_completed', 'is_public']

