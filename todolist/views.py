from django.views.generic import DetailView
from todolist.models import TodoList

class TodoList(DetailView):
    model = TodoList
    template_name = 'todolist/todolist.html'
    
    #context_object_name = 'todolist_entries'

    # http://stackoverflow.com/questions/11494483/django-class-based-view-how-do-i-pass-additional-parameters-to-the-as-view-meth
    #def get_object(self, queryset=None):
        #return queryset.get(todolist=self.todolist)
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(EntryList, self).get_context_data(**kwargs)
    #     # Add in the name of the todolist
    #     context['todolist_name'] = Entry.todolist
    #     return context