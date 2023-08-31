from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Publication, Comment, Profile_image
from django import forms
from .forms import PublicationForm, CommentForm, Profile_imageForm, BackProfileForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse 
from django.contrib import messages
from django.utils import timezone
# Create your views here.
#@login_required
"""def nav (request):
    #form3 = PublicationForm()                     # if the request is POST then create a instance of the publication whit the request
    if request.method == 'POST':
        form3 = PublicationForm(request.POST)
        print("se renderizó correctamente el form")
        if form3.is_valid():  # validate if the form data is correct     
                publication = form3.save(commit = False) #the publication in publication variable
                publication.author = request.user # save the author of the publication like request.user
                publication.save_author()
                return redirect('profile')
    else:
        return render(request, 'nav.html', {
            'form3': PublicationForm,
            })
    return render(request,'nav.html', {
                    'form3': form3,
                    'error': 'error', 
                    })"""


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

"""@login_required
def create_publication(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():  # validate if the form data is correct
                publication = form.save(commit = False) #the publication in publication variable
                publication.author = request.user # save the author of the publication like request.user
                publication.save_author()
                return redirect('profile')  # redirect to a get page
            except IntegrityError:
                return render(request, 'create_publication.html', {
                    'form': PublicationForm()
                    })
        else:
            return render(request, 'create_publication.html', {
                    'form': PublicationForm(),
                    'error': "Integrity error"
                    })"""
            

                                            

@login_required
def publications_(request):
    publications = Publication.objects.all().order_by('-created_on')                                                # if the request is POST then create a instance of the publication whit the request
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():  # validate if the form data is correct     
            publication = form.save(commit = False) #the publication in publication variable
            publication.author = request.user # save the author of the publication like request.user
            publication.save_author()
            form = PublicationForm() 
        
    else:
        form = PublicationForm()

    #publications = Publication.objects.all().order_by('-created_on')
    return render (request, 'posts.html', {
        'publications': publications,
        'form': PublicationForm
        
        })



@login_required
def comments_page (request, post_id):
    publication = Publication.objects.get(id = post_id)
    comment = publication.comments.filter(active = True).order_by('-created_on') 
    form = CommentForm()

    if request.method == 'POST': 
        form = CommentForm(request.POST)
        if form.is_valid():
                new_form = form.save(commit= False)
                new_form.publication = publication
                new_form.comment_author = request.user
                new_form.created_on = timezone.now()
                try:
                    new_form.save()
                    new_form.active = True  # Intenta guardar el formulario
                    comment = publication.comments.filter(active=True).order_by('-created_on')
                    print("Guardado correctamente")
                    print(comment)
                    messages.error(request, form.errors)
                except Exception as e:
                    messages.error(request, form.errors)
                    print("Error al guardar el formulario:", str(e))
                return redirect(reverse('comments', args=[post_id]))
                    
        else: 
            messages.error(request, "error al guardar el formulario")
            
    print(comment)
    form = CommentForm()
    comment_url = (reverse('comments', args=[post_id]))
    return render (request, 'comments.html', {
        'publication': publication,
        'comments': comment,
        'form': form,
        'comment_url': comment_url,                                  
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



def likes_comments(request, comment_id):
    comment_ = Comment.objects.get(id = comment_id)
    is_like = False
    for like_ in comment_.likes_C.all():
        if like_ == request.user:
            is_like = True
            break
    if not is_like:
        comment_.likes_C.add(request.user)
    if is_like:
        comment_.likes_C.remove(request.user)
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)
        
@login_required
def profile(request):
    user = request.user
    comments = Comment.objects.filter(comment_author = user)
    comment_count = comments.count()
    publications = Publication.objects.filter(author=user)
    p_count = publications.count()
    num_likes = user.likes.all().count()
    back_img = get_object_or_404(Profile_image, user = user)
    img = get_object_or_404(Profile_image, user=user)
    try:
        back_img = Profile_image.objects.get(user = user)
        img = Profile_image.objects.get(user=user)
    except Profile_image.DoesNotExist:
        img = None
        back_img = None

    if request.method == 'POST':
        form1 = BackProfileForm(request.POST, request.FILES, instance = back_img)
        form = Profile_imageForm(request.POST, request.FILES, instance=img)
        if form.is_valid():
            profile_image = form.save(commit=False) 
            profile_image.user = user
            profile_image.save()
            form = Profile_imageForm(instance=img)
            print("Image saved successfully.")
        if form1.is_valid():
            back_profile_image = form1.save(commit=False)
            back_profile_image.user = user
            back_profile_image.save()
            form1 = BackProfileForm(instance=back_img)
                    
            print("Image saved successfully.")
    else:
        form1 = BackProfileForm(instance= back_img)
        form = Profile_imageForm(instance=img)
        print("Form is not valid:", form.errors)
    print("Image URL:", img.image.url if img.image else "No image")

    return render(request, 'profile.html', {
        'back_img': back_img,
        'img': img,
        'form1': form1,
        'form': form,
        'user': user,
        'publications': publications,
        'num_likes': num_likes,
        'p_count': p_count,
        'comment_count': comment_count,
    })





