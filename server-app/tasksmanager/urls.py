from django.urls import path

from .views import HomeView, NewTaskView, EditTaskView, DeleteTaskView

urlpatterns = [
    path('tarea/<int:pk>/eliminar', DeleteTaskView.as_view(), name='delete'),
    path('tarea/<int:pk>', EditTaskView.as_view(), name='edit'),
    path('tarea', NewTaskView.as_view(), name='new'),
    path('', HomeView.as_view(), name='home'),
]

