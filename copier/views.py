from django.shortcuts import render
from bots.models import indices_bot,gold_bot,fx_bot,crypto_bot
from accounts.models import add_client_trading_account 
from opentrades.trade_scanner import *
import time
import MetaTrader5 as mt5

#this function counts how many trades in the slave account have that given comment
def total_trades_with_comment(number=0, server="server",password="password", comment="comment"):
	import MetaTrader5 as mt5
	import time
	import MetaTrader5 as mt5
	from datetime import datetime
	count=0
	#print(comment)
	if mt5.initialize(login=number, server=server,password=password):
		positions=mt5.positions_get()
		if positions==None:
			return -1
		elif len(positions)>0:
			for positions in positions:
				symbol=(positions[16])
				comm=(positions[17]) 
				#print(symbol + "  : "+ comm)
				if comm ==comment:
					count=count+1
			if count>0:
				return 234000
			else:
				return -1	

				#break
		
	else:
		print("not logged in successfully")
#this function picks trades details and copies them into slave accounts
def base_copir(request,Master_trade_details,slave_trade_details,master_account_login,listed_accounts):
	global endtime
	endtime= time.time()
	comment_=Master_trade_details['trade_comment']
	symbol=Master_trade_details['symbol']
	account_number=int(slave_trade_details['account_number'])
	server=str(slave_trade_details['account_server_name'])
	password=str(slave_trade_details['account_password'])
	open_trades=total_trades_with_comment(account_number,server,password,comment_)
	## if open trades ==0, enter trades# prepare the buy request structure
	if listed_accounts.find(str(account_number))==-1:
		print("trade already exists ",account_number)
		return
	if(open_trades==None or open_trades== -1):
		symbol = symbol
		symbol_info = mt5.symbol_info(symbol)
		#print(symbol)
		if symbol_info is None:
		    print(symbol, "not found, can not call order_check()")
		    mt5.shutdown()
		    quit()
		else:
			lot = 0.1
			point = mt5.symbol_info(symbol).point
			price = mt5.symbol_info_tick(symbol).ask
			deviation = 20
			request = {
			    "action": mt5.TRADE_ACTION_DEAL,
			    "symbol": symbol,
			    "volume": lot,
			    "type": mt5.ORDER_TYPE_BUY,
			    "price": price,
			    "sl": price - 100 * point,
			    "tp": price + 100 * point,
			    "deviation": deviation,
			    "magic": 234000,
			    "comment":Master_trade_details['trade_comment'],
			    "type_time": mt5.ORDER_TIME_GTC,
			    "type_filling": mt5.ORDER_FILLING_RETURN,
			}
			result = mt5.order_send(request)

	else:
		pass

def base_copier(request):
	starttime=time.time()
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
	import time
	t2=time.time()
	#loop accrosss all the trades in master accounts
	for acc in all_accounts:
		#print(acc[1])
		server=(acc[7])
		login=(acc[8])
		password=(acc[9])
		#look for ttrades in this account
		result=[]
		result=(main(login,server,password))
		account_=(acc[13])
		total=(total_trades(login,server,password))
		slaves=[]
		slaves=(account_.split(":"))
		context_trades_details={}
		#loop accross all the trades and record their details in a dictionary
		if total==0:
			#print("This is a good trade")
			continue
		for req in main(login,server,password):
			#print(req)
			context_trades_details={}
			context_trades_details={
			"trade_comment":str(str(req[0])),
			"order_type":(req[2]),
			"lot_size":(req[3]),
			"sl":(req[5]),
			"tp":(req[6]),
			"symbol":str(req[8]),
			}
			for slaves  in slaves:
				slave_accounts={}
				sla_=add_client_trading_account.objects.filter(account_number__contains=str(slaves)).values()
				#print(sla_)
				if sla_:
					sla_=(list(sla_)[0])
					slave_accounts={
					"account_number":sla_['account_number'],
					"choose_platform":sla_['choose_platform'],
					"account_password":sla_['account_password'],
					"account_server_name":sla_['account_server_name'],
					}
					base_copir(request,context_trades_details,slave_accounts,login,account_)
	t3=time.time()
	print(starttime-endtime)
	return render(request,"base_copier.html",{"context":"acco"})
