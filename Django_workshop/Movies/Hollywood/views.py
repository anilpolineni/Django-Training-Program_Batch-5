from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	data = {'Name': "Vidhya Sagar Bobby", 'Number': 'Y18CS146'}
	return render(request,'home.html',{'info':data})

def moviename(request, name, id):
	return HttpResponse("Welcome {} {}".format(name, str(id)))

def table(request, n):
	tab = []
	for i in range(1, 11):
		tab.append("{} * {} = {} ".format(n, i, n*i))
	return HttpResponse(tab)

def index(request):
	return render(request, 'index.html')