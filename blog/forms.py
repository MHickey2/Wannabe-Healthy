from .models import Comment
from .models import Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('category', 'title', 'slug', 'featured_image', 'excerpt',  'content', 'status')
        
#         widgets = {
#             'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Category'}),
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'slug': forms.TextInput(attrs={'class': 'form-control'}),
#             'excerpt': forms.TextInput(attrs={'class': 'form-control'}),
#             'content': forms.TextInput(attrs={'class': 'form-control'}),
#             'status': forms.TextInput(attrs={'class': 'form-control'}),
#         }
