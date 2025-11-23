# Restaurant Management System (Django)  

> **Status:** Ongoing Project  

A Django-based restaurant management system with **role-based dashboards** for Admin, Waiter, and Kitchen Staff.  
This project is under development and new features will be added gradually.

---

## Project Overview

This system allows:

- **Admin**: View a summary of all orders and their statuses.  
- **Waiter**: Create orders, add items to orders.  
- **Kitchen Staff**: View pending/cooking orders and update order status.  

Role-based access ensures each user only accesses their relevant dashboard.

---

## Models

### Profile

```python
class Profile(models.Model):
    ROLE_CHOICES = [('Admin','Admin'), ('Waiter','Waiter'), ('Kitchen','Kitchen')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
