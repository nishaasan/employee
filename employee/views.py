from django.shortcuts import render,get_object_or_404
from employee.models import Employee
from django.http import Http404,HttpResponse

# Create your views here.
def emp_details(request,id):
    try:
        # employee = Employee.objects.get(id=id)
        # print(employee)
        employee=get_object_or_404(Employee,id=id)
        # print(employee)
        # return HttpResponse(employee)
        context={
            'employee':employee,
        }
        return render(request,'emp_details.html',context)
    except:
        raise Http404
    
def emp2(request):
    return render(request,'1.html')

