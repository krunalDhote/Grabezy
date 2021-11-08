from django.db import models
from django.db.models.base import Model
from django.db.models.fields import AutoField

# Create your models here.

class Contact(models.Model):
    contact_id=models.AutoField
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    phone=models.CharField(max_length=13)
    email=models.CharField(max_length=20)
    issue=models.TextField()
    def __str__(self):
        return self.fname + " " + self.lname


class Electronic(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    catagory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="static/images",default="")
    def __str__(self):
        return self.product_name


class Grocery(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    catagory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="static/images",default="")
    def __str__(self):
        return self.product_name


class Fashion(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    catagory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="static/images",default="")
    def __str__(self):
        return self.product_name


class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.TextField(max_length=50000)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=12,default="")
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=50)
    pincode=models.CharField(max_length=6,default="")
    state=models.CharField(max_length=20,default="")

    def __str__(self):
        return str(self.order_id)
 


class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        orderString=str(self.order_id) +" "+ self.update_desc[0:20] + "..."
        return orderString
   
class Feedback(models.Model):
    feedback_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=15)
    feedback=models.TextField(max_length=10000)

    def __str__(self):
        return self.username