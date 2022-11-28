from django.urls import path
from . import views
from .views import editProfile

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/edit_profile/', views.editProfile, name='editprofile')
]
