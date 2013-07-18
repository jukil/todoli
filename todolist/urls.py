from django.conf.urls import patterns, url
from todolist.views import TodoListShow, todo_add, todo_done, todo_undo

urlpatterns = patterns('',
    url(r'^(?P<slug>[\w-]+)/$', TodoListShow.as_view(), name='todolist'),
    url(r'^(?P<slug>[\w-]+)/todo-add/$', todo_add, name='todo_add'), 
    url(r'^(?P<slug>[\w-]+)/todo-done/$', todo_done, name='todo_done'), 
    url(r'^(?P<slug>[\w-]+)/todo-undo/$', todo_undo, name='todo_undo'), 
)