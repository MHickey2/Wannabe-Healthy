from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.translation import gettext
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic import DeleteView
from django.contrib import messages
from django.db.models import Q
from .models import Post
from profiles .models import Profile
from .forms import CommentForm
from .forms import PostForm
from django.urls import reverse_lazy


# def my_view(request):
#     output = gettext("Welcome to my site.")
#     return HttpResponse(output)


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        """ Presents the details of individual blog on PostDetail Page """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        profile = Profile.objects.filter(user=post.author)[0]
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
                "profile": profile
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """ allows user to post comments on blogs """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        profile = Profile.objects.filter(user=post.author)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()
        msg = 'Your comment was added successfully and is awaiting approval!'
        messages.add_message(self.request, messages.SUCCESS, msg)
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
                "profile": profile

            },
        )


class PostLike(View):
    """ allows user to like blog posts """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            msg = 'Your have unliked this Post'
            messages.add_message(self.request, messages.SUCCESS, msg)
        else:
            post.likes.add(request.user)
            msg = 'Your have liked this Post'
            messages.add_message(self.request, messages.SUCCESS, msg)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class AddPostView(generic.CreateView):
    model = Post
    template_name = "blog/add_post.html"
    fields = ['category', 'title', 'slug', 'featured_image', 'excerpt',
              'content', 'status']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """ Ensures form valid and new inputs are saved"""
        """ adding the username automatically for the post """
        form.instance.author = self.request.user
        form.save()
        msg = 'Your Post has been created successfully'
        messages.add_message(self.request, messages.SUCCESS, msg)
        return super().form_valid(form)


def about(request):
    """ A view to return the about page """
    return render(request, 'about.html', {})


class EditPostView(generic.UpdateView):
    model = Post
    template_name = "blog/edit_post.html"
    fields = ['category', 'title', 'featured_image', 'excerpt',  'content',
              'status']

    def get_success_url(self):
        """ Allows the Poster to edit their blog and see the changes """
        slug = self.kwargs["slug"]
        msg = 'Your Post has been edited successfully'
        messages.add_message(self.request, messages.SUCCESS, msg)
        return reverse("home")


class DeletePostView(generic.DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy('home')


class BlogSearchView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"

    def get(self, request, *args, **kwargs):
        """ allows user to search through blogs by category/title """

        query = self.request.GET.get('q')
        post_list = Post.objects.filter(
            Q(category__icontains=query) | Q(title__icontains=query)
        )

        context = {"post_list": post_list}

        return render(request, "blog/index.html", context)
