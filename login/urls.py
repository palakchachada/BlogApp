from django.urls import path
from .views import home,user_login,user_logout, signup_view , profile , add_blog , delete_blog
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('login/',user_login, name='login'),
    path('logout/',user_logout, name='logout'),
    path('signup/',signup_view, name='signup'),
    path('profile/', profile, name='profile'),
    path("blog/", add_blog, name="add-blog"),
    path('delete-blog/<int:id>/',delete_blog,name='delete-blog'),
    path("blogs_1/", blogs_1, name="blogs_1"),
    path("blogs_2/", blogs_2, name="blogs_2"),
    path("blogs_3/", blogs_3, name="blogs_3"),
    path("blogs_4/", blogs_4, name="blogs_4"),
    # path("blogs_5/", blogs_5, name="blogs_5"),
    # path("blogs_6/", blogs_6, name="blogs_6"),
]