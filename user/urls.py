from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('register/manager/',ManagerRegisterView.as_view(),name='manager_register'),
    path('register/developer/',DeveloperRegisterView.as_view(),name='developer_register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('manager/dashboard/',ManagerDashboardView.as_view(),name='manager_dashboard'),
    path('developer/dashboard/',DeveloperDashBoardView.as_view(),name='developer_dashboard'),
    
]
