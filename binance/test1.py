# -*- coding: utf-8 -*-
"""
Created on Tue May 15 16:11:17 2018

@author: vkulikov
"""

import ccxt  # noqa: E402
import re

# -----------------------------------------------------------------------------

binance = ccxt.binance()

binance.load_markets()



#for x in binance.markets:
#    #print (x)
#    #if (re.search('/BTC$', x)!=None):
#    #    print (x)
#
#    if (re.search('/ETH$', x)!=None):
#        print (x)


s1 = 'ETH'
s1 = 'BNB'
s1 = 'XRP'
s1 = 'ETH'
s1 = 'ADA'



def get3profit(ss):

    symbol1 = ss + '/BTC'
    symbol2 = ss + '/BNB'
    symbol3 = 'BNB/BTC'
    
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

for x in range(0, 20):
    r=get3profit(s1)
    print('BTC:',r)

