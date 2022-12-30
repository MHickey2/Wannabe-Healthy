from .models import Comment
from .models import Post
from django import forms
from django.forms import ModelForm, TextInput
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'title', 'slug', 'featured_image', 'excerpt',
                  'content', 'status')

        widgets = {
            'content': SummernoteWidget(),
        }

        def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)
        # widgets = {
        #     'category': forms.TextInput(attrs={'class': 'form-control'}),
        #     'title': TextInput(attrs={'class': 'form-control'}),
        #     'slug': forms.TextInput(attrs={'class': 'form-control'}),
        #     'excerpt': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.TextInput(attrs={'class': 'form-control'}),
        #     'status': forms.TextInput(attrs={'class': 'form-control'}),
        # }
