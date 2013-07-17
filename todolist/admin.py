from django.contrib import admin
from todolist.models import TodoList, Entry

class TodoListAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ('id',)

admin.site.register(TodoList, TodoListAdmin)
admin.site.register(Entry)