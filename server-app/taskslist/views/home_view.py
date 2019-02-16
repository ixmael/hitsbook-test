from django.views.generic import ListView

from tasksmanager.models import Task

class HomeView(ListView):
    model = Task
    template_name = "taskslist/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context
