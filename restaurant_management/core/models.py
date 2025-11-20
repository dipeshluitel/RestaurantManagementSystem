from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    ROLE_CHOICES = [
        ('Admin','Admin'),
        ('Waiter','Waiter'),
        ('Kitchen','Kitchen'),
    ]

    user = models.OneToOneField(User, on_delete= models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

    
class MenuCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MenuItems(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    category = models.ForeignKey(MenuCategory, on_delete= models.CASCADE)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - Rs. {self.price}"
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending','Pending'),
        ('cooking','Cooking'),
        ('serverd','Served'),
        ('paid','Paid'),
    ]
    TABLE_NUMBER = [
        ('A1','A1'),('A2','A2'),('A3','A3'),
        ('B1','B1'),('B2','B2'),('B3','B3'),
        ('C1','C1'),('C2','C2'),('C3','C3'),
        ('Takeaway','Takeaway'),
    ]
    CUSTOMER_TYPE=[
        ('Special Guests','Special Guests'),('Normal Guests','Normal Guests')
    ]
    waiter = models.ForeignKey(User,on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending')
    customer_type = models.CharField(max_length=20,choices=CUSTOMER_TYPE,verbose_name='Customer Type')
    table_number = models.CharField(max_length=10,choices=TABLE_NUMBER,verbose_name='Table Number')
    notes = models.TextField(max_length=400,blank=True,null=True, verbose_name='Special Requirements')

    def __str__(self):
        return f"Order {self.id} by {self.waiter.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItems, on_delete= models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.item.name}"