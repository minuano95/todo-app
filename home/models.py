import email
from pyexpat import model
from tkinter import CASCADE
from django.db import models

# Create your models here.

# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=30, null=False)
#     last_name = models.CharField(max_length=30, null=False)
#     age = models.IntegerField(null=False)
#     email = models.EmailField(null=False)
#     password = models.CharField(max_length=16, null=False)

#     def __str__(self):
#         return str(self.first_name + ' ' + self.last_name)

class Task(models.Model):
    task_id = models.AutoField(primary_key=True, editable=False)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=30, null=False, verbose_name='title')
    task_description = models.CharField(max_length=100, null=False, verbose_name='description')
    task_date = models.DateTimeField(verbose_name='date')
    task_status = models.BooleanField(default=False, editable=False)


    def __str__(self):
        return str(self.task_id)

class CompletedTask(models.Model):
    completed_task_id = models.IntegerField(null=False, editable=False)
    task_completed_at = models.DateField(auto_now=True, editable=False)
    task_status = models.BooleanField(default=True, editable=False)
    
    def __str__(self):
        return str(self.completed_task_id)