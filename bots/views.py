from django.shortcuts import render
from .models import indices_bot,gold_bot,fx_bot,crypto_bot
from accounts.models import add_client_trading_account 
# Create your views here.

def bots_list(request):
	indices_bots_list=indices_bot.objects.all()
	user=request.user.email
	indices_bots_list_drop_down=add_client_trading_account.objects.filter(created_by=user)
	#print(indices_bots_list_drop_down)
	return render(request,"bots_list.html",{"indices_bots_list":indices_bots_list,"drop_down":indices_bots_list_drop_down})

def go_forex_bots(request):
	indices_bots_list=fx_bot.objects.all()
	user=request.user.email
	indices_bots_list_drop_down=add_client_trading_account.objects.filter(created_by=user)
	#print(indices_bots_list_drop_down)
	return render(request,"bots_list.html",{"indices_bots_list":indices_bots_list,"drop_down":indices_bots_list_drop_down})

def gold_bots(request):
	indices_bots_list=gold_bot.objects.all()
	user=request.user.email
	indices_bots_list_drop_down=add_client_trading_account.objects.filter(created_by=user)
	#print(indices_bots_list_drop_down)
	return render(request,"bots_list.html",{"indices_bots_list":indices_bots_list,"drop_down":indices_bots_list_drop_down})
def crypto_bots(request):
	indices_bots_list=crypto_bot.objects.all()
	user=request.user.email
	indices_bots_list_drop_down=add_client_trading_account.objects.filter(created_by=user)
	#print(indices_bots_list_drop_down)
	return render(request,"bots_list.html",{"indices_bots_list":indices_bots_list,"drop_down":indices_bots_list_drop_down})

def add_account(request,master,slave):
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
			if str(ac)==str(master):
				#print(ac)
				count=count+1
				break
		if count>0:
			print(acc)
			index=int(acc[0])
			content=indices_bot.objects.get(id=index)
			accounts_added=content.non_paid_subscribers
			content.non_paid_subscribers=str(slave)+":"+accounts_added
			content.save()
			content=indices_bot.objects.get(id=index)
			context={"Master":master,"Slave":slave}
			return render(request,"account_added.html",{"form":context})
			
			break
	return render(request,"account_added.html",{})
def add_account_to_crypto(request,master,slave):
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
			if str(ac)==str(master):
				#print(ac)
				count=count+1
				break
		if count>0:
			#print(acc)
			index=int(acc[0])
			content=crypto_bot.objects.get(id=index)
			accounts_added=content.non_paid_subscribers
			content.non_paid_subscribers=str(slave)+":"+accounts_added
			content.save()
			content=crypto_bot.objects.get(id=index)
			context={"Master":master,"Slave":slave}
			return render(request,"account_added.html",{"form":context})
			
			break
	return render(request,"account_added.html",{})
def add_account_to_gold(request,master,slave):
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
			if str(ac)==str(master):
				#print(ac)
				count=count+1
				break
		if count>0:
			#print(acc)
			index=int(acc[0])
			content=gold_bot.objects.get(id=index)
			accounts_added=content.non_paid_subscribers
			content.non_paid_subscribers=str(slave)+":"+accounts_added
			content.save()
			content=gold_bot.objects.get(id=index)
			context={"Master":master,"Slave":slave}
			return render(request,"account_added.html",{"form":context})
			
			break
	return render(request,"account_added.html",{})

def add_account_to_forex(request,master,slave):
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
			if str(ac)==str(master):
				#print(ac)
				count=count+1
				break
		if count>0:
			#print(acc)
			index=int(acc[0])
			content=fx_bot.objects.get(id=index)
			accounts_added=content.non_paid_subscribers
			content.non_paid_subscribers=str(slave)+":"+accounts_added
			content.save()
			content=fx_bot.objects.get(id=index)
			context={"Master":master,"Slave":slave}
			return render(request,"account_added.html",{"form":context})
			
			break
	return render(request,"account_added.html",{})