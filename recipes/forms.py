from .models import Comment
from .models import Recipe
from django import forms


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
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Enter Title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }
