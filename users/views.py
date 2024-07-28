from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from django.db import transaction
from adopet.models import Tutor

# Create your views here.

@transaction.atomic
def register_user(request):
    if request.method == 'POST':
        user = get_user_model().objects.create(
            email=request.POST['email'],
            username=request.POST['username']
        )
        user.set_password(request.POST['password'])
        user.save()

        tutor = Tutor.objects.create(
            id_user_id = user.id,
            telefone = request.POST['phone'],
            whatsapp = request.POST['whatsapp'],
            cidade = request.POST['cidade'],
            estado = request.POST['estado']
        )
        tutor.save()

        messages.success(request, 'Usuário salvo com sucesso')

    return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user:
            login(request, user)
            return redirect('pets_index')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('users:login_user')