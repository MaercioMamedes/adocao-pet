from django.urls import path
from .views import api_animal, animal_detail


# app_name = 'adopet'
urlpatterns = [
    path('pets/', api_animal),
    path('pets/<int:pk>', animal_detail ),
]