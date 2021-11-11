from django.urls import path
from .views import changePassword

urlpatterns = [
    path('changePassword/',changePassword,name = 'changePassword'),
]