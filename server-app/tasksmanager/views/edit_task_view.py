from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from tasksmanager.models import Task
from tasksmanager.forms import EditTaskForm

class EditTaskView(UpdateView):
    template_name = "tasksmanager/new.html"
    form_class = EditTaskForm
    model = Task
    success_url = reverse_lazy('tasksmanager:home')

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
