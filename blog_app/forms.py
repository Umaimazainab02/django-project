from django import forms
from .models import Add_Blog

class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Add_Blog
        fields = ["title", "image"]