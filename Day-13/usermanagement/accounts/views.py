from django.shortcuts import render

from django.contrib.auth.models import User

from accounts.models import Profile

from django.contrib.auth import login,logout,authenticate 

# Create your views here.


def home(request):
	return render(request,'accounts/home.html')



def register(request):
	error=""
	if request.method=="POST":
		fname=request.POST['first_name']
		lname=request.POST['last_name']
		uname=request.POST['username']
		em=request.POST['email']
		img=request.FILES['img']
		mb=request.POST['mobileno']
		dob=request.POST['dob']
		pwd=request.POST['pswd']
		try:
			user=User.objects.create_user(first_name=fname,last_name=lname,
				username=uname,email=em,password=pwd)
			Profile.objects.create(user=user,image=img,mobileno=mb,dob=dob)
			error = "no"
		except:
			error="yes"
	context={'error':error}
	return render(request,'accounts/register.html',context)


def signin(request):
	error=""
	if request.method=="POST":
		uname=request.POST['uname']
		pwd=request.POST['pwd']
		user=authenticate(username=uname,password=pwd)
		try:
			if user:
				login(request,user)
				error="no"
			else:
				error='yes'
		except:
			error="yes"
	context={'error':error}
	return render(request,'accounts/signin.html',context)