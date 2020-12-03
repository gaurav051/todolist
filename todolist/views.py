from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from todolist.forms import Todolistform, userprofileform
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from todolist.models import Todolist,Userprofile


def guest_view(request, pk):
    name = Userprofile.objects.get(id = pk)
    todo = name.todolist_set.all()
    context = { 'todo' : todo , 'name': name}


    return render(request, 'guest.html', context)

def create(request):
    if request.method == 'POST':
        form = userprofileform(request.POST)

        if form.is_valid():
            n = form.cleaned_data['address']
            t = Userprofile(address= n)
            t.save()
            request.user.name.add(t)

        return HttpResponseRedirect('/guest/'+str(t.id)+'/')

    else:
        form = userprofileform()

        return render(request,'create.html', {'form': form} )


def create_list(request):
    user = request.user
    form = Todolistform(request.POST)
    if form.is_valid():
        form = Todolistform(request.POST)
  
        form.save()
        return HttpResponseRedirect('/guest/'+str(user.id)+'/')

    context = {'form': form}
    return render(request, 'create_list.html', context) 

def update_list(request, pk):
    user = request.user
    todo = Todolist.objects.get(id = pk)
    form = Todolistform(instance = todo)
    if request.method == 'POST':
        form = Todolistform(request.POST, instance = todo)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/guest/'+str(user.id)+'/')

    context = {'form': form}
    return render(request, 'update_list.html', context )

def delete_list(request, pk):
    user = request.user
    todo = Todolist.objects.get(id = pk)
    if request.method == 'POST':
        todo.delete()
        return HttpResponseRedirect('/guest/'+str(user.id)+'/')
    context = {'todo': todo }
    return render(request, 'delete_list.html', context)

