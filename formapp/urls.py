from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('users/', views.fetch_users, name='fetch_users'), 
]
