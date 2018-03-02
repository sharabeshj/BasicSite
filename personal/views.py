from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'personal/content.html')

def contact(request):
	return render(request,'personal/basic.html',{'content':['Sharabesh','81,zircon C, near NIC, NITT, Thuakudi, Trichy']})