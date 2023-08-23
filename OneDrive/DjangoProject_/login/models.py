from django.db import models
from django import forms
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Publication (models.Model):
    text_content = models.TextField(max_length=1000, default = None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    created_on = models.DateTimeField(default=datetime.now)
    likes = models.ManyToManyField(User, blank=True, related_name = 'likes')


    def formatted_created_on_(self):
        return self.created_on.strftime("%b. %d")
    

    def __str__(self):
        return f"Publication made by {self.author.username}"  # method that takes a username for the Publication Class
    
    def save_author(self, *args, **kwargs):
        if not self.author:
            self.author = kwargs.pop('author', None) # Si no se ha establecido un autor, lo establecemos como el usuario autenticado
        super().save(*args, **kwargs)


class Comment(models.Model):
    comment = models.CharField(max_length=500, default= None)
    comment_author = models.ForeignKey(User, on_delete= models.CASCADE, default = None)
    publication = models.ForeignKey(Publication, on_delete= models.CASCADE, related_name='comments')
    created_on = models.DateTimeField(default=datetime.now)
    active = models.BooleanField(default=True)
    likes_C = models.ManyToManyField(User, blank=True, related_name = 'likes_C')


    #def formatted_created_on(self):
        #return self.created_on.strftime("%b. %d")

    def __str__(self):
        return f"Publication made by {self.comment_author.username}"



    def save_comment_author(self, *args, **kwargs):
        if not self.comment_author:
            self.comment_author = kwargs.pop('comment_author', None)
        super().save(*args, **kwargs)

    
    def save(self, *args, **kwargs):
        # Establecer automáticamente active en True al crear un nuevo comentario.
        if not self.id:
            self.active = True
        super().save(*args, **kwargs)