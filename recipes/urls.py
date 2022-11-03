from . import views
from django.urls import path
from .views import AddRecipeView, EditRecipeView, DeleteRecipeView

urlpatterns = [
    path("recipes.html", views.RecipeList.as_view(), name="recipes"),
    path('search_recipes/', views.RecipeSearchView.as_view(), name='search_recipes'),
    path('add_recipe/', views.AddRecipeView.as_view(), name='add_recipe'),    
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_likes'),
    path('<slug:slug>/edit_recipe/', views.EditRecipeView.as_view(), name='edit_recipe'),
    path('<slug:slug>/delete_post/', views.DeleteRecipeView.as_view(), name='delete_recipe'),
]