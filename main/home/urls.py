
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('signup',views.signup,name='signup')
]