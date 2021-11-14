from django.urls import path
from .views import HomeView,articleView

urlpatterns = [
    path('',HomeView,name='home'),
    path('article/',articleView,name = 'article'),
   
]