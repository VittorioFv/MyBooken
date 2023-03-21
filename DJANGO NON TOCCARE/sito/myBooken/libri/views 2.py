from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from libri.forms import formAggiuntaLibri
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
def aggiungiLibro(request):
  if request.method == 'POST' and request.user.is_authenticated:
    form = formAggiuntaLibri(request.POST, files=request.FILES)
    if form.is_valid():
      libro = form.save(commit=False)
      libro.idUser = request.user
      libro.save()

      return redirect('libri')
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