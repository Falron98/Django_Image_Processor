from django import forms
from .models import Image

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'img_file']

class ImageDeleteForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['to_delete']