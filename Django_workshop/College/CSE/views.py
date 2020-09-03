from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CseStudentRegister


def home(request):
    return render(request, "index.html")


def welcome(request):
    return render(request, "welcome.html")


def about(request):
    return render(request, "about.html")


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_num = request.POST["phone_num"]
        email = request.POST.get('email')
        age = request.POST.get('age')
        student = CseStudentRegister(student_name=name, phone_num=phone_num,
                                     email=email, age=age)
        student.save()
        return redirect('student_details')
    return render(request, 'register.html')


def student_details(request):
    details = CseStudentRegister.objects.all()
    return render(request,'student_data.html', {'data': details})


def edit(request, id):
    student = CseStudentRegister.objects.get(id=id)
    if request.method == "POST":
        student.student_name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.phone_num = request.POST.get('phone_num')
        student.age = request.POST.get('age')

        student.save()
        return redirect('student_details')
    return render(request, 'edit.html', {'data': student})


def delete(request,id):
    student = CseStudentRegister.objects.get(id=id)
    student.delete()
    return redirect('student_details')