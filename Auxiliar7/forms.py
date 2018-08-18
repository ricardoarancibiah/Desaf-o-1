from django import forms
import models


class SeleccionTamanoForm(forms.Form):
def __init__(self, tamanoselecc, *args, **kwargs):
   	super(EditarTamanoForm, self).__init__(*args, **kwargs)
   	self.fields['idTamanos'] = forms.ModelChoiceField(label="Selecciona el tamano del tatuaje",
           	   empty_label="Selecciona Tamano", querset=Tamanos.objects.filter(tamanoselecc=tamanoselecc))

class SeleccionEstiloForm(forms.Form):
def __init__(self, estiloselecc, *args, **kwargs):
    super(EditarEstiloForm, self).__init__(*args, **kwargs)
    self.fields['idEstilo'] = forms.ModelChoiceField(label="Selecciona el estilo del tatuaje",
               empty_label="Selecciona un estilo" , querset=Tipo_Estilos.objects.filter(estiloselecc=estiloselecc))

class SeleccionCuerpoForm(forms.Form):
def __init__(self, cuerposelecc, *args, **kwargs):
    super(EditarCuerpoForm, self).__init__(*args, **kwargs)
    self.fields['idCuerpo'] = forms.ModelChoiceField(label="Selecciona la parte del cuerpo que quieres tatuar",
               empty_label="Seleccion una parte del cuerpo" , querset=Bands.objects.filter(cuerposelecc=cuerposelecc))






