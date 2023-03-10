from django.forms import ModelForm
from libri.models import Libri, Categorie 

from django import forms

class CategorieField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, categoria):
        return str(categoria.nomeCategoria)

class formAggiuntaLibri(ModelForm):
    
    class Meta:
        
        model = Libri
        fields = ('isbn','titolo','autore','descrizione','citta','immagine','longitudine','latitudine','categoria')

    categoria = CategorieField(
        queryset = Categorie.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )
    
    def __init__(self, *args, **kwargs):
        super(formAggiuntaLibri, self).__init__(*args, **kwargs)

        self.fields['isbn'].label = "ISBN"

        self.fields['isbn'].widget.attrs['class'] = 'form-control'
        self.fields['titolo'].widget.attrs['class'] = 'form-control'
        self.fields['autore'].widget.attrs['class'] = 'form-control'
        self.fields['descrizione'].widget.attrs['class'] = 'form-control'
        self.fields['citta'].widget.attrs['class'] = 'form-control'
        self.fields['citta'].widget.attrs['id'] = 'citta'
        self.fields['immagine'].required = False

        self.fields['longitudine'].widget.attrs['class'] = 'inputHidden'
        self.fields['latitudine'].widget.attrs['class'] = 'inputHidden'

        self.fields['longitudine'].widget.attrs['id'] = 'longitudine'
        self.fields['latitudine'].widget.attrs['id'] = 'latitudine'


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