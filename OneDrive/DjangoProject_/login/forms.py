from .models import Publication
from django import forms
from .models import Comment
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
     
