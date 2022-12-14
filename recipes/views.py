from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe
from profiles .models import Profile
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic import UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import Q
from .forms import CommentForm
from .forms import RecipeForm
from django.urls import reverse_lazy


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by("-created_on")
    template_name = "recipes/recipes.html"
    paginate_by = 6


class RecipeDetail(View):
    """ Presents details of one recipe on recipe_detail Page """
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by
        profile = Profile.objects.filter(user=recipe.author)[0]
        ("-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipes/recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
                "profile": profile
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """ allows user to post comments on recipes """
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by
        ("-created_on")
        profile = Profile.objects.filter(user=recipe.author)[0]
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm(data=request.POST)
        msg = 'Your comment was sent successfully and is awaiting approval!'
        messages.add_message(self.request, messages.SUCCESS, msg)
        return render(
            request,
            "recipes/recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
                "profile": profile
            },
        )


class RecipeLike(View):
    """ allows user to like blog posts """
    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)
            msg = 'Your have liked this Recipe'
            messages.add_message(self.request, messages.SUCCESS, msg)
        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class AddRecipeView(generic.CreateView):
    model = Recipe
    template_name = "recipes/add_recipe.html"
    fields = ['category', 'title', 'featured_image', 'description',
              'difficulty', 'cooking_time', 'ingredients', 'method', 'status']
    success_url = reverse_lazy('recipes')

    def form_valid(self, form):
        """ Adding a new Recipe """
        """ adding the username automatically for the recipe """
        form.instance.author = self.request.user
        form.save()
        msg = 'Your Recipe has been added successfully'
        messages.add_message(self.request, messages.SUCCESS, msg)
        return super().form_valid(form)


class EditRecipeView(generic.UpdateView):
    model = Recipe
    template_name = "recipes/edit_recipe.html"
    fields = ['category', 'title', 'featured_image', 'description',
              'difficulty', 'cooking_time', 'ingredients', 'method', 'status']

    def get_success_url(self):
        """ Allows the Poster to edit their recipe and see the changes """
        slug = self.kwargs["slug"]
        msg = 'Your Recipe has been edited successfully'
        messages.add_message(self.request, messages.SUCCESS, msg)
        return reverse("recipes")


class DeleteRecipeView(SuccessMessageMixin, generic.DeleteView):
    model = Recipe
    template_name = "recipes/delete_recipe.html"
    success_url = reverse_lazy('recipes')
    success_message = 'Recipe was deleted successfully.'


class RecipeSearchView(generic.ListView):
    model = Recipe
    template_name = "recipes/recipes.html"
    context_object_name = "recipes"

    def get(self, request, *args, **kwargs):
        """ Allows the user to search through Recipes by category/title """
        query = self.request.GET.get('q')
        recipe_list = Recipe.objects.filter(
            Q(category__icontains=query) | Q(title__icontains=query)
        )

        context = {"recipe_list": recipe_list}

        return render(request, "recipes/recipes.html", context)
