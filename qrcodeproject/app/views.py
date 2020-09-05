from django.shortcuts import render
import random
import qrcode
from django.http import HttpResponse
# Create your views here.
ootp=0
def login(req):
	if req.method=="POST":
		uname=req.POST['username']
		pas=req.POST['password']
		if uname=="satheesh" and pas=="APSSDC":
			otp=random.randint(10000,99999)
			global ootp
			ootp=otp
			print(ootp)
			image=qrcode.make("hello user"+uname+"ypor otp is"+str(otp))
			image.save(r"app/static/qrcodeimage/otp.jpg")
			return render(req,'app/qrcodepage.html')
	return render(req,"app/login.html")
def qrvalidation(req):
	if req.method=="POST":
		no=req.POST['qrno']
		if no==str(ootp):
			return render(req,"app/home.html")
		else:
			return HttpResponse("data otp wrong")


	return render(req,"app/qrcodepage.html")