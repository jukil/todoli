from django.db import models

class TodoList(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Entry(models.Model):
    todolist = models.ForeignKey(TodoList)
    content = models.TextField()
    # Todo: Differentiate between done and not completed
    status = models.BooleanField()

    def __unicode__(self):
        return self.content

class Comment(models.Model):
    entry = models.ForeignKey(Entry)
    content = models.TextField()

    def __unicode__(self):
        return self.content