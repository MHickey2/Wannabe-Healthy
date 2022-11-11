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
    profile = get_object_or_404(Profile, user=request.user)    
    template = 'base.html'
    fields = ['profile_pic']
    context = {
        'profile': profile,
        'form': profile_form,
    }
    
    return render(request, template, context)
    

def editProfile(request):
    """ Display the user's profile. """
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



# class editProfile(generic.UpdateView):
#     model = Profile
#     template_name = "edit_profile.html"
#     fields = ['user', 'avatar', 'bio']

#     def get_success_url(self):
#         """ Allows the User to edit their profile and see the changes """
#         if request.method == 'POST':
#             form = ProfileForm(instance=profile)
#             if form.is_valid():
#                 form.save()
#             messages.success(request, 'Profile updated successfully')
#             # msg = 'Your Profile has been edited successfully'
#             # messages.add_message(self.request, messages.SUCCESS, msg)
#             return reverse("profile")
   
#             template = 'profiles/profile.html'
#             context = {
#                 'form': form
#             }

#         return render(request, template, context)

#     def get_object(self):
#         return self.request.user


    # class editProfile(generic.UpdateView):
    #     model = Profile
    #     template_name = "edit_profile.html"
    #     fields = ['user', 'bio', 'avatar']

    #     def get_success_url(self):
    #         """ Allows the Poster to edit their recipe and see the changes """
    #         slug = self.kwargs["slug"]
    #         msg = 'Your Profile has been edited successfully'
    #         messages.add_message(self.request, messages.SUCCESS, msg)
    #         return reverse("profile")
    