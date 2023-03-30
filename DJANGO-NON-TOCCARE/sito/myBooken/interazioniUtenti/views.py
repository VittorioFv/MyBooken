from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.db.models import Q

from autenticazione.models import Profilo
from libri.models import Libri
from myBooken.settings import HTTP_URL

from .models import Chat, Scambi

import random


@login_required
def chatMain(request):
    chatId = Chat.objects.filter(Q(utente1 = request.user) | Q(utente2 = request.user)).order_by('data', 'tempo')[:10]

    uId = []
    for chat in chatId:
        if chat.utente1 == request.user:
            uId.append(chat.utente2)
        else:
            uId.append(chat.utente1)
    utenti = User.objects.filter(username__in = uId)

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
        while (a):
            codice = random.randint(0, 999999)
            try:
                scambio = Scambi.objects.get(codice=codice)
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


def scambiaTokenTra(richiedente, ricevente):
    profilo2 = Profilo.objects.get(user = richiedente)
    if profilo2.numTopen <= 0:
        return False
    profilo2.numTopen -= 1
    profilo2.save()
    
    profilo1 = Profilo.objects.get(user = ricevente)
    profilo1.numTopen += 1
    profilo1.save()
    
    return True

@login_required
def controllaCodiceScambio(request, codiceScambio):
    try:
        scambio = Scambi.objects.get(codice=codiceScambio)
        libro = Libri.objects.get(pk=scambio.libro.id)
        riceveneTetoken = User.objects.get(pk=libro.idUser.id)
        richiedenteTetoken = User.objects.get(username=scambio.idRichiedente)

        if riceveneTetoken == request.user:
            if (scambiaTokenTra(richiedenteTetoken, riceveneTetoken)):
                scambio.delete()
                libro.delete()
                try:
                    chat = Chat.objects.get(utente1=richiedenteTetoken, utente2=riceveneTetoken)
                except:
                    chat = Chat.objects.get(utente1=riceveneTetoken, utente2=richiedenteTetoken)
                
                chat.numeroScambi += 1
                chat.save()

                return render(request, 'confermaCodice.html')
            else:
                return render(request, 'nonHaiToken.html')
    except:
        return render(request, 'codiceErrato.html')

    return render(request, 'codiceErrato.html')
