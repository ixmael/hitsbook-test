from django.forms import ModelForm
from tasksmanager.models import Task

class NewTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title']
        labels = {
            'title': 'Tarea',
        }
        help_texts = {
            'title': 'Ingresa la descripción de la tarea',
        }
        # attrs = {
        #     'title': {
        #         'placeholder': 'Escribir tarea',
        #     }
        # }
