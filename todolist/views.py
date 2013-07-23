from django.views.generic import DetailView, TemplateView, RedirectView
from todolist.models import TodoList, Entry

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.template.defaultfilters import slugify

class IndexView(TemplateView):

    template_name = "todolist/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

class TodoListShow(DetailView):
    model = TodoList
    template_name = 'todolist/todolist.html'

def todo_add(request, slug):
    p = get_object_or_404(TodoList, slug=slug)
    new_todo = Entry(todolist=p, content=request.POST['content'], status=False)
    new_todo.save()
    
    return HttpResponseRedirect(reverse('todolists:todolist', args=(p.slug,)))

def todo_done(request, slug):
    todolist = get_object_or_404(TodoList, slug=slug)
    p = get_object_or_404(Entry, pk=int(request.POST['todo_pk']))
    p.status = True
    p.save()
    
    return HttpResponseRedirect(reverse('todolists:todolist', args=(todolist.slug,)))

def todo_undo(request, slug):
    todolist = get_object_or_404(TodoList, slug=slug)
    p = get_object_or_404(Entry, pk=int(request.POST['todo_pk']))
    p.status = False
    p.save()
    
    return HttpResponseRedirect(reverse('todolists:todolist', args=(todolist.slug,)))

def todolist_add(request):
    p = TodoList(name=request.POST['todolist_name'], slug=slugify(request.POST['todolist_name']))
    p.save()
    todolist = get_object_or_404(TodoList, name=request.POST['todolist_name'])
    return HttpResponseRedirect('/todolist/%s' % todolist.slug)