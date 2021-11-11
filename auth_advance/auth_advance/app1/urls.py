from django.urls import path
from .views import HomeView,Logout,LogoutView,registrationForm,Login

urlpatterns = [
    path('home/',HomeView,name='home'),
    path('register/',registrationForm,name='register'),
    path('login/',Login,name='login'),
    path('logout/',Logout,name='logout'),
    path('',LogoutView,name='logoutView')


]