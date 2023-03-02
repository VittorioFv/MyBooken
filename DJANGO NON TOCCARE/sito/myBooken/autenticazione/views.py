from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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