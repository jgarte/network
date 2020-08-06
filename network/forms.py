from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content', )
        widgets = {
            'content':
            forms.Textarea(attrs={
                'cols': 10,
                'rows': 2,
                'class': "form-control"
            })
        }
        error_messages = {
            'content': {
                'max_length':
                (f"The post is too long. Try to keep it under {Post.POST_LIMIT} characters."
                 ),
            }
        }
        # exclude = ['comments']
