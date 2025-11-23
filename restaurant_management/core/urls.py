from django.contrib import admin
from django.urls import path
from .import views
from .views import CustomLogin
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", CustomLogin.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page='login'),name="logout"),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/waiter/', views.waiter_dashboard, name='waiter_dashboard'),
    path('dashboard/kitchen/', views.kitchen_dashboard, name='kitchen_dashboard'),
    path('dashboard/waiter/createorder/', views.create_order, name='create_order'),
    path('dashboard/waiter/giveorder/<int:order_id>/', views.give_order, name='give_order'),
    path('dashboard/kitchen/update/<int:order_id>/',views.update_order_status,name='update_order_status')
    
]
