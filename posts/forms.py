from django import forms
from .models import Post, Comment

class PostCreation(forms.ModelForm):
    tags = forms.CharField(label='tags (seperated by comma)', help_text='example: (tag1,tag2,tag3, etc..)',widget=forms.TextInput(attrs={'class': 'input is-medium'}))
    # tags_titles = forms.CharField(label='tags (seperated by comma)',widget=forms.TextInput(attrs={'class': 'input is-medium'}))
    class Meta:
        model = Post
        fields=['picture','question_text','content','tags']
class CommentCreation(forms.ModelForm):
    comment = forms.CharField(max_length=90, label='add comment',widget=forms.TextInput(attrs={'class': 'input is-medium'}))
    class Meta:
        model = Comment
        fields = ['comment']