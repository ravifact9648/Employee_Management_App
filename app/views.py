from django.contrib import messages
from django.shortcuts import render, redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.models import User, auth
from app.forms import EmployeeForm
from django.shortcuts import HttpResponse
from django.contrib import messages
from app.models import Employee
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'app/home.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']  
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect(register)
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password, 
                                        email=email, first_name=first_name, last_name=last_name)
                user.save() 
                return redirect('login_user')
        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register)
    else:
        return render(request, 'app/registration.html')
    
def regsuccess(request):
    return render(request, 'app/regsuccess.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')
    else:
        return render(request, 'app/login.html')

def logout_user(request):
    auth.logout(request)
    return redirect('home')

def employee_data(request):
    form=EmployeeForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('success')
    return render(request,'app/empdataform.html',{'form':form})


def get_emp_data(request):
    emp_data=Employee.objects.all()
    return render(request,'app/emp_data.html',{'emp_data':emp_data})

def success(request):
    return render(request, 'app/formsuccess.html')


def update_view(request, id):
    context ={}
    emp = get_object_or_404(Employee, id = id)
    form = EmployeeForm(request.POST or None, instance = emp)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/app/get_emp_data")
    context["form"] = form
    return render(request, "app/update_view.html", context)



def delete_view(request, id):
    context ={}
    emp = get_object_or_404(Employee, id = id)
    if request.method =="POST":
        emp.delete()
        return HttpResponseRedirect("/app/get_emp_data")
    return render(request, "app/delete_view.html", context)
