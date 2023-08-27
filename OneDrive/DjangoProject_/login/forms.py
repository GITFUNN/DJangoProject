
from django import forms
from .models import Comment, Publication, Profile_image
from django.forms import ImageField, FileInput
from django.forms.widgets import ClearableFileInput

class PublicationForm(forms.ModelForm): # Create a new CLASS that inherits 
    class Meta:
         model = Publication # Assign the publication class to this model
         fields = ['text_content'] #Assign the publication text content to this variable
# In general, the PublicationForm class inherits the methods from django.forms.ModelForm
# to make the creation of the publication more easy.
class CommentForm(forms.ModelForm): # Create a new CLASS that inherits from django.forms.ModelForm
     class Meta:
          model = Comment
          fields = ['comment', 'active']

     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs.update({'autocomplete': 'off'})



class CustomFileInput(forms.FileInput):
    clear_checkbox_label = None
    template_name = 'custom_file_input.html'



class Profile_imageForm(forms.ModelForm):
    class Meta:
        model = Profile_image
        fields = ['image']
        widgets = {
            'image': CustomFileInput(),
        }


class BackProfileForm(forms.ModelForm):
    class Meta:
        model = Profile_image
        fields = ['back_image']
        widgets = {
            'back_image': CustomFileInput(),
        }




