from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Userprofile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    address = models.CharField(max_length = 200, null = True, blank = True)

    def __str__(self):
        return str(self.user)
        

class Todolist(models.Model):
    PRIORITY = [
        ('high', 'high'),
        ('normal', 'normal')

    ]
    name = models.ForeignKey(Userprofile, on_delete = models.SET_NULL,  null = True)
    title = models.CharField(max_length = 200, null = True)
    description = models.TextField(null = True, blank = True)
    priority = models.CharField(max_length = 200,null = True, blank = True, choices = PRIORITY)
    STATUS = [
        ('pending' , 'pending' ),
        ('completed' , 'completed')

    ]
    status = models.CharField(max_length = 200,null = True, blank = True, choices = STATUS)


    Date_created = models.DateField(auto_now = True, blank = True)
    Date = models.DateField(auto_now_add = False, auto_now = False, blank = True)

    def __str__(self):
        return str(self.title) if self.title else ''