from django.urls import path
from .views import RegistrationView,loginView,logoutView ,changePassword,forgotPassword,forgotDetail

urlpatterns = [
    path('cRegister',RegistrationView,name = 'cRegister'),
    path('cLogin/',loginView,name = 'cLogin'),
    path('cLogout/',logoutView,name = 'cLogout'),
    path('changePassword/',changePassword,name = 'changePassword'),
    path('forgotPassword/',forgotPassword,name = 'forgotPassword'),
    path('resetPassword/',forgotDetail,name = 'reset'),
    
]