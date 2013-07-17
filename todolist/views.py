from django.views.generic import DetailView
from todolist.models import TodoList

class TodoList(DetailView):
    model = TodoList
    template_name = 'todolist/todolist.html'