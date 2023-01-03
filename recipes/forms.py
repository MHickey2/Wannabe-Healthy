from .models import Comment
from .models import Recipe
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('category', 'title', 'featured_image', 'description', 'difficulty',  # noqa
                  'ingredients', 'method', 'status')

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter your Title'}),  # noqa
            'description': forms.TextInput(attrs={'placeholder': 'Enter a short Description'}),  # noqa
            'method': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
        }

        def __init__(self, *args, **kwargs):
            super(RecipeForm, self).__init__(*args, **kwargs)
