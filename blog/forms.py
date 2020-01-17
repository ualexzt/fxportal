from django import forms

from blog.models import Post


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))

