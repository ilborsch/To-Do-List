from django.contrib import admin
from .models import UserModel, Task

admin.site.register(UserModel)
admin.site.register(Task)

