from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CseStudentRegister, Faculty
from django.contrib import messages
from .forms import FacultyRegisterForm
from College import settings
from django.core.mail import EmailMessage


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
        sub = 'Regards Student register'
        body = 'Hi' + name+',\n We are glad to have you in our platform'
        send = settings.EMAIL_HOST_USER
        receiver = email
        email_msg = EmailMessage(sub, body, send, [receiver])
        email_msg.send()

        messages.success(request, 'Student added Successfully!!!')
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
        messages.info(request, 'Student details updated Successfully!!!')
        return redirect('student_details')
    return render(request, 'edit.html', {'data': student})


def delete(request,id):
    student = CseStudentRegister.objects.get(id=id)
    student.delete()
    messages.warning(request, 'A Student details deleted!!!')
    return redirect('student_details')


def faculty_register(request):
    form = FacultyRegisterForm()
    if request.method == 'POST':
        form_data = FacultyRegisterForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('Faculty added successfully!!!')
        return HttpResponse("invalid details!!")
    return render(request, 'facultyregister.html', {'form': form})


def faculty_edit(request, num):
    faculty_data = Faculty.objects.get(id=num)
    form = FacultyRegisterForm(request.POST or None, instance=faculty_data)
    if form.is_valid():
        form.save()
        return HttpResponse("details edited successfully!!")
    return render(request, 'facultyedit.html', {'form': form})

