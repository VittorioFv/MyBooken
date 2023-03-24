from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from libri.forms import formAggiuntaLibri
from libri.forms import formModificaLibri
from autenticazione.models import Profilo, Recensioni
from interazioniUtenti.models import Chat
from .models import Libri
from django.contrib.auth.models import User

from datetime import datetime

from django.db.models import Q

from django.contrib.auth.decorators import login_required

import geopy
import geopy.distance


def getArea(lon, lat, kilometri):
    start = geopy.Point(lat, lon)
    d = geopy.distance.distance(kilometers=kilometri)

    latm = d.destination(point=start, bearing=0).latitude
    latM = d.destination(point=start, bearing=180).latitude
    if latM < latm:
        t = latM
        latM = latm
        latm = t

    lonm = d.destination(point=start, bearing=90).longitude
    lonM = d.destination(point=start, bearing=270).longitude
    if lonM < lonm:
        t = lonM
        lonM = lonm
        lonm = t

    return ((lonm, lonM), (latm, latM))


@login_required
def contattaAutore(request, username):
    utente1 = User.objects.get(username=request.user.username)
    utente2 = User.objects.get(username=username)

    try:
        chat = Chat.objects.get(
            utente1=utente1, utente2=utente2)
    except:
        try:
          chat = Chat.objects.get(utente1=utente2,
                                utente2=utente1)
        except:
          chat = Chat(utente1=utente1, utente2=utente2, numeroScambi = 0)
          chat.tempo = datetime.now()
          chat.save()
    
    return redirect('chat_main')

@login_required
def libri(request):
    profilo = Profilo.objects.get(user=request.user.id)
    lon = profilo.longitudine
    lat = profilo.latitudine
    ((lonm, lonM), (latm, latM)) = getArea(lon=lon, lat=lat, kilometri=10)

    print(lonm, lonM, latm, latM)

    mylibri = Libri.objects.filter(
        longitudine__gt=lonm, longitudine__lt=lonM, latitudine__gt=latm, latitudine__lt=latM)
    mylibri = mylibri.exclude(idUser=request.user.id)
    if request.method == 'POST':
        testoDaCercare = request.POST.get('cercaLibri')
        mylibri = mylibri.filter(Q(titolo__icontains=testoDaCercare) | Q(descrizione__icontains=testoDaCercare) | Q(
            autore__icontains=testoDaCercare) | Q(isbn__icontains=testoDaCercare))

    mylibri = mylibri[:10]

    return render(request, 'esplora.html', {
        'mylibri': mylibri,
    })


@login_required
def dettagliLibro(request, id):
    libro = Libri.objects.get(id=id)
    # utente = User.objects.get(username = libro.idUser)
    profilo = Profilo.objects.get(user=libro.idUser)
    recensioni = Recensioni.objects.filter(idUser=libro.idUser)

    template = loader.get_template('dettagliLibro.html')
    context = {
        'mylibri': libro,
        'usernameUtente': libro.idUser,
        'profilo': profilo,
        'recensioni': recensioni,
    }
    return HttpResponse(template.render(context, request))


@login_required
def mieiLibri(request):
    mylibri = Libri.objects.filter(idUser=request.user.id)
    # values_list('titolo') solo per titolo
    # filter(titolo='prova').values()
    # filter(firstname__startswith='L').values()
    # order_by('-firstname').values()

    template = loader.get_template('iMieiLibri.html')
    context = {
        'mylibri': mylibri,
    }
    return HttpResponse(template.render(context, request))


@login_required
def modificaLibro(request, id):
    libro = Libri.objects.get(pk=id)
    if libro.idUser != request.user:
        return redirect('i_miei_libri')
    if request.method == 'POST':
        form = formModificaLibri(request.POST, instance=libro)
        if form.is_valid():
            libro = form.save(commit=False)
            libro.save(update_fields=[
                       'titolo', 'autore', 'isbn', 'descrizione'])

            return redirect('libri')
    else:
        form = formModificaLibri(instance=libro)
    return render(request, 'modificaLibro.html', {
        'form': form,
        'id': id,
    })


@login_required
def aggiungiLibro(request):
    if request.method == 'POST':
        form = formAggiuntaLibri(request.POST, request.FILES)
        if form.is_valid():
            libro = form.save(commit=False)

            libro.idUser = request.user

            libro.save()

            form.save_m2m()

            return redirect('i_miei_libri')
    else:
        form = formAggiuntaLibri()
    return render(request, 'aggiuntaLibri.html', {
        'form': form,
    })


@login_required
def eliminaLibro(request, id):
    libro = Libri.objects.get(pk=id)
    libro.delete()

    return redirect('i_miei_libri')
