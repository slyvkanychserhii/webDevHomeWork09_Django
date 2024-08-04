from django.contrib import admin
from .models import Category, Task, SubTask


class TaskModelAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'status', 'deadline', 'categories']


admin.site.register(Category)
admin.site.register(Task, TaskModelAdmin)
admin.site.register(SubTask)
