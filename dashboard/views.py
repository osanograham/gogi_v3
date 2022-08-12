from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
def dashboard(request):
	name =request.user.get_username()
	msg="Welcome back "+ name + ", "
	return render(request,"dashboard_main.html",{"greetings":msg})
def logout_(request):
	logout(request)
	return redirect('index')