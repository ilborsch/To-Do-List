from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import User
from .models import UserModel


class UserRegistration(UserCreationForm):
    """
    User Registration Form used in get_registration_page() view from .views .
    Generates form for registration.html template.
    FIELDS:
        - username: User username (required);
        - email: User Email (required);
        - password1: User password (required);
        - password2: User password confirmation (required).

    VALIDATORS:
        - username: Checks, if username is UNIQUE in the .models.User model.
        - email: Checks, if email is UNIQUE in the .models.User model.
    """

    username = forms.CharField(label='Username', max_length=24, min_length=3,
                               widget=forms.TextInput(attrs={"class": 'login-input'}))

    email = forms.EmailField(label='Email', max_length=64,
                             widget=forms.EmailInput(attrs={"class": 'email-input'}))

    password1 = forms.CharField(label='Password', max_length=24, min_length=4,
                                widget=forms.PasswordInput(attrs={'class': 'psswrd-input'}))

    password2 = forms.CharField(label='Password confirmation', max_length=24, min_length=4,
                                widget=forms.PasswordInput(attrs={'class': 'psswrd-input'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        users_with_same_username = User.objects.filter(username=username)
        if users_with_same_username:
            raise ValidationError("Username must be unique, sorry.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        users_with_same_email = User.objects.filter(email=email)
        if users_with_same_email:
            raise ValidationError("Email must be unique, sorry.")
        return email


class UserLoginForm(AuthenticationForm):
    """
    User Login Form used in UserLoginView view from .views .
    Generates form for login.html template.
    FIELDS:
        - username: User username (required);
        - password: User password (required);
    """

    username = forms.CharField(label='Username or Email', widget=forms.TextInput())
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class UserTasksForm(forms.Form):
    """
    User Login Form used in
    create_new_task(), get_change_task_page() views from .views .
    Generates form for create_new_task.html, change_task.html templates.
    FIELDS:
        - title: Task title (required);
        - description: Task description (required);
        - is_public: Task public boolean field (initial = True).
    """

    title = forms.CharField(label="Title", widget=forms.TextInput())
    description = forms.CharField(label="Description", widget=forms.TextInput())
    is_public = forms.BooleanField(label="Public", widget=forms.CheckboxInput(),
                                   required=False, initial=True)


class ProfileImageForm(forms.ModelForm):
    """
    User Profile avatar image form used in get_user_profile_page() view from .views .
    Generates form for user_profile.html templates.
    FIELDS:
        - profile_photo: User profile image choose (optional).
    """

    class Meta:
        model = UserModel
        fields = ['profile_photo']
        widgets = {'profile-photo': forms.ClearableFileInput()}


