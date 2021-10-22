from django.db import models
from django.db.models.base import Model

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
   