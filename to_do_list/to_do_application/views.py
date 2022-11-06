from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import UserModel, Task
from django.contrib.auth.views import LoginView
from django.shortcuts import render, reverse
from .forms import UserRegistration, UserLoginForm, UserTasksForm, ProfileImageForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.db.models import Count, Q

# Create your views here.


def get_welcome_page(request):
    """
    main_page.html render view.
    VARIABLES:
        - points: text used in main_page.html (just more convenient here instead of html document lol)
    """

    main_page_text = ['Play and become better - Complete the planned tasks and gain the highest level!',
                      'Be more successful than others.',
                      'Or be more successful together.',
                      'Your choice - your career.', ]

    return render(request, 'to_do_application/main_page.html', context={
        'points': main_page_text,
    })


def get_registration_page(request):
    """
    registration.html OR user_profile.html render view.
    In POST method case the function proceed Register form and send
    the data into 'to_do_application_usermodel' TABLE.
    After, user get automatically authorised and logged into his account.
    Otherwise, form is unvalid or request.method == "GET" - renders registration.html.
    VARIABLES:
        - form: UserRegistration form .
    """

    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            new_user = UserModel.objects.create_user(
                username=username,
                password=password,
                email=email
            )

            login(request,
                  authenticate(username=username, password=password))

            return HttpResponseRedirect(reverse('user_profile', args=[form.cleaned_data['username']]))

    else:
        form = UserRegistration()
    return render(request, 'to_do_application/registration.html', context={
        'form': form,
    })


def get_about_page(request):
    """
    about_us.html render view.
    """
    return render(request, 'to_do_application/about_us.html')


@login_required
def get_user_profile_page(request, user_name: str):
    """
    user_profile.html render view.
    In POST method case the function proceed ProfileImageForm and send
    the data into 'to_do_application_usermodel' TABLE.
    Otherwise, form is unvalid or request.method == "GET" - renders user_profile.html.
    VARIABLES:
        - form: ProfileImageForm form ,
        - profile_user: User profile page owner ,
        - request_user: User who made the GET request to the server ,
        - amount_tasks_completed: Amount of completed tasks by 'profile_user' ,
        - amount_tasks: Total 'profile_user' tasks amount .
    """

    user = UserModel.objects.get(username=user_name)
    amount_tasks_completed = user.task_set.filter(is_completed=True).aggregate(Count('is_completed'))
    amount_tasks = user.task_set.aggregate(Count('id'))

    if request.method == "POST":
        form = ProfileImageForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            image = form.cleaned_data['profile_photo']
            user.profile_photo = image
            form.save()

    else:
        form = ProfileImageForm()
    return render(request, 'to_do_application/user_profile.html', context={
        'profile_user': user,
        'request_user': request.user,
        'form': form,
        'amount_tasks_completed': amount_tasks_completed['is_completed__count'],
        'amount_tasks': amount_tasks['id__count'],
    })


class UserLoginView(LoginView):
    """
    login.html render view.
    In POST method case the view class proceed UserLoginForm and validate
    the data in 'to_do_application_usermodel' TABLE.
    Otherwise, form is unvalid or request.method == "GET" - renders login.html.
    VARIABLES:
        - form: UserLoginForm form .
    """
    template_name = 'to_do_application/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('main_page')


@login_required
def logout_user(request):
    """
    logout.html render view.
    Does user log out after GET request method.
    """
    logout(request)
    return render(request, 'to_do_application/logout.html')


@login_required
def get_user_tasks_page(request, user_name: str = None, task_id: int = None):
    """
    tasks.html render view.
    If Function gets the 'task_id' parameter it processes the data and deletes
    task with given task_id argument from 'to_do_application_task' TABLE.
    Otherwise, task_id is None instance - View function renders html template
    without any data changing
    VARIABLES:
        - user: UserModel instance.
    """

    if task_id is not None:
        task = Task.objects.get(id=task_id)
        username = task.user.username
        task.delete()
        return HttpResponseRedirect(reverse('tasks', args=[username]))
    else:
        user = UserModel.objects.get(username=user_name)
    return render(request, 'to_do_application/tasks.html', context={
        'user': user,
    })


@login_required()
def create_new_task(request, user_name: str):
    """
    create_new_task.html render view.
    In POST method case the view class proceed UserTasksForm and creates new
    table instance in 'to_do_application_task' TABLE.
    Otherwise, form is unvalid or request.method == "GET" - renders create_new_task.html.
    VARIABLES:
        - form: UserTasksForm form .
    """
    if request.method == 'POST':
        form = UserTasksForm(request.POST)

        if form.is_valid():
            user = UserModel.objects.get(username=user_name)
            new_task = Task(is_public=form.cleaned_data['is_public'],
                            title=form.cleaned_data['title'],
                            description=form.cleaned_data['description'],
                            user=user)
            new_task.save()
            return HttpResponseRedirect(reverse('tasks', args=[user_name]))
    else:
        form = UserTasksForm()
    return render(request, 'to_do_application/create_new_task.html', context={
        'form': form,
    })


@login_required
def get_change_task_page(request, user_name: str, task_id: int):
    """
    change_task.html render view.
    In POST method case the view class proceed UserTasksForm and does data update
    query into 'to_do_application_task' TABLE.
    Otherwise, form is unvalid or request.method == "GET" - renders change_task.html.
    VARIABLES:
        - form: UserTasksForm form .
    """
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        form = UserTasksForm(request.POST)

        if form.is_valid():
            is_public = form.cleaned_data['is_public']
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']

            task.is_public = is_public
            task.title = title
            task.description = description
            task.save()
            return HttpResponseRedirect(reverse('tasks', args=[user_name]))

    else:
        form = UserTasksForm()
    return render(request, 'to_do_application/change_task.html', context={
        'form': form,
    })


@login_required
def get_completed_task(request, user_name: str, task_id: int):
    """
    is_completed_check_page.html OR tasks.html render view.
    In POST method case the view function changes task's 'is_completed' and 'is_public'
    fields update query into 'to_do_application_task' TABLE.
    Otherwise, form is unvalid or request.method == "GET" - renders is_completed_check_page.html.
    VARIABLES:
        - form: UserTasksForm form .
    """
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.is_completed = True
        task.is_public = False
        task.save()
        return HttpResponseRedirect(reverse('tasks', args=[user_name]))

    return render(request, 'to_do_application/is_completed_check_page.html', context={
        'the_task': task,
    })


def get_search_page(request):
    """
    search_people.html render view.
    In POST method case the view class process search-users Form field and does SELECT query
    into 'to_do_application_usermodel' TABLE.
    Otherwise, form is unvalid or request.method == "GET" - renders search_people.html.
    VARIABLES:
        - searched_value: the text entered by user in Search Form ,
        - users: Filtered users from UserModel model by 'username' or 'email' fields.
    """
    if request.method == 'POST':
        search = request.POST.get('search-users', "")
        users = UserModel.objects.filter(Q(username__contains=search) | Q(email__contains=search))
        return render(request, 'to_do_application/search_people.html', context={
            'searched_value': search,
            'users': users,
        })
    return render(request, 'to_do_application/search_people.html', context={})
