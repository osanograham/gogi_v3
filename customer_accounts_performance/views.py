from django.shortcuts import render
from accounts.models import add_client_trading_account
# Create your views here.

def individual_performance(request):
	indices_bots_list=add_client_trading_account.objects.all()
	return render(request,"performance.html",{"indices_bots_list":indices_bots_list})

def account_history_(request):
	return render(request,"account_history2.html",{})


 

