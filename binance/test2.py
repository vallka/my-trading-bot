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

#symbols = ['AMB']


#
#
#
def get3profits(ss):
    debug = False

    btc=1

    symbol1 = ss + '/BTC'
    
    orderbook1 = binance.fetch_order_book (symbol1,5)
    bid = orderbook1['bids'][0][0] if len (orderbook1['bids']) > 0 else None
    ask = orderbook1['asks'][0][0] if len (orderbook1['asks']) > 0 else None
    ask1 = orderbook1['asks'][1][0] if len (orderbook1['asks']) > 0 else None

    q = btc/ask
    q1 = btc/ask1
    if debug:
        print (symbol1,binance.id, 'market price', { 'bid': bid, 'ask': ask },q,q1)

    symbol2 = ss + '/ETH'
    
    orderbook2 = binance.fetch_order_book (symbol2,5)
    bid = orderbook2['bids'][0][0] if len (orderbook2['bids']) > 0 else None
    ask = orderbook2['asks'][0][0] if len (orderbook2['asks']) > 0 else None
    bid1 = orderbook2['bids'][1][0] if len (orderbook2['bids']) > 0 else None

    eth = q * bid
    eth1 = q1 * bid1
    if debug:
        print (symbol2,binance.id, 'market price', { 'bid': bid, 'ask': ask },eth,eth1)
    
    symbol3 = ss + '/BNB'
    
    orderbook3 = binance.fetch_order_book (symbol3,5)
    bid = orderbook3['bids'][0][0] if len (orderbook3['bids']) > 0 else None
    ask = orderbook3['asks'][0][0] if len (orderbook3['asks']) > 0 else None
    bid1 = orderbook3['bids'][1][0] if len (orderbook3['bids']) > 0 else None
    bnb = q * bid
    bnb1 = q1 * bid1
    if debug:
        print (symbol3,binance.id, 'market price', { 'bid': bid, 'ask': ask },bnb,bnb1)

    symbol4 = ss + '/USDT'
    if binance.markets.get(symbol4):
        orderbook4 = binance.fetch_order_book (symbol4,5)
        bid = orderbook4['bids'][0][0] if len (orderbook4['bids']) > 0 else None
        ask = orderbook4['asks'][0][0] if len (orderbook4['asks']) > 0 else None
        bid1 = orderbook4['bids'][1][0] if len (orderbook4['bids']) > 0 else None
        usdt = q * bid
        usdt1 = q1 * bid1
        if debug:
            print (symbol3,binance.id, 'market price', { 'bid': bid, 'ask': ask },usdt)
    else:
        orderbook4 = None
        usdt = 0
        usdt1 = 0

    symbol5 = 'ETH/BTC'
    orderbook5 = binance.fetch_order_book (symbol5,5)
    bid = orderbook5['bids'][0][0] if len (orderbook5['bids']) > 0 else None
    ask = orderbook5['asks'][0][0] if len (orderbook5['asks']) > 0 else None
    btc2 = eth * bid
    btc21 = eth1 * bid
    if debug:
        print (symbol5,binance.id, 'market price', { 'bid': bid, 'ask': ask },btc2,btc21)

    symbol6 = 'BNB/BTC'
    orderbook6 = binance.fetch_order_book (symbol6,5)
    bid = orderbook6['bids'][0][0] if len (orderbook6['bids']) > 0 else None
    ask = orderbook6['asks'][0][0] if len (orderbook6['asks']) > 0 else None
    btc3 = bnb * bid
    btc31 = bnb1 * bid
    if debug:
        print (symbol6,binance.id, 'market price', { 'bid': bid, 'ask': ask },btc3,btc31)

    symbol7= 'BTC/USDT'
    orderbook7 = binance.fetch_order_book (symbol7,5)
    bid = orderbook7['bids'][0][0] if len (orderbook7['bids']) > 0 else None
    ask = orderbook7['asks'][0][0] if len (orderbook7['asks']) > 0 else None
    btc4 = usdt / ask
    btc41 = usdt1 / ask
    if debug:
        print (symbol7,binance.id, 'market price', { 'bid': bid, 'ask': ask },btc4,btc41)

    
    return btc2,btc3,btc4,btc21,btc31,btc41

pro = 1.002
maxpro = 0;

def do_profit(x,r,base,r1):
    pp=(r-1)*100
    pp1=(r1-1)*100
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),x+'/'+base,pp,'%',pp1,'%')

#    if o1!=None:
#        print(o1['asks'])
#    if o2!=None:
#        print(o2['bids'])
    

debug1 = False

for i in range(1,2001):
    print (i)
    maxpro = 0;
    for x in symbols:
        [re,rb,ru,re1,rb1,ru1] =get3profits(x)
        if debug1:
            print (x,re,rb,ru)
        if re>pro:
            do_profit(x,re,'ETH',re1);
        if rb>pro:
            do_profit(x,rb,'BNB',rb1);
        if ru>pro:
            do_profit(x,ru,'USDT',ru1);

