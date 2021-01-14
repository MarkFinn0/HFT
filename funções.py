from datetime import datetime
import MetaTrader5 as mt5
import math
import pandas as pd
from colorama import Fore
import time as tm

mt5.initialize()
ativo = 'BTCUSD'
time = mt5.TIMEFRAME_M1
laris = mt5.copy_rates_from(ativo, time, datetime.now(), 1)
Close = laris['close']
lot = 0.01

'Cógigo de compra e venda com o Fibbonaci'
def BSFibo(Y):
    global fibolista
    'x é o ultimo preço'
    Fibbonacci()
    laris = mt5.copy_rates_from(ativo, time, datetime.now(), 1)
    x = laris["close"]

    "ordens de abertura "
    if Y == "Entrada":
        if x >= V1:
            'manda ordem'
            Ordem("Vender",'Fibo')
        if x <= V2:
            Ordem("Comprar","Fibo1")
        if x >= V3:
            Ordem("Vender","Fibo2")
        if x >= V4:
            Ordem("Vender","Fibo3")

    fibolista = fibolista-1

    'ordens de fechamento'

    if Y == "Saida":
        if x >= V1:
            'Acessa a lista e decide'
            Decisao(lsfibo3)
            FecharOrdem(lot, "Venda")

        if x <= V2:
            'Acessa a lista e decide'
            Decisao(lsfibo)
            FecharOrdem(lot, "Compra")

        if x >= V3:
            'Acessa a lista e decide'
            Decisao(lsfibo1)
            FecharOrdem(lot, "Venda")

        if x >= V4:
            'Acessa a lista e decide'
            Decisao(lsfibo2)
            FecharOrdem(lot, "Compra")


'Cógigo de compra e venda com o VWAP'
def BSvwap(X):
    global vwaplista
    laris = mt5.copy_rates_from(ativo, time, datetime.now(), 1)
    x = laris['close']
    VWAP()
    if X == "Entrada":
        if x >= eq:
            Ordem("Vender",'VwapH')

        if x <= eq:
            Ordem("Comprar",'VwapL')
    vwaplista =vwaplista-1

    if X == "Saida":
        if x >= eq:
            Decisao(Vwaplista2)
            FecharOrdem(lot, "Vender")

        if x <= eq:
            Decisao(Vwaplista1)
            FecharOrdem(lot, "Comprar")


'Cógigo de compra e venda com o Suporte e Resistencia'
def BSSupeRes(Tipo):
    global SupeReslista
    laris = mt5.copy_rates_from(ativo, time, datetime.now(), 1)
    U = laris['close']
    laris3 = mt5.copy_rates_from(ativo, time, datetime.now(),200)
    close3 = laris3['close']
    SupeRes().Res(close3)
    SupeRes().Med(close3)
    SupeRes().Sup(close3)
    "Entrada"
    if Tipo=="Entrada":
        if U >= la or  U>k:
            Ordem("Vender","Res")

        if U <= lo or U<k:
            Ordem("Comprar","Supo")
    SupeReslista=SupeReslista-1

    "Saida"
    if Tipo=="Saida":
            Pose("Tipo")
            Decisao(Sup)
            FecharOrdem(lot, "Venda")
            Decisao(Res)
            FecharOrdem(lot, "Compra")

"Médias Móveis"

'curta'
def SMAshort(y):
    chindlershort.clear()
    p=9
    x = 0
    while x!= y:
         laris = mt5.copy_rates_from_pos(ativo, time,x, p)
         close = laris['close']
         'Fazer o calculo'
         calculo = sum(close) /9
         chindlershort.append("{:.2f}".format(calculo))
         x = x + 1
    return chindlershort

'media'
def SMAave(y):
    chindlerave.clear()
    p=34
    x = 0
    while x != y:
        laris = mt5.copy_rates_from_pos(ativo, time, x, p)
        close = laris['close']
        calculo = sum(close) /34
        chindlerave.append(calculo)
        x = x + 1
    return chindlerave

'longa'
def SMAlong(y):
    chindlerlong.clear()
    p=34
    x = 0
    while x!=y:
        laris = mt5.copy_rates_from_pos(ativo, time, x, p)
        close = laris['close']
        calculo = sum(close) /34
        chindlerlong.append("{:.2f}".format(calculo))
        x = x + 1
    return chindlerlong


confirmacao = 0
    confirmacao2 = 0
    confirmation = 0
    y = 0


    if o == "Entrada":
        SMAshort(5)
        SMAlong(5)
        'se a média móvel curta estiver abaixo da média móvel longa '
        'fazer uma lista de confirmação'
        for x in chindlershort:

            if x < chindlerlong[y]:
                confirmacao = confirmacao + 1

            elif x > chindlerlong[y]:
                confirmacao2 = confirmacao2 + 2
            y = y + 1

        if chindlerlong[0]==chindlershort[0]:
                confirmation=confirmation+2

        if chindlerlong[0]!=chindlershort[0]:
                confirmation=confirmation+15



        MAlis=MAlis-1
        confirmacao = confirmacao + confirmation
        confirmacao2 = confirmacao2 + confirmation

        if confirmacao2 == 10:
            Ordem('Vender', "Media Movel")

        if confirmacao == 6:
            Ordem('Comprar', "Media Movel")