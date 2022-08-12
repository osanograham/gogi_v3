
# display data on the MetaTrader 5 package
from second import *
import time
import MetaTrader5 as mt5

if mt5.initialize(login=172108, server="osprey-demo",password="asygo8ie"):
	symbol = "USDJPY"
	symbol_info = mt5.symbol_info(symbol)
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
    		"sl": price - 1000 * point,
    		"tp": price + 1000 * point,
    		"deviation": deviation,
    		"magic": 234000,
    		"comment": "python script open",
    		"type_time": mt5.ORDER_TIME_GTC,
    		"type_filling": mt5.ORDER_FILLING_IOC,
    		}
    		result = mt5.order_send(request)
else:
  	print("we are not able to log in")
t2=time.time()
main()

t3=time.time()





