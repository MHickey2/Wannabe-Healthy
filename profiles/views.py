from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Profile
from django.views import generic, View
from django.views.generic import UpdateView


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(Profile, user=request.user)    
    template = 'profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)


class editProfile(generic.UpdateView):
    model = Profile
    template_name = "edit_profile.html"
    fields = ['user', 'avatar', 'bio']

    def get_success_url(self):
        """ Allows the User to edit their profile and see the changes """
        slug = self.kwargs["slug"]
        msg = 'Your Profile has been edited successfully'
        messages.add_message(self.request, messages.SUCCESS, msg)
        return reverse("profile")
