from django.urls import path
from . import views
from .views import editProfile

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('<slug:slug>/edit_profile/', views.editProfile.as_view(), name='editprofile')
    
]
