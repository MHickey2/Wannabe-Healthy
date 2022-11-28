from . import views
from django.urls import path
from .views import AddPostView, EditPostView, DeletePostView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('search_blogs/', views.BlogSearchView.as_view(), name='search_blogs'),
    path('about.html/', views.about, name='about'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/edit_post/', views.EditPostView.as_view(),
         name='edit_post'),
    path('<slug:slug>/delete_post/', views.DeletePostView.as_view(),
         name='delete_post'),
]
