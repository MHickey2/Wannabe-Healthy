from . import views
from django.urls import path
from .views import AddPostView, EditPostView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),   
    path('add_post/', views.AddPostView.as_view(), name='add_post'),    
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/edit_post/', views.EditPostView.as_view(), name='edit_post'),   
       
]
