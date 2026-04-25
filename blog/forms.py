from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class': 'w-full border border-black rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500'
        })

        self.fields['content'].widget.attrs.update({
            'class': 'w-full border border-black rounded-lg px-4 py-2 h-40 resize-none focus:outline-none focus:ring-2 focus:ring-blue-500'
        })