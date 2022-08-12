from django.shortcuts import render
from .trade_scanner import *
import time
from bots.models import indices_bot,fx_bot,gold_bot,crypto_bot
t2=time.time()
main()

t3=time.time()

# Create your views here.

def result(request):
	#open_trades=main()
	return render(request,"results.html",{"opentrades":"open_trades"})
def results_specific(request,indices_nu="5"):

	indices_nuts=[]
	all_accounts=[]
	form1=indices_bot.objects.all().values_list()
	for acc in form1:
		accounts=[]
		for ac in acc:
			accounts.append(ac)
		all_accounts.append(accounts)
	form2=fx_bot.objects.all().values_list()
	for acc in form2:
		accounts=[]
		for ac in acc:
			accounts.append(ac)
		all_accounts.append(accounts)
	form3=gold_bot.objects.all().values_list()
	for acc in form3:
		accounts=[]
		for ac in acc:
			accounts.append(ac)
		all_accounts.append(accounts)
	form4=crypto_bot.objects.all().values_list()
	for acc in form4:
		accounts=[]
		for ac in acc:
			accounts.append(ac)
		all_accounts.append(accounts)
	count=0
	#print(accoun)
	for acc in all_accounts:
		for ac in acc:
			if str(ac)==str(indices_nu):
				#print(indices_nu)
				count=count+1
				break
		if count>0:
			
			open_trades=main(acc[8],acc[7],acc[9])
			print(acc)
			return render(request,"results.html",{"opentrades":open_trades})
			break
	return render(request,"results.html",{})
	
	
