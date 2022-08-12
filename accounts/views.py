from django.shortcuts import render
from .import forms
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from users.models import CustomUser
from .models import add_client_trading_account 
from .decorators import main

# Create your views here.
def logged_user(request):
	current_user = request.user
	print (current_user.email)
	main(request)

	return render(request,"logged_user.html",{"form":"form"})

def add_account(request):
	add_account_form=forms.add_client_account_form
	form=add_account_form(request.POST)
	#print(request.user.email)
	#print(form)
	if request.method=="POST":
		if form.is_valid():
			user=form.save()
			print(user.created_by)
			user.created_by=request.user.email
			form.save()
			
			return redirect('my-trading-accounts')
		else:
			return render(request,'add_client_account.html',{"form":form})
	else:
		print("not post")
		return render(request,'add_client_account.html',{"form":form})
def trading_accounts(request):
	return render(request,"trading_accounts.html",{})

def delete_account(request):
	return render(request,'delete_account.html',{})
def account_history(request):
	return render(request,'account_history.html',{})

def test(request):
	total_accounts=add_client_trading_account.objects.all().count()

	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits+1
	print(num_visits)
	context = {
	'num_visits': num_visits,
	}
	return render(request,'test.html',context)

def my_trading_accounts(request):
	user=request.user.email
	indices_bots_list=add_client_trading_account.objects.filter(created_by=user)
	return render(request,"my_trading_accounts.html",{"indices_bots_list":indices_bots_list})

def account_details(request,num):
	account=add_client_trading_account.objects.all().filter(account_number=num).values()
	return render(request,"account_details.html",{"account":account})
def status_Set(request,change,status,num):
	account=add_client_trading_account.objects.all().filter(account_number=num).values()
	indices_bots_list=add_client_trading_account.objects.all()
	return render(request,"my_trading_accounts.html",{"indices_bots_list":indices_bots_list})
