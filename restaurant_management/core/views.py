from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
@login_required
def dashboard(request):
    user_groups = request.user.groups.values_list('name', flat=True)

    if 'Admin' in user_groups:
        return redirect('admin_dashboard')
    elif 'Waiter' in user_groups:
        return redirect('waiter_dashboard')
    elif 'Kitchen' in user_groups:
        return redirect('kitchen_dashboard')
    else:
        return redirect('logout')
    
    
@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required
def waiter_dashboard(request):
    return render(request, 'waiter_dashboard.html')

@login_required
def kitchen_dashboard(request):
    return render(request, 'kitchen_dashboard.html')