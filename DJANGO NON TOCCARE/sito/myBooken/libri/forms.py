from django.forms import ModelForm
from libri.models import Libri

class formAggiuntaLibri(ModelForm):
    
    class Meta:
        
        model = Libri
        fields = ('isbn','titolo','autore','descrizione','citta','immagine',)
        

    def __init__(self, *args, **kwargs):
        super(formAggiuntaLibri, self).__init__(*args, **kwargs)

        self.fields['isbn'].widget.attrs['class'] = 'form-control'
        self.fields['titolo'].widget.attrs['class'] = 'form-control'
        self.fields['autore'].widget.attrs['class'] = 'form-control'
        self.fields['descrizione'].widget.attrs['class'] = 'form-control'
        self.fields['citta'].widget.attrs['class'] = 'form-control'
        self.fields['citta'].widget.attrs['id'] = 'citta'
        self.fields['immagine'].required = False


class formModificaLibri(ModelForm):
    
    class Meta:
        model = Libri
        fields = ('isbn','titolo','autore','descrizione')
        

    def __init__(self, *args, **kwargs):
        super(formModificaLibri, self).__init__(*args, **kwargs)

        self.fields['isbn'].widget.attrs['class'] = 'form-control'
        self.fields['titolo'].widget.attrs['class'] = 'form-control'
        self.fields['autore'].widget.attrs['class'] = 'form-control'
        self.fields['descrizione'].widget.attrs['class'] = 'form-control'