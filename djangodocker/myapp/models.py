from django.db import models

# class Student(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)

class todoList(models.Model):
    this_item = models.CharField(max_length=50)
    time = models.CharField(max_length=50)


