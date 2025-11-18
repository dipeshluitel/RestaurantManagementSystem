from django.contrib import admin
from django.urls import path
from .import views
from .views import CustomLogin

urlpatterns = [
    path("", CustomLogin.as_view(), name="login"),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/waiter/', views.waiter_dashboard, name='waiter_dashboard'),
    path('dashboard/kitchen/', views.kitchen_dashboard, name='kitchen_dashboard'),
    
]
