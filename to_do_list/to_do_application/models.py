from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class UserModel(User):

    slug = models.SlugField()
    profile_photo = models.ImageField(upload_to='to_do_application/media/user_photos',
                                      default='to_do_application/media/user_photos/profile-icon-9.png')


    def get_absolute_url(self):
        return reverse('user-profile', args=['slug'])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(args, kwargs)

    def __str__(self):
        return f"User: {self.username}"


class Task(models.Model):
    is_completed = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)
    title = models.CharField(max_length=60, default="")
    description = models.CharField(max_length=250, default="")
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title




