from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Task(models.Model):
    is_completed = models.BooleanField(default=False)


class UserModel(User):

    tasks = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('user-profile', args=['slug'])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(args, kwargs)

    def __str__(self):
        return f"User: {self.username}"




