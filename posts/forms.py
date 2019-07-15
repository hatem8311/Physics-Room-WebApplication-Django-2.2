from django import  forms
from .models import Posts,Comments

class post_create_form(forms.ModelForm):
    class Meta:
        model = Posts
        fields =['title','content']


class comments_to_post_form(forms.ModelForm):
    class Meta:
        model = Comments
        fields=['text']


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude=['']

