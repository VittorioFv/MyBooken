from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from libri.forms import formAggiuntaLibri
from libri.forms import formModificaLibri
from autenticazione.models import Profilo
from .models import Libri, Categorie

from django.db.models import Q

from django.contrib.auth.decorators import login_required

import geopy
import geopy.distance

@login_required
def libri(request):
  profilo = Profilo.objects.get(user = request.user.id)
  lon = 180 # a 180 c'è il salto
  lat = 90
  
  start = geopy.Point(lat, lon)
  d = geopy.distance.distance(kilometers = 10)

  print(start)
  print(d.destination(point=start, bearing=0).latitude) # 1km nord
  print(d.destination(point=start, bearing=180).latitude) # 1km sud

  print(d.destination(point=start, bearing=90).longitude) # 1km est
  print(d.destination(point=start, bearing=270).longitude) # 1km ovest

  mylibri = Libri.objects.exclude(idUser = request.user.id)
  if request.method == 'POST':
    testoDaCercare = request.POST.get('cercaLibri')
    mylibri = mylibri.filter(Q(titolo__icontains = testoDaCercare) | Q(descrizione__icontains = testoDaCercare) | Q(autore__icontains = testoDaCercare) | Q(isbn__icontains = testoDaCercare))
  
  return render(request, 'esplora.html', {
    'mylibri': mylibri,
  })

@login_required
def dettagliLibro(request, id):
  mylibri = Libri.objects.get(id=id)
  template = loader.get_template('dettagliLibro.html')
  context = {
    'mylibri': mylibri,
  }
  return HttpResponse(template.render(context, request))


@login_required
def mieiLibri(request):
  mylibri = Libri.objects.filter( idUser = request.user.id)
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
    form = formModificaLibri(request.POST, instance = libro)
    if form.is_valid():
      libro = form.save(commit=False)
      libro.save(update_fields=['titolo','autore','isbn','descrizione'])

      return redirect('libri')
  else:
    form = formModificaLibri(instance = libro)
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