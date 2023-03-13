from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from autenticazione.models import Profilo

class formDiRegistrazione(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(formDiRegistrazione, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class formProfilo(forms.ModelForm):
    
    class Meta:
        model = Profilo
        fields = ('citta','longitudine','latitudine')
    
    def __init__(self, *args, **kwargs):
        super(formProfilo, self).__init__(*args, **kwargs)

        self.fields['citta'].widget.attrs['class'] = 'form-control'
        self.fields['citta'].widget.attrs['id'] = 'citta'

        self.fields['longitudine'].widget.attrs['class'] = 'inputHidden'
        self.fields['latitudine'].widget.attrs['class'] = 'inputHidden'

        self.fields['longitudine'].widget.attrs['id'] = 'longitudine'
        self.fields['latitudine'].widget.attrs['id'] = 'latitudine'