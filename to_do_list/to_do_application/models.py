from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class UserModel(User):
    """
    'to_do_application_usermodel' TABLE.
    COLUMNS:
        - user_ptr_id ,
        - slug ,
        - profile_photo .
    """

    slug = models.SlugField()
    profile_photo = models.ImageField(upload_to='to_do_application/media/user_photos',
                                      default='to_do_application/media/user_photos/profile-icon-9.png')


    def get_absolute_url(self):
        """
        :return: The function returns absolute url path for the model instance's profile page.
        """
        return reverse('user-profile', args=['slug'])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(args, kwargs)

    def __str__(self):
        return f"User: {self.username}"


class Task(models.Model):
    """
    'to_do_application_task' TABLE.
    COLUMNS:
        - is_completed ,
        - description ,
        - is_public ,
        - title ,
        - user_id .
    """
    is_completed = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)
    title = models.CharField(max_length=60, default="")
    description = models.CharField(max_length=250, default="")
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title




