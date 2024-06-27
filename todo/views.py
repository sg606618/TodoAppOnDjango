from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from todo.models import Todo
from todo.forms import TodoForm


# Create your views here.
class TodoList(ListView):
    model = Todo
    # paginate_by = 10
    http_method_names = ['get', ]
    template_name = 'landing/index.html'
    context_object_name = 'todo'
    print(context_object_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class TodoCreate(CreateView, SuccessMessageMixin):
    model = Todo
    template_name = 'create.html'
    form_class = TodoForm
    success_url = reverse_lazy('todo:read')


class TodoUpdate(UpdateView, SuccessMessageMixin):
    model = Todo
    template_name = 'update.html'
    form_class = TodoForm
    success_url = reverse_lazy('todo:read')
    success_message = 'Todo added successfully'
    context_object_name = 'todo'


class TodoDelete(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo:read')

