from django.forms import ModelForm
from libri.models import Libri

class formAggiuntaLibri(ModelForm):
    
    class Meta:
        
        model = Libri
        fields = ('isbn','titolo','autore','descrizione','immagine',)
        

    def __init__(self, *args, **kwargs):
        super(formAggiuntaLibri, self).__init__(*args, **kwargs)

        self.fields['isbn'].widget.attrs['class'] = 'form-control'
        self.fields['titolo'].widget.attrs['class'] = 'form-control'
        self.fields['autore'].widget.attrs['class'] = 'form-control'
        self.fields['descrizione'].widget.attrs['class'] = 'form-control'
        self.fields['immagine'].required = False