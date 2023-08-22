from django.db import models
from django import forms
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Publication (models.Model):
    text_content = models.TextField(max_length=200, default = None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    created_on = models.DateTimeField(default=datetime.now)


    def formatted_created_on_(self):
        return self.created_on.strftime("%b. %d")
    

    def __str__(self):
        return f"Publication made by {self.author.username}"  # method that takes a username for the Publication Class
    
    def save_author(self, *args, **kwargs):
        if not self.author:
            self.author = kwargs.pop('author', None) # Si no se ha establecido un autor, lo establecemos como el usuario autenticado
        super().save(*args, **kwargs)


class Comment(models.Model):
    comment = models.CharField(max_length=225, default= None)
    comment_author = models.ForeignKey(User, on_delete= models.CASCADE, default = None)
    publication = models.ForeignKey(Publication, on_delete= models.CASCADE, related_name='comments')
    created_on = models.DateTimeField(default=datetime.now)
    active = models.BooleanField(default=True)

    def formatted_created_on(self):
        return self.created_on.strftime("%b. %d")

    def __str__(self):
        return f"Publication made by {self.comment_author.username}"



    def save_comment_author(self, *args, **kwargs):
        if not self.comment_author:
            self.comment_author = kwargs.pop('comment_author', None)
        super().save(*args, **kwargs)
