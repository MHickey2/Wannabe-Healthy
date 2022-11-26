from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Profile
from django.views import generic, View
from django.views.generic import UpdateView
from django.contrib import messages
from .forms import ProfileForm
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(Profile, user=request.user)
    template = 'profile.html'
    fields = ['user', 'profile_pic', 'bio']
    context = {
        'profile': profile,
    }

    return render(request, template, context)


def profilePicDisplay(request):
    """ Display the user's profile pic on the base page. """
    profile = get_object_or_404(Profile, user=request.user)
    template = 'base.html'
    fields = ['profile_pic']
    context = {
        'profile': profile,
        'form': profile_form,
    }

    return render(request, template, context)


def editProfile(request):
    """ Allows the user to edit their profile. """
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
        messages.success(request, 'Profile updated successfully')
        return redirect('profile')

    else:
        profile_form = ProfileForm(instance=profile)

    template = 'edit_profile.html'

    context = {
       'profile': profile,
       'form': profile_form,
    }

    return render(request, template, context)
