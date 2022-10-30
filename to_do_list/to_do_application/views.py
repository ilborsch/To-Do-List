from django.shortcuts import render, reverse
from .forms import UserRegistration
from .models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

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
            new_user = User(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            new_user.save()
            return HttpResponseRedirect(reverse('authorisation'))

    else:
        form = UserRegistration()
    return render(request, 'to_do_application/registration.html', context={
        'form': form,
    })


def get_authorisation_page(request):
    return render(request, 'to_do_application/authorisation.html')


def get_about_page(request):
    return render(request, 'to_do_application/about_us.html')


def get_user_profile_page(request, user_slug: str):
    return render(request, 'to_do_application/user_profile.html')