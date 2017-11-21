from django.contrib import admin
from pensun.models import Materia, MateriaAdmin, Pensun, PensunAdmin


admin.site.register(Materia, MateriaAdmin)
admin.site.register(Pensun, PensunAdmin)

# Register your models here.
