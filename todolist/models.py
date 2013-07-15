from django.db import models

class TodoList(models.Model):
    id = models.AutoField(primary_key=True)

    def __unicode__(self):
        return self.id

class Entry(models.Model):
    todolist = models.ForeignKey(TodoList)
    content = models.TextField()
    # Todo: Differentiate between done and not completed
    status = models.SmallPositiveIntegerField()

    def __unicode__(self):
        return self.content