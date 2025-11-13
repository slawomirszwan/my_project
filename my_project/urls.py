"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from django.views.generic import RedirectView

#------
from django.http import HttpResponse

def index(request):
    return HttpResponse("index response")
#-------

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),

    #path('', RedirectView.as_view(pattern_name='home', permanent=False)),
    #path('home/', include('apps.hardware.urls')),
    #path('hardware/', include('apps.hardware.urls')),
    #path('software/', include('apps.software.urls')),


    #dodanie wskazania na urls z aplikacji hardware
    path('hardware/', include('hardware.urls'))
]
