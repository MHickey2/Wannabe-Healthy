from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Post
from .forms import CommentForm
# from .forms import PostForm
from django.urls import reverse_lazy


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class AddPostView(generic.CreateView):
    model = Post
    template_name = "add_post.html"
    fields = ['category', 'title', 'slug', 'featured_image', 'excerpt',  'content', 'status']
    success_url = '/'

    def form_valid(self, form):
        """ adding the username automatically for the post """
        form.instance.author = self.request.user        
        form.save()
        return super().form_valid(form)


class EditPostView(generic.UpdateView):
    model = Post
    template_name = "edit_post.html"
    fields = ['category', 'title', 'featured_image', 'excerpt',  'content', 'status']
    
    def get_success_url(self):
        slug = self.kwargs["slug"]
        return reverse("post_detail", kwargs={"slug": slug})
    

class DeletePostView(generic.DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')