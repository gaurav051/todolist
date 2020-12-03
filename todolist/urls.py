
from django.urls import path
from todolist.views import guest_view, create_list, update_list, delete_list, create


app_name = 'todolist'

urlpatterns = [
    path('guest/<str:pk>/', guest_view, name = 'guest_view'),
    path('create_list/', create_list, name = 'create_list'),
    path('create/', create, name = 'create'),
    path('update_list/<str:pk>/', update_list, name = 'update_list'),
    path('delete_list/<str:pk>/', delete_list, name = 'delete_list'),


    
    
    ]

