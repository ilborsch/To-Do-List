from django.contrib import admin
from .models import UserModel, Task


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'profile_photo')
    empty_value_display = 'unknown'
    ordering = ['username', 'email']
    readonly_fields = ['username']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'is_completed', 'is_public')
    empty_value_display = 'unknown'
    ordering = ['user', 'title', 'description']
    readonly_fields = ['user', 'is_completed', 'is_public']

