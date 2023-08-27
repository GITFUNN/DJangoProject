from django.urls import path, include
from login import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.publications_, name = 'home'),
    path('signup/', views.signup_page, name = 'signup'),
    path('logout/', views.signout, name = 'logout'),
    path('signin/', views.signin, name = 'signin'),
    path('main/', views.main_page, name='main'),
    path('create/', views.create_publication, name='create_publication'),
    #path('posts/', views.iterate_posts, name='posts'),
    path('<int:post_id>/', views.comments_page, name='comments'),
    path('home/', views.publications_, name='posts_'),
    path('comments/<int:publication_id>/', views.likes_publication, name = 'likes'),
    path('/comments/<int:comment_id>/', views.likes_comments, name = 'comments_likes'),
    path('nav/', views.nav, name = 'nav'),
    path('profile/', views.profile, name = 'profile'),

]   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)