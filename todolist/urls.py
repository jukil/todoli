from django.conf.urls import patterns, url
from todolist.views import TodoList

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', TodoList.as_view(), name='todolist'),
    )