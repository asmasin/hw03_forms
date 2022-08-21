from django import forms
from posts.models import Post


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
