from django.urls import path
from .views import pets_view, register_pet_view, api_animal, animal_detail


app_name = 'adopet'
urlpatterns = [
    path('', pets_view, name='pets_index'),
    path('register/', register_pet_view, name='pets_register'),
]
