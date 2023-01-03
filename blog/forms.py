from .models import Comment
from .models import Post
from django import forms
from django.forms import ModelForm, TextInput
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'title', 'featured_image', 'excerpt',
                  'content', 'status')

        widgets = {
             'title': forms.TextInput(attrs={'placeholder': 'Enter your Title'}),  # noqa
             'excerpt': forms.TextInput(attrs={'placeholder': 'Enter a short Excerpt'}),  # noqa
             'content': SummernoteWidget(),
        }

        def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)
