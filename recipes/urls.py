from . import views
from django.urls import path

urlpatterns = [
    path("recipe.html", views.RecipeList.as_view(), name="recipes"),
]
