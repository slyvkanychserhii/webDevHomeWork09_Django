from django.contrib import admin
from .models import Category, Task, SubTask


# Т.к. переопределенное поле 'title' модели 'Task' определяется
# последним, то и в форме админ-панели Django оно отображается последним. 
# Чтобы это исправить нужно определить и зарегистрировать 'TaskModelAdmin':
class TaskModelAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'status', 'deadline', 'categories']


admin.site.register(Category)
admin.site.register(Task, TaskModelAdmin)
admin.site.register(SubTask)
