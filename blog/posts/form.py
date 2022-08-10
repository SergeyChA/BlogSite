from django import forms
from .models import Posts, Comments


class PostsCreateForm(forms.ModelForm):
    title = forms.CharField(
        label='Заголовок' ,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control col-6'}))
    text = forms.CharField(
        label='Текст' ,
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control col-6'}))

    class Meta:
        model = Posts
        fields = ['title', 'text']

class CommentsCreateForm(forms.ModelForm):
    text = forms.CharField(
        label='Текст' ,
        required=True,
        help_text= '*не более 200 символов',
        widget=forms.Textarea(attrs={'class': 'form-control col-6'}))

    class Meta:
        model = Comments
        fields = ['text']
