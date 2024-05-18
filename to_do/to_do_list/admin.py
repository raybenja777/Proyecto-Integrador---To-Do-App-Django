from django.contrib import admin
from .models import Task # Importa el modelo Task del directorio actual

admin.site.register(Task) # Registra el modelo Task en el panel de administración de Django