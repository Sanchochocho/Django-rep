from django.urls import path
from .views import post_list, post, create_post

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<id>', post, name='post'),
    path('create_post', create_post, name='create_post')
]
