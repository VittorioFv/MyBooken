from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from libri.forms import formAggiuntaLibri
from libri.forms import formModificaLibri
from .models import Libri

from django.contrib.auth.decorators import login_required

@login_required
def libri(request):
  mylibri = mylibri = Libri.objects.exclude( idUser = request.user.id)
  # values_list('titolo') solo per titolo
  # filter(titolo='prova').values()
  # filter(firstname__startswith='L').values()
  # order_by('-firstname').values()

  template = loader.get_template('esplora.html')
  context = {
    'mylibri': mylibri,
  }
  return HttpResponse(template.render(context, request))

@login_required
def dettagliLibro(request, id):
  mylibri = Libri.objects.get(id=id)
  template = loader.get_template('dettagliLibro.html')
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
    form = formAggiuntaLibri(request.POST)
    if form.is_valid():
      libro = form.save(commit=False)
      libro.idUser = request.user

      libro.save()

      return redirect('i_miei_libri')
  else:
    form = formAggiuntaLibri()
  return render(request, 'aggiuntaLibri.html', {
    'form': form,
  })

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