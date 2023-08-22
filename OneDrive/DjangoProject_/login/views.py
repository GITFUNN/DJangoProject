from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Publication, Comment
from django import forms
from .forms import PublicationForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.


def main_page(request):
    return render(request, 'main.html')


def home_page(request):
    return render(request, 'home.html')


def signup_page(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm

        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Register the user
            try:
                user = User.objects.create(
                username=request.POST['username'])
                user.set_password(request.POST['password1'])    
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'username already exists'})

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'password do not match'

        })


def signout(request):
    logout(request)
    return redirect('signin')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm

        })

    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or Password is incorrect'
            })
        else:
            login(request, user)
            return redirect('home')

@login_required
def create_publication(request):
    if request.method == 'GET':
        return render(request, 'create_publication.html', {
            'form': PublicationForm()
            })                                           # if the request is POST then create a instance of the publication whit the request
    elif request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():  # validate if the form data is correct
            try:      
                publication = form.save(commit = False) #the publication in publication variable
                publication.author = request.user # save the author of the publication like request.user
                publication.save_author() # save the publication using the save_author method from Publiaction Class. it have not parameters then the default parameter is the authenticated user.
            except IntegrityError:
                return render(request, 'create_publication.html', {
                    'form': PublicationForm()
                    })
        else:
            return render(request, 'create_publication.html', {
                    'form': PublicationForm(),
                    'error': "Integrity error"
                    })
        return redirect('main') # redirect to main page after publication has been saved

                                            

            
"""def iterate_posts(request):
    #Obtain the objets por the Publication class.
    publications = Publication.objects.all()
    
    #Create lists to save the publiactions objets
    text_content_list = []
    authors_list  = []
    ids = []

    #Iterate through the columns of the column text_content
    for i in publications:
        text_content_list.append(i.text_content)
        authors_list.append(i.author)
    
    authors_content = zip(text_content_list, authors_list)

    
    return render (request, 'show_posts.html', {
        'authors_content': authors_content,
        
    })"""


def publications_(request):
    publications = Publication.objects.all()

    return render (request, 'posts.html', {'publications': publications}) 

@login_required
def comments_page (request, post_id):
    publication = Publication.objects.get(id = post_id)
    comment = publication.comments.filter(active = True)
    form = CommentForm()

    if request.method == 'POST': 
        form = CommentForm(request.POST)
        if form.is_valid():
                new_form = form.save(commit= False)
                new_form.publication = publication
                new_form.comment_author = request.user
                new_form.save()
                return redirect(reverse('comments', args=[post_id]))
    else:
       
    
        form = CommentForm

    return render (request, 'comments.html', {
        'publication': publication,
        'comments': comment,
        'form': form,                                     
        })

@login_required  
def likes_publication(request, publication_id):
    publication = Publication.objects.get(id = publication_id)
    is_like = False
    for like in publication.likes.all():
        if like == request.user:
            is_like = True
            break
    if not is_like:
       publication.likes.add(request.user)
    if is_like:
        publication.likes.remove(request.user)
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)
