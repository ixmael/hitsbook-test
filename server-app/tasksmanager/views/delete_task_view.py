from django.urls import reverse_lazy
from django.views.generic import DeleteView

from tasksmanager.models import Task

class DeleteTaskView(DeleteView):
    template_name = "tasksmanager/delete.html"
    model = Task
    success_url = reverse_lazy('tasksmanager:home')
