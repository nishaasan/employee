from django.http import HttpResponse
from django.shortcuts import render
from employee.models import Employee
# def index(request):
#     return HttpResponse('<h1>home page</h1>')



def homepage(request):
    employees=Employee.objects.all()
    print(employees)
    context={
        'employees':employees,
    }
    return render(request,'index.html',context)