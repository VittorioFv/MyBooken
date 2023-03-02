from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import formDiRegistrazione

def loginUtente(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('libri')
        else:
            messages.success(request, ("Errore: forse la password o l'username non sono corretti"))
            return redirect('login')
    else:
        return render(request, 'login.html')

def logoutUtente(request):
    logout(request)
    return render(request, 'login.html')

def registrazioneUtente(request):
    if request.method == 'POST':
        form = formDiRegistrazione(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            utente = authenticate(username = username, password = password)
            login(request, utente)

            messages.success(request, (" Sei stato registrato correttamente"))
            return redirect('libri')
    else:
        form = formDiRegistrazione()
    return render(request, 'registrazione.html', {
        'form': form,
    })