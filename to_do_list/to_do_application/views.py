from django.contrib.auth import authenticate, login, logout
from .models import UserModel, Task
from django.contrib.auth.views import LoginView
from django.shortcuts import render, reverse
from .forms import UserRegistration, UserLoginForm, UserTasksForm, ProfileImageForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy

# Create your views here.
main_page_text = ['Play and become better - Complete the planned tasks and gain the highest level!',
                  'Be more successful than others.',
                  'Or be more successful together.',
                  'Your choice - your career.', ]


def get_welcome_page(request):
    return render(request, 'to_do_application/main_page.html', context={
        'points': main_page_text,
    })


def get_registration_page(request):
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
    return render(request, 'to_do_application/about_us.html')


def get_user_profile_page(request, user_name: str):
    user = UserModel.objects.get(username=user_name)
    if request.method == "POST":
        form = ProfileImageForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            image = form.cleaned_data['profile_photo']
            user.profile_photo = image
            form.save()

    else:
        form = ProfileImageForm()
    return render(request, 'to_do_application/user_profile.html', context={
        'user': user,
        'form': form,
    })


class UserLoginView(LoginView):
    template_name = 'to_do_application/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('main_page')


def logout_user(request):
    logout(request)
    return render(request, 'to_do_application/logout.html')


def get_user_tasks_page(request, user_name: str = None, task_id: int = None):
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


def create_new_task(request, user_name: str):
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







#def get_login_page(request):
   # if request.method == "POST":
      #  form = UserLogin(request.POST)
     #   if form.is_valid():
           # cd = form.cleaned_data
          #  user = authenticate(username=cd['username'], password=cd['password'])
         #   if user is not None:
        #        if user.is_active:
       #             login(request, user)
      #              return HttpResponse('Authenticated successfully')
     #           else:
    #                return HttpResponse('Disabled Account')
   #         else:
  #              return HttpResponse('Invalid login')
 #   else:
 #       form = UserLogin()
#    return render(request, 'to_do_application/login.html', context={
#        'form': form,
#    })