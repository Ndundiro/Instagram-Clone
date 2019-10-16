from django import forms

from .models import *


##############################################
# class CommentForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['text'].widget=forms.TextInput()
#         self.fields['text'].widget.attrs['placeholder']='Add a comment...'

#     class Meta:
#         model = Comment
#         fields = ('text',)