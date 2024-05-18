from django.db import models
from django.contrib.auth.models import User # Importa el modelo User de Django para gestionar usuarios



class Task(models.Model):
    title = models.CharField(max_length=100) # Campo para el título de la tarea
    description = models.TextField() # Campo para la descripción de la tarea
    created_at = models.DateTimeField(auto_now_add=True) # Campo para la fecha de creación
    STATUS_CHOICES = (
        ('P', 'Pendiente'),
        ('C', 'Completado'),
    ) # Campo para el estado de la tarea
    status = models.CharField(max_length=1, choices=STATUS_CHOICES) # Campo para el estado de la tarea
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Campo para el usuario que crea la tarea

    # Método para mostrar el tiítulo de la tarea
    def __str__(self):
        return self.title 
     
    


