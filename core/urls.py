"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from adopet.views import pets_view, register_pet_view, api_animal, animal_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('pets/', pets_view, name='pets_index'),
    path('api/pets/', api_animal),
    path('api/pets/<int:pk>', animal_detail ),
    path('pets/register', register_pet_view, name='pets_register'),
]
