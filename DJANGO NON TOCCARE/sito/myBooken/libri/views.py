from django.http import HttpResponse
from django.template import loader
from .models import Libri

def libri(request):
  mylibri = Libri.objects.all().values()
  # values_list('titolo') solo per titolo
  # filter(titolo='prova').values()
  # filter(firstname__startswith='L').values()
  # order_by('-firstname').values()

  template = loader.get_template('esplora.html')
  context = {
    'mylibri': mylibri,
  }
  return HttpResponse(template.render(context, request))

   
def dettagliLibro(request, id):
  mylibri = Libri.objects.get(id=id)
  template = loader.get_template('dettagliLibro.html')
  context = {
    'mylibri': mylibri,
  }
  return HttpResponse(template.render(context, request))