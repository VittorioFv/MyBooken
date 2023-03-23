from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.db.models import Q

from libri.models import Libri
from myBooken.settings import HTTP_URL

from .models import Chat, Scambi

import random


@login_required
def chatMain(request):
    utentiId = Chat.objects.values('utente2').filter(utente1=request.user)
    utentiId2 = Chat.objects.values('utente1').filter(utente2=request.user)
    utenti = User.objects.filter(Q(pk__in=utentiId) | Q(pk__in=utentiId2))

    return render(request, 'chat.html', {'utenti': utenti})


@login_required
def scegliLibro(request, username):

    user = User.objects.get(username=username)

    mylibri = Libri.objects.filter(idUser=user.id)

    return render(request, 'scambiaLibro.html',  {
        'mylibri': mylibri,
    })


@login_required
def generaCodice(request, id):
    libro = Libri.objects.get(pk=id)

    try:
        scambio = Scambi.objects.get(libro=libro, idRichiedente=request.user)
    except Scambi.DoesNotExist:
        scambio = None

    if not scambio:
        a = True
        while(a):
            codice = random.randint(0, 999999)
            try:
                scambio = Scambi.objects.get(codice = codice)
            except:
                a = False
        scambio = Scambi(
            libro=libro, idRichiedente=request.user, codice=codice)
        scambio.save()
    else:
        codice = scambio.codice
    
    linkCodice = HTTP_URL + "codice/" + str(codice) + "/" 
    
    return render(request, 'codiceScambio.html',  {
        'link': linkCodice,
        'codice': codice,
    })


@login_required
def controllaCodiceScambio(request, codiceScambio):
    try:
      scambio = Scambi.objects.get(codice=codiceScambio)
      libro = Libri.objects.get(pk = scambio.libro.id)
      user =  User.objects.get(pk = libro.idUser.id)
      if user == request.user:
          return render(request, 'confermaCodice.html')
    except:
        return render(request, 'codiceErrato.html')
    
    return render(request, 'codiceErrato.html')