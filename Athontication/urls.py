from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login,name='login'),
    path('logout/', views.Logout_User, name='logout'),


]
