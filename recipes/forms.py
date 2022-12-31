from .models import Comment
from .models import Recipe
from django import forms
# from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('category', 'title', 'description', 'slug', 'difficulty',
                  'method', 'ingredients', 'featured_image', 'likes', 'status')

        widgets = {
            'method': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
        }

        def __init__(self, *args, **kwargs):
            super(RecipeForm, self).__init__(*args, **kwargs)

        # widgets = {
        #     'category': forms.TextInput(attrs={'class': 'form-control'}),
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'description': forms.TextInput(attrs={'class': 'form-control'}),
        #     'slug': forms.TextInput(attrs={'class': 'form-control'}),
        #     'difficulty': forms.TextInput(attrs={'class': 'form-control'}),
        #     'method': forms.TextInput(attrs={'class': 'form-control'}),
        #     'ingredients': forms.TextInput(attrs={'class': 'form-control'}),
        #     'status': forms.TextInput(attrs={'class': 'form-control'}),
        # }
