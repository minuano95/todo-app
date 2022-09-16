from django.contrib import admin
from .models import Task, CompletedTask

# Register your models here.

admin.site.register(CompletedTask)
admin.site.register(Task)
