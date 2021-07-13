from django.db import models
from django.db.models.fields.related import ForeignKey
Gander = (
    ("Male", "Male"),
    ("Female", "Female"),
)

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_Name= models.CharField(max_length=100)
    last_Name= models.CharField(max_length=100)
    salary= models.IntegerField()
    totalDay = models.IntegerField()
    contact= models.IntegerField()
    email= models.EmailField(max_length=254)
    gander= models.CharField(max_length=50)
    address= models.CharField(max_length=400)
    city= models.CharField(max_length=100)
    pincode= models.IntegerField()
    state= models.CharField(max_length=100)
    country= models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} : {self.first_Name} {self.last_Name}"
    
class Attedance(models.Model):
    id = models.AutoField(primary_key=True)
    employee = models.CharField(max_length=200)
    date = models.DateField(auto_now=False, auto_now_add=False)
    in_time = models.TimeField(auto_now=False, auto_now_add=False)
    out_time = models.TimeField(auto_now=False, auto_now_add=False)
    desc = models.CharField(max_length=500)
    
    def __str__(self):
        return f"{self.employee} : {self.date}"