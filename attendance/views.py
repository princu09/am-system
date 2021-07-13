from django.shortcuts import render, redirect
# import Tables
from attendance.models import Attedance , Employee
# Login account
from django.contrib.auth import authenticate, login, logout
# Gmail Request Add
import smtplib

def index(request):
    e = Employee.objects.all()
    empLen = len(e)
    a = Attedance.objects.all()
    atteLen = len(a)
    return render(request , 'index.html' , {'empLen' : empLen , 'atteLen':atteLen})

def add_employee(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        salary = request.POST['salary']
        contact = request.POST['contact']
        email = request.POST['email']
        gander = request.POST['gander']
        address = request.POST['address']
        city = request.POST['city']
        pincode = request.POST['pincode']
        state = request.POST['state']
        country = request.POST['country']

        u = Employee(first_Name=fname , last_Name=lname , salary=salary , contact=contact , email=email , gander=gander , address=address , city=city , pincode=pincode , state=state , country=country)
        u.save()
        return redirect('/add_employee')

    return render(request , 'add_employee.html')

def detail_employee(request):
    employee = Employee.objects.all()
    return render(request , 'detail_employee.html', context={'employee': employee})

def add_attendance(request):
    if request.method=="POST":
        empId = request.POST['emp_id']
        emp = request.POST['employee']
        attedance_date = request.POST['attedance_date']
        in_time = request.POST['in_time']
        out_time = request.POST['out_time']
        desc = request.POST['desc']

        a = Attedance.objects.create(employee=emp , date=attedance_date , in_time=in_time , out_time=out_time , desc=desc)
        a.save()
        
        e = Employee.objects.filter(id=empId)
        newData = e[0].totalDay + 1
        empNew = Employee.objects.filter(id=empId).update(totalDay=newData)
        return redirect('/add_attendance')

    employee = Employee.objects.all()
    return render(request , 'add_attendance.html', context={'employee':employee})

def detail_attendance(request):
    attedance = Attedance.objects.all()
    return render(request , 'detail_attendance.html' , context={'attedance' : attedance})

def handleLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request , 'incFiles/login.html')

def handleLogout(request):
    logout(request)
    return redirect('/')

def update_employee(request , id):
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        salary = request.POST['salary']
        contact = request.POST['contact']
        email = request.POST['email']
        gander = request.POST['gander']
        address = request.POST['address']
        city = request.POST['city']
        pincode = request.POST['pincode']
        state = request.POST['state']
        country = request.POST['country']

        u = Employee.objects.filter(id=id).update(first_Name=fname , last_Name=lname , salary=salary , contact=contact , email=email , gander=gander , address=address , city=city , pincode=pincode , state=state , country=country)
        return redirect('/detail_employee')

    employee = Employee.objects.filter(id=id)
    return render(request , 'update_employee.html', context={'employee':employee})
    
def delete_employee(request , id):
    d = Employee.objects.filter(id=id)
    d.delete()
    return redirect('/detail_employee')

def delete_attendance(request , id):
    d = Attedance.objects.filter(id=id)
    d.delete()
    return redirect('/detail_attendance')