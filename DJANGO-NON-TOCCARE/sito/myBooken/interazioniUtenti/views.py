from django.shortcuts import render


def chatMain(request):  
  return render(request, 'chat.html', {})