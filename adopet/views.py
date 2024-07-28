from django.shortcuts import render, redirect
from django.http import HttpResponse
from adopet.models import Animal, Tutor
from adopet.forms import CreatePetForm
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes, renderer_classes
from .serializers import AnimalSerializer
from rest_framework import status

from rest_framework_xml.parsers import XMLParser
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer

# Create your views here.

def pets_view(request):
    animais = Animal.objects.all()
    return render(request, 'adopet/index.html', context={'animais': animais})

def register_pet_view(request):
    form = CreatePetForm()
    if request.method == 'POST':
        form = CreatePetForm(request.POST)
        if form.is_valid():
            tutor = Tutor.objects.get(id_user = request.user.id)
            animal = form.save(commit=False)
            animal.id_tutor_id = tutor.id
            animal.disponivel = 'disponivel'
            animal.save()
            return redirect('pets_index')

    return render(request, 'adopet/register.html', {'form': form})



@api_view(['GET', 'POST'])
# @renderer_classes(XMLRenderer)
# @parser_classes(XMLParser)
def api_animal(request):
    
    if request.method == "GET":

        animal = Animal.objects.all()
        serializer = AnimalSerializer(animal, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT','DELETE'])
def animal_detail(request, pk):
    try:
        animal = Animal.objects.get(pk=pk)
    except:
        return Response({'erro':'not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        animal_serializer = AnimalSerializer(animal)
        return Response(animal_serializer.data, status=status.HTTP_200_OK)

   
    elif request.method == 'PUT':
        animal_serializer = AnimalSerializer(animal, data=request.data)

        if animal_serializer.is_valid():
            animal_serializer.save()
            return Response(animal_serializer.data)
        
        return Response(animal_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        animal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


