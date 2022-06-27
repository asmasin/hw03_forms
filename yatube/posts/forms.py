from django import forms
from django.contrib.auth import get_user_model
from posts.models import Post

User = get_user_model()


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            'text',
            'group',
        )
        help_text = {
            'text': 'Текст публикации',
            'group': 'Группа публикации',
        }
