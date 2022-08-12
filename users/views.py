from django.shortcuts import render
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django import forms 
from .forms import CustomUserCreationForm

# Create your views here.
def signup(request):
	form=CustomUserCreationForm(request.POST)
	if request.method=="POST":
		username=request.POST.get('username')
		password=request.POST.get('password')
		if form.is_valid():
			user=form.save()
			login(request,user)
			return redirect('dashboard-template')
		else:
			print("form is not valid")
			return render(request,'sign-up.html',{"form":form})
	else:
		return render(request,'sign-up.html',{"form":form})

def signin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('dashboard-template')
    else:
        return render(request,'signin.html',{})