from . import views
from django.urls import path
from .views import AddRecipeView

urlpatterns = [
    path("recipes.html", views.RecipeList.as_view(), name="recipes"),
    path('add_recipe/', views.AddRecipeView.as_view(), name='add_recipe'),    
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_likes'),
]