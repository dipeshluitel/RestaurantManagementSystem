# Restaurant Management System (Django) (Ongoing)

A simple Django-based restaurant management system with role-based dashboards for **Admin**, **Waiter**, and **Kitchen Staff**.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Models](#models)  
3. [Views](#views)  
4. [Templates](#templates)  
5. [URLs](#urls)  
6. [Usage](#usage)  

---

## Project Overview

This project allows:

- **Admin**: View summary of orders and statuses.
- **Waiter**: Create orders and add items to them.
- **Kitchen Staff**: View pending/cooking orders, update status to cooking or served.

Role-based access ensures users only access their respective dashboards.

---

## Models

### Profile

```python
class Profile(models.Model):
    ROLE_CHOICES = [('Admin','Admin'), ('Waiter','Waiter'), ('Kitchen','Kitchen')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
