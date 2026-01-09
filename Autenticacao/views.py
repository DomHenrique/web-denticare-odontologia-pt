from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.db import OperationalError
# Create your views here.

class RegistroView(View):
    def get(self,request):
        try:
            form=UserCreationForm()
            return render(request, 'registro/registro.html', {'form':form})
        except OperationalError:
            return render(request, 'registro/registro.html', {'form': None, 'db_error': True})

    def post(self, request):
        try:
            form=UserCreationForm(request.POST)

            if form.is_valid():
                usuario = form.save()
                login(request, usuario)
                return redirect('inicio')
            
            else:
                for msg in form.error_messages:
                    messages.error(request, form.error_messages[msg])

                return render(request, 'registro/registro.html', {'form':form})
        except OperationalError:
            return render(request, 'registro/registro.html', {'form': None, 'db_error': True})


def fazer_logout(request):
    try:
        logout(request)
    except OperationalError:
        pass

    return redirect('inicio')


def fazer_login(request):
    try:
        if request.method == 'POST':
            form=AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                nome_usuario = form.cleaned_data.get('username')
                senha = form.cleaned_data.get('password')
                usuario = authenticate(username = nome_usuario, password = senha)
                if usuario is not None:
                    login(request, usuario)
                    return redirect('inicio')
                else:
                    messages.error(request, 'Usuario invalido')
        
        form = AuthenticationForm()
        return render(request, 'login/login.html', {'form':form})
    except OperationalError:
        return render(request, 'login/login.html', {'form': None, 'db_error': True})