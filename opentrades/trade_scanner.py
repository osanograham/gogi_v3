
# display data on the MetaTrader 5 package


#BUY NZDUSD, LOTSIZE 10, sl=12343, tp=13443,"robot identify"
def main(number=0, server="server",password="password"):
    try:
        count=0.1
        import time
        import MetaTrader5 as mt5
        from datetime import datetime
       # print("attempting to login")
        if mt5.initialize(login=number, server=server,password=password):
            #print("logged in successfully")
            positions=mt5.positions_get()
            if positions==None:
                list_ =[]
                return list_
                print("No positions on , error code={}".format(mt5.last_error()))
            elif len(positions)>0:
                trades=[]
                # display all open positions
                count=0
                for positions in positions:
                    #print(positions)
                    new_list=[]
                    count=0
                    for p in positions:
                        if count ==2 or count==3 or count==4 or count ==6 or count==7 or count==8 or count==13 or count ==14 or count==18:
                            pass
                        else:
                            new_list.append(p)
                        count=count+1
                    trades.append(new_list)
                #print(count)  
                
                return trades
    except:
        print("we could not log in successfully")    
    mt5.shutdown()
def total_trades(number=0, server="server",password="password"):
    try:
        count=0.1
        import time
        import MetaTrader5 as mt5
        from datetime import datetime
       # print("attempting to login")
        if mt5.initialize(login=number, server=server,password=password):
            #print("logged in successfully")
            positions_total=mt5.positions_total()
            return positions_total

    except:
        print("we could not log in successfully")    
    mt5.shutdown()
 






"""    account=[(60873705,"MetaQuotes-Demo","7ovjfnrf"),(5004804271,"MetaQuotes-Demo","evg2xjwx"),(5004804287,"MetaQuotes-Demo","juid8als"),(5004804311,"MetaQuotes-Demo","vqckef8r"),(5004804318,"MetaQuotes-Demo","lvkimx0o")]
    account=[(60873705,"MetaQuotes-Demo","7ovjfnrf"),(5004804271,"MetaQuotes-Demo","evg2xjwx"),(5004804287,"MetaQuotes-Demo","juid8als"),(5004804311,"MetaQuotes-Demo","vqckef8r"),(5004804318,"MetaQuotes-Demo","lvkimx0o")]

# prepare the buy request structure
            symbol = "GBPUSD"
            symbol_info = mt5.symbol_info(symbol)

            if symbol_info is None:
                print(symbol, "not found, can not call order_check()")
                #mt5.shutdown()
                quit()
             
            # if the symbol is unavailable in MarketWatch, add it
            if not symbol_info.visible:
                print(symbol, "is not visible, trying to switch on")
                if not mt5.symbol_select(symbol,True):
                    print("symbol_select({}}) failed, exit",symbol)
                   # mt5.shutdown()
                    quit()
             
            lot = count
            point = mt5.symbol_info(symbol).point
            price = mt5.symbol_info_tick(symbol).ask
            deviation = 200
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
                "type_filling": mt5.ORDER_FILLING_RETURN,
            }
             
            # send a trading request
            result = mt5.order_send(request)
            count=count+0.1
            print(count)
    for account in account:
        if not mt5.initialize(login=account[0], server=account[1],password=account[2]):
           quit()
        mt5.shutdown()



if not mt5.initialize(login=1177950, server="FreshForex-MT5",password="4mqhecpx"):
        quit()
    
    if not mt5.initialize(login=1177952, server="FreshForex-MT5",password="mzuwdv8v"):
        quit()
    
    if not mt5.initialize(login=1177953, server="FreshForex-MT5",password="ueobkcr3"):
        quit()
    mt5.shutdown()

"""


