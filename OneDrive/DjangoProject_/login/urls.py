from django.urls import path, include
from login import views

urlpatterns = [
    path('', views.publications_, name = 'home'),
    path('signup/', views.signup_page, name = 'signup'),
    path('logout/', views.signout, name = 'logout'),
    path('signin/', views.signin, name = 'signin'),
    path('main/', views.main_page, name='main'),
    path('create/', views.create_publication, name='create_publication'),
    #path('posts/', views.iterate_posts, name='posts'),
    path('<int:post_id>', views.comments_page, name='comments'),
    path('home/', views.publications_, name='posts_'),
    path('comments/<int:publication_id>/', views.likes_publication, name = 'likes'),
    path('/comments/<int:comment_id>/', views.likes_comments, name = 'comments_likes'),

]   