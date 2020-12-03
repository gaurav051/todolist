
from django.contrib import admin
from todolist.models import Todolist, Userprofile


@admin.register(Userprofile)
class UserprofileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address',)


@admin.register(Todolist)
class TodolistAdmin(admin.ModelAdmin):
    list_display = ('name', 'title' , 'description', 'priority', 'status', 'Date',)
    list_search = ('title', 'priority', 'status',)