# -*- coding: utf-8 -*-
"""
Created on Tue May 15 16:11:17 2018

@author: vkulikov
"""

from datetime import datetime




import ccxt  # noqa: E402
import re


binance = ccxt.binance()

binance.load_markets()


symbols = []

for x in binance.markets:
    #print (x)
    [x1,x2] =  re.split('/', x)
    #print (x1)
    
    if x1 not in symbols:
        if binance.markets.get(x1+'/ETH'):
            if binance.markets.get(x1+'/BNB'):
                if binance.markets.get(x1+'/BTC'):
                    #if binance.markets.get(x1+'/USDT'):
                        symbols.append(x1)
#
#
#print (symbols)
#print (len(symbols))
#    if (re.search('/ETH$', x)!=None):
#        print (x)


#
#
#
def get3profit(ss,s2):

    symbol1 = ss + '/BTC'
    symbol2 = ss + '/' + s2
    symbol3 = s2 + '/BTC'
    
    bits=1
    
    orderbook = binance.fetch_order_book (symbol1,5)
    bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
    ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None
    #print (binance.id, 'market price', { 'bid': bid, 'ask': ask })
    
    eth = bits/ask
    
    #print('ETH:',eth)
    
    orderbook = binance.fetch_order_book (symbol2,5)
    bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
    ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None
    #print (binance.id, 'market price', { 'bid': bid, 'ask': ask })
    
    usdt = eth * bid
    
    #print('USDT:',usdt)
    
    orderbook = binance.fetch_order_book (symbol3,5)
    bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
    ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None
    #print (binance.id, 'market price', { 'bid': bid, 'ask': ask })
    
    bit = usdt * bid
    
    return bit    

pro = 1.002
maxpro = 0;

print (0)

for i in range(1,1000):
    maxpro = 0;
    for x in symbols:
        r=get3profit(x,'BNB')
        #print (x,r,'BNB')
        if (r-1)*100>maxpro:
            maxpro = (r-1)*100                
        if r>pro:
            while r>pro:
                pp=(r-1)*100
                print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),x+'/'+'BNB',pp,'%')
                r=get3profit(x,'BNB')
                if (r-1)*100>maxpro:
                    maxpro = (r-1)*100                
        r=get3profit(x,'ETH')
        #print (x,r,'ETH')
        if (r-1)*100>maxpro:
            maxpro = (r-1)*100                
        if r>pro:
            while r>pro:
                pp=(r-1)*100
                print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),x+'/'+'ETH',pp,'%')
                r=get3profit(x,'ETH')
                if (r-1)*100>maxpro:
                    maxpro = (r-1)*100                
        #r=get3profit(s1,'USDT')
        #print(x+'/'+'USDT',r)

    print (i,maxpro)
