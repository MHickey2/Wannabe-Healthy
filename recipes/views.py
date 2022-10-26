from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.shortcuts import render
from django.views import generic, View
from .models import Recipe
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.db.models import Q
from .forms import CommentForm
from django.urls import reverse_lazy


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by("-created_on")
    template_name = "recipe.html"
    paginate_by = 6


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        """ Presents the details of individual blog on PostDetail Page """
        queryset = Recipe.objects.filter(status=1)        
        recipe = get_object_or_404(queryset, slug=slug)
        # comments = post.comments.filter(approved=True).order_by("-created_on")
        # liked = False
        # if post.likes.filter(id=self.request.user.id).exists():
        #     liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                # "comments": comments,
                # "commented": False,
                # "liked": liked,
                # "comment_form": CommentForm()
            },
        )
        
    # def post(self, request, slug, *args, **kwargs):
    #     """ allows user to post comments on blogs """
    #     queryset = Recipe.objects.filter(status=1)
    #     recipe = get_object_or_404(queryset, slug=slug)
    #     comments = recipe.comments.filter(approved=True).order_by("-created_on")
    #     liked = False
    #     if recipe.likes.filter(id=self.request.user.id).exists():
    #         liked = True

    #     comment_form = CommentForm(data=request.POST)
    #     if comment_form.is_valid():
    #         comment_form.instance.email = request.user.email
    #         comment_form.instance.name = request.user.username
    #         comment = comment_form.save(commit=False)
    #         comment.post = post
    #         comment.save()
    #     else:
    #         comment_form = CommentForm()
    #     msg = 'You have left a comment successfully'
    #     messages.add_message(self.request, messages.SUCCESS, msg)
    #     return render(
    #         request,
    #         "recipe_detail.html",
    #         {
    #             "recipe": recipe,
    #             "comments": comments,
    #             "commented": True,
    #             "comment_form": comment_form,
    #             "liked": liked
    #         },
    #     )
