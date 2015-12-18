from django.contrib import admin
from .models import Grupo
from .models import Usuario
from .models import Ruta
from .models import Evento

admin.site.register(Grupo)
admin.site.register(Usuario)
admin.site.register(Ruta)
admin.site.register(Evento)
# Register your models here.
