from django.urls import path
from .viewsets import create_user,get_profile,spam

urlpatterns=[
    path('create',create_user,name='create'),
    path('profile',get_profile,name='profile'),
    path('spam',spam,name='spam')
]