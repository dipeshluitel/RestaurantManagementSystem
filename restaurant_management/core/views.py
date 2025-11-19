from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
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
    return render(request, 'admin_dashboard.html')

@login_required
def waiter_dashboard(request):
    if request.user.profile.role != 'Waiter':
        return redirect('login')
    return render(request, 'waiter_dashboard.html')

@login_required
def kitchen_dashboard(request):
    if request.user.profile.role != 'Kitchen':
        return redirect('login')
    return render(request, 'kitchen_dashboard.html')