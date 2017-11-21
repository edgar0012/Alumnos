from django import forms

from .models import Pensun, Materia


class PensunForm(forms.ModelForm):
#todos los campos de Pelicula
   class Meta:
      model = Pensun
      fields = ('nombre', 'materias')
def __init__ (self, *args, **kwargs):
     super(PeliculaForm, self).__init__(*args, **kwargs)

     self.fields["materias"].widget = forms.widgets.CheckboxSelectMultiple()

     self.fields["materias."].help_text = "Ingrese las materias para el grado"

     self.fields["materias"].queryset = Materia.objects.all()
