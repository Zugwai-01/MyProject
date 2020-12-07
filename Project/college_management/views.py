from django.shortcuts import render
#from django.http import HttpResponse
#from college_management.models import Student,Department,Staff,Courses
from .forms import FormName,DeptForm




def students(request):

    Student_list = Student.objects.order_by('first_name')
    Student_dict = {'students':Student_list}
    return render (request,'college_management/students.html',context=Student_dict)

def departments(request):

    Department_list = Department.objects.order_by('Name_of_dept')
    Department_dict = {'departments':Department_list}

    return render (request,'college_management/departments.html',context=Department_dict)

#def staffs(request):

    #Staff_list = Staff.objects.order_by('Staff_ID')
    #Staff_dict = {'staffs':staffs_list}
    #return render (request,'college_management',context=Staff_dict)

#def course(request):

    #Courses_list = Courses.objects.order_by('Course_code')
    #Courses_dict = {'course':course_list}
    #return render (request,'college_management',context=Courses_dict)

def homepage(request):
    form = FormName()

    if request.method == "POST":
        form = FormName(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
    return render(request,'college_management/homepage.html',{'form':form})

def index(request):
    return render(request,'college_management/index.html',)

def departments(request):
    form = DeptForm()

    if request.method == "POST":
        form = DeptForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
    return render(request,'college_management/departments.html',{'form':form})

def about(request):
    return render(request,'college_management/about.html',)

def library(request):
    return render(request,'college_management/library.html',)

def news(request):
    return render(request,'college_management/news.html',)

def Studentcouncil(request):
    return render(request,'college_management/Studentcouncil.html',)
