from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from tasksmanager.forms import NewTaskForm

class NewTaskView(FormView):
    template_name = "tasksmanager/new.html"
    form_class = NewTaskForm
    success_url = reverse_lazy('tasksmanager:home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
