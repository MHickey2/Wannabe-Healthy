from django.shortcuts import render, get_object_or_404
from .models import Profile


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(Profile, user=request.user)    
    template = 'profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)


