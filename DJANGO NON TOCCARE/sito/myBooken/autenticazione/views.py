from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from .forms import formDiRegistrazione
# EMAIL VERIFICA
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

from .tokensAutenticazione import account_activation_token

def activateEmail(request, user, to_email):
    oggettoMail = " Attiva il tuo account di MyBooken"

    messaggio = render_to_string("attivaAccountMail.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http',
    })

    email = EmailMessage(oggettoMail, messaggio, to=[to_email])
    if email.send():
        pass
    else:
        messages.error(request, 'Non siamo riusciti a inviare la mail a {to_email}, controlla di averla scritta correttamente.')

def attivaUtente(request, uidb64, token):
    Utente = get_user_model()

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        utente = Utente.objects.get(pk=uid)
    except:
        utente = None
    
    if utente is not None and account_activation_token.check_token(utente, token):
        utente.is_active = True
        utente.save()

        messages.success(request, " Grazie per aver confermato la mail. or puoi accedere col tuo account")
        return redirect('login')
    else:    
        messages.error(request, " Il link di attivazione è invalido")
    
    return redirect('login')

def loginUtente(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('libri')
        else:
            messages.success(request, ("Errore: forse la password o l'username non sono corretti, ricordati di congfermare l'email se non lo hai fatto"))
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
            utente = form.save(commit = False)
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            # utente = authenticate(username = username, password = password) Proviene da un altro tutorial ma sembra inutile

            utente.is_active = False # utente "in pause" finche non conferma la mail
            utente.save()

            # activateEmail(request, utente, form.cleaned_data.get('email'))

            login(request, utente)

            return render(request, 'confermaMail.html', {'nome': utente.username})
    else:
        form = formDiRegistrazione()
    return render(request, 'registrazione.html', {
        'form': form,
    })