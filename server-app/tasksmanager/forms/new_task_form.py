from django.forms import ModelForm
from tasksmanager.models import Task

class NewTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title']
