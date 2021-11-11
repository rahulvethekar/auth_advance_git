from django.urls import path
from .views import forgotPassword,forgotDetail

urlpatterns = [
    path('forgotPassword/',forgotPassword,name = 'forgotPassword'),
    path('resetPassword/',forgotDetail,name = 'reset'),

]