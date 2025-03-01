
from django.urls import path
from django.views.generic import TemplateView
from formapp import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employee.urls')),
    path('', include('loginapp.urls')),
    
]
