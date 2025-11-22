import datetime
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import OrderForm, PlaceOrderForm

from .models import MenuItems, Order

# Create your views here.
class CustomLogin(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        user = self.request.user
        role = self.request.user.profile.role

        if role == "Admin":
            return reverse_lazy('admin_dashboard')
        elif role == "Waiter":
            return reverse_lazy('waiter_dashboard')
        elif role == "Kitchen":
            return reverse_lazy('kitchen_dashboard')
        
        return reverse_lazy('login')

@login_required
def admin_dashboard(request):
    if request.user.profile.role != 'Admin':
        return redirect('login')
    time = datetime.datetime.now()
    order_count = Order.objects.count()
    pending_order_count = Order.objects.filter(status='pending').count()
    completed_order_count = Order.objects.filter(status='served').count()
    cooking_order_count = Order.objects.filter(status='cooking').count()
    return render(request, 'admin_dashboard.html',
    {'order_count':order_count, 
    'completed':completed_order_count,
    'pending':pending_order_count,
    'cooking':cooking_order_count,
    'time':time})

@login_required
def waiter_dashboard(request):
    if request.user.profile.role != 'Waiter':
        return redirect('login')
    time = datetime.datetime.now()  
    menu_items = MenuItems.objects.all()

    return render(request, 'waiter_dashboard.html',
    {'time':time,
     'items':menu_items})

@login_required
def kitchen_dashboard(request):
    if request.user.profile.role != 'Kitchen':
      return redirect('login')
    time=datetime.datetime.now()
    orders =  Order.objects.filter(status__in = ["pending","cooking"])
            
    return render(request, 'kitchen_dashboard.html',{'orders':orders,'time':time})

@login_required
def create_order(request):
    if request.user.profile.role!= 'Waiter':
        return redirect('login')
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.waiter = request.user
            order.save()
            return redirect('waiter_dashboard')
        
    else:
        form = OrderForm()
    return render(request,'create_order.html',{'form':form})

@login_required
def give_order(request):
    if request.user.profile.role!= 'Waiter':
        return redirect('login')
    if request.method == 'POST':
        form = PlaceOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.waiter = request.user
            order.save()
            return redirect('waiter_dashboard')
        
    else:
        form =PlaceOrderForm()
    return render(request,'give_order.html',{'form':form})


@login_required
def update_order_status(request,order_id):
    if request.user.profile.role != "Kitchen":
        return redirect('login')
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        order.status = new_status
        order.save()
    
    return redirect('kitchen_dashboard')