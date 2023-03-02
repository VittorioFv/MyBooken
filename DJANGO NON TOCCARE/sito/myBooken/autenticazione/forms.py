from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class formDiRegistrazione(UserCreationForm):
    email = forms.EmailField()#widget = forms.EmailInput(attrs = {'class':'form-coontrol'})) #per qualche motivo non funziona 

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(formDiRegistrazione, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'