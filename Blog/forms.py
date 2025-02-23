from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'tag']  
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control w-100',
                }),
            'content': forms.Textarea(attrs={
                'rows': 3,
                'class': 'form-control w-100',
                }),
            'category': forms.Select(attrs={
                'class': 'form-control w-100',
                }),
            'tag': forms.SelectMultiple(attrs={
                'class': 'form-control w-100',
                }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'class': 'form-control w-100',
                }),
        }