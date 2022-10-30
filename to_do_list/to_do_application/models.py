from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Task(models.Model):
    is_completed = models.BooleanField(default=False)


class User(models.Model):
    username = models.CharField(max_length=24, null=False, default='Username')
    password = models.CharField(max_length=36, null=False)
    tasks = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    slug = models.SlugField()
    email = models.EmailField(max_length=64, null=True)

    def get_absolute_url(self):
        return reverse('user-profile', args=['slug'])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(args, kwargs)

    def __str__(self):
        return f"User: {self.username}"




