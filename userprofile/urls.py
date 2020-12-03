
from django.urls import path
from userprofile.views import login_view, register_view, user_logout_view


app_name = 'userprofile'

urlpatterns = [
    path('register/', register_view, name = 'register'),
    path('login/', login_view, name = 'login'),
    path('logout/', user_logout_view, name = 'logout'),
    ]

