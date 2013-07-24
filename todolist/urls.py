from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from todolist.views import TodoListShow, IndexView, todo_add, todo_done, todo_undo, todolist_add

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/todolists/')),
    url(r'^todolists/$', IndexView.as_view(), name='index'),
    url(r'^todolists/todolist-add/$', todolist_add, name='todolist_add'), 
    url(r'^todolists/(?P<slug>[\w-]+)/$', TodoListShow.as_view(), name='todolist'),
    url(r'^todolists/(?P<slug>[\w-]+)/todo-add/$', todo_add, name='todo_add'), 
    url(r'^todolists/(?P<slug>[\w-]+)/todo-done/$', todo_done, name='todo_done'), 
    url(r'^todolists/(?P<slug>[\w-]+)/todo-undo/$', todo_undo, name='todo_undo'), 
)