from django.forms import ModelForm
from tasksmanager.models import Task

class EditTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'status']
