from datetime import datetime
import MetaTrader5 as mt5
import math
import pandas as pd
from colorama import Fore
import time as tm

#Todas as listas
'lista de médias'
chindlershort=[]
chindlerlong=[]
chindlerave=[]

"Listas de tipos de Ordens"
listadeordemC = []
listadeordemV = []
listadeordemC1 = []
listadeordemV1= []

"Lista de IDs de ordens"
listadeID=[]

'Lista de ordens por nivel de Fibo'
lsfibo = []
lsfibo1 = []
lsfibo2 = []
lsfibo3 = []

"Lista de Ordens por nivel de Vwap"
Vwaplista1 = []
Vwaplista2 = []

"Lista de ordens Por nivel de Suporte e Resistencia"
Sup=[]
Res=[]

"Lista de ordens de Médias Móveis"
Malista=[]
Malista2=[]

"Lista de liberação de crédito por tipo de estrátegia"
'25%'
MAlis=0
'40%'
SupeReslista=0
'15%'
vwaplista=0
'20%'
fibolista=0


# variaveis globais
barras1 = 1000
minutoslast=0
calculo1=0
calculo2=0
calculo3=0
p=0
lot = 0.02

mt5.initialize()
ativo = 'BTCUSD'
time = mt5.TIMEFRAME_M1
laris = mt5.copy_rates_from(ativo, time, datetime.now(), 1)
Close = laris['close']


def FecharOrdem(lot, Tipo):
    print("Cheguei até aqui")

    if Tipo == "Compra":
        print("Compra")
        for hj in listadeordemV:

            position_id = hj
            price = mt5.symbol_info_tick(ativo).ask
            deviation = 20
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": ativo,
                "volume": lot,
                "type": mt5.ORDER_TYPE_BUY,
                "position": position_id,
                "price": price,
                "deviation": deviation,
                "magic": 234000,
                "comment": "python script close",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_IOC,
            }
            # enviamos a solicitação de negociação
            result = mt5.order_send(request)
            # verificamos o resultado da execução
            print("3. close position #{}: sell {} {} lots at {} with deviation={} points".format(position_id, ativo, lot,price, deviation))


        for hj in listadeordemV1:

            position_id = hj
            price = mt5.symbol_info_tick(ativo).ask
            deviation = 20
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": ativo,
                "volume": lot,
                "type": mt5.ORDER_TYPE_BUY,
                "position": position_id,
                "price": price,
                "deviation": deviation,
                "magic": 234000,
                "comment": "python script close",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_IOC,
            }
            # enviamos a solicitação de negociação
            result = mt5.order_send(request)
            # verificamos o resultado da execução
            print("3. close position #{}: sell {} {} lots at {} with deviation={} points".format(position_id, ativo, lot,price, deviation))

    if Tipo == "Venda":
        print("venda")
        for hj in listadeordemC:
            position_id = hj
            price = mt5.symbol_info_tick(ativo).bid
            deviation = 20
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": ativo,
                "volume": lot,
                "type": mt5.ORDER_TYPE_SELL,
                "position": position_id,
                "price": price,
                "deviation": deviation,
                "magic": 234000,
                "comment": "python script close",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_IOC,
            }
            # enviamos a solicitação de negociação
            result = mt5.order_send(request)
            # verificamos o resultado da execução
            print(
                "3. close position #{}: sell {} {} lots at {} with deviation={} points".format(position_id, ativo, lot,
                                                                                               price, deviation))
        for hj in listadeordemC1:
            position_id = hj
            price = mt5.symbol_info_tick(ativo).bid
            deviation = 20
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": ativo,
                "volume": lot,
                "type": mt5.ORDER_TYPE_SELL,
                "position": position_id,
                "price": price,
                "deviation": deviation,
                "magic": 234000,
                "comment": "python script close",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_IOC,
            }
            # enviamos a solicitação de negociação
            result = mt5.order_send(request)
            # verificamos o resultado da execução
            print(
                "3. close position #{}: sell {} {} lots at {} with deviation={} points".format(position_id, ativo, lot,
                                                                                               price, deviation))

def Pose(x):

    'retorna a ID'
    if x == 'ID':
        global id, tp
        hiu = mt5.positions_get(symbol=ativo)
        for hj2 in hiu:
            id = hj2[0]
            listadeID.append(id)

    'retorna as informações de posição para o CMD'
    if x == 'info':
        hiu = mt5.positions_get(symbol=ativo)
        print(Fore.RESET, "Total de Ordens:")
        global id2
        for hj2 in hiu:
            'profit'
            prof = hj2[15]
            'simbolo'
            Symb = hj2[16]
            'Preço de abertura'
            Prabt = hj2[10]
            'ID da operação'
            id2 = hj2[0]
            'tipo'
            tip=hj2[17]
            if prof < 0:
                print(Fore.RESET, f'Ativo:{Symb}' f' ID: {id2}' f' Preço de Abertura: {"{:.2f}".format(Prabt)}', Fore.RED,
                      f' Prejuizo {prof}', Fore.RESET,f' Tipo de Ordem {tip}')

            if prof > 0:
                print(Fore.RESET, f'Ativo:{Symb}' f' ID: {id2}' f' Preço de Abertura: {"{:.2f}".format(Prabt)}',
                      Fore.GREEN,
                      f' Lucro {prof}', Fore.RESET,f' Tipo de Ordem {tip}')

    "Retorna por lista e tipo de ordem"
    if x=="Tipo":
        hiu = mt5.positions_get(symbol=ativo)
        Malista.clear()

        for hj2 in hiu:
            "tipo"
            tp=hj2[17]
            "Id"
            id = hj2[0]

            if tp == "Media Movel":
                Malista.append(id)
                print(Malista)
'curta'
def SMAshort(y):
    chindlershort.clear()
    p=3
    x = 0
    n=0
    while x!= y:
         laris = mt5.copy_rates_from_pos(ativo, time,n, p)
         close = laris['close']
         'Fazer o calculo'
         calculo = sum(close) /3
         chindlershort.append("{:.0f}".format(calculo))

         n=n+1
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
    p=6
    x = 0
    n=0
    while x!=y:
        laris = mt5.copy_rates_from_pos(ativo, time, n, p)
        close = laris['close']
        calculo = sum(close) /6

        chindlerlong.append("{:.0f}".format(calculo))
        x = x + 1
        n = n + 1
    return chindlerlong

"Algoritmo para mandar Request de compra ou venda"
def Ordem(x,Tipo):
    global lot

    # Mandar Orderm compra
    if x == "Comprar":
        price = mt5.symbol_info_tick(ativo).ask
        deviation = 5
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": ativo,
            "volume": lot,
            "type": mt5.ORDER_TYPE_BUY,
            "price": price,
            "deviation": deviation,
            "magic": 234000,
            "comment": Tipo,
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }
        # enviamos a solicitação de negociação
        result = mt5.order_send(request)
        print("Ordem Enviada(): Para {} {} Quantidade em {} Com o Desvio={}".format(ativo, lot, price, deviation))
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print("2. order_send failed, retcode={}".format(result.retcode))
            # solicitamos o resultado na forma de dicionário e exibimos elemento por elemento
            result_dict = result._asdict()
            for field in result_dict.keys():
                print("   {}={}".format(field, result_dict[field]))
                # se esta for uma estrutura de uma solicitação de negociação, também a exibiremos elemento a elemento
                if field == "request":
                    traderequest_dict = result_dict[field]._asdict()
                    for tradereq_filed in traderequest_dict:
                        print("       traderequest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))

    if x == "Vender":
        # criamos uma solicitação de venda
        price = mt5.symbol_info_tick(ativo).bid
        deviation =5
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": ativo,
            "volume": lot,
            "type": mt5.ORDER_TYPE_SELL,
            "price": price,
            "deviation": deviation,
            "magic": 234000,
            "comment": Tipo,
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }
        # enviamos a solicitação de negociação
        result = mt5.order_send(request)
        print("Ordem Enviada(): Para {} {} Quantidade em {} Com o Desvio={}".format(ativo, lot, price, deviation))
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print("2. order_send failed, retcode={}".format(result.retcode))
            # solicitamos o resultado na forma de dicionário e exibimos elemento por elemento
            result_dict = result._asdict()
            for field in result_dict.keys():
                print("   {}={}".format(field, result_dict[field]))
                # se esta for uma estrutura de uma solicitação de negociação, também a exibiremos elemento a elemento
                if field == "request":
                    traderequest_dict = result_dict[field]._asdict()
                    for tradereq_filed in traderequest_dict:
                        print("       traderequest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))
    return
def Decisao(x,g):
    'Ele limpa a lista de ordens toda vez que é executado'
    listadeordemC1.clear()
    listadeordemV1.clear()
    hiu = mt5.positions_get(symbol=ativo)
    while len(hiu) != len(x):
        if len(hiu) != len(x):
            x.append(1)
    y = 0
    p = x

    if g == "Fake":
        if x == Malista:
            if p != "":
                for hj2 in hiu:
                    'profit'
                    prof = hj2[15]
                    'ID da operação'
                    id2 = hj2[0]
                    'compra ou venda'
                    Cv = hj2[5]
                    if p != "":
                        if id2 == p[y]:
                            if Cv == 0:
                                if prof < 0 or prof>0:
                                    listadeordemC1.append(id2)
                                    print(listadeordemC1)

                            if Cv == 1:
                                if prof < 0 or prof>0:
                                    listadeordemV1.append(id2)
                                    print(listadeordemV1)
                            y = y + 1

def Decisao1(x, g):
    'Ele limpa a lista de ordens toda vez que é executado'
    listadeordemC.clear()
    listadeordemV.clear()
    hiu = mt5.positions_get(symbol=ativo)
    while len(hiu) != len(x):
        if len(hiu) != len(x):
            x.append(1)
    y = 0
    p = x

    if g=="fake":

        if x == Malista:
            if p != "":
                for hj2 in hiu:
                    'profit'
                    prof = hj2[15]
                    'ID da operação'
                    id2 = hj2[0]
                    'compra ou venda'
                    Cv = hj2[5]
                    if p != "":
                        if id2 == p[y]:
                            if Cv == 0:
                                    listadeordemC.append(id2)
                                    print(listadeordemC)
                            if Cv == 1:
                                    listadeordemV.append(id2)
                                    print(listadeordemV)
                            y = y + 1

def BSMA(o):
    global MAlis
    ' fazer calculo de compra com média móvel para trades curtos e longos'

    SMAshort(5)
    SMAlong(5)
    confirmacao = 0
    confirmacao2 = 0
    confirmation = 0
    y = 0

    if o == "Entrada":
        'se a média móvel curta estiver abaixo da média móvel longa '
        'fazer uma lista de confirmação'
        for x in chindlershort:

            if x < chindlerlong[y]:
                confirmacao = confirmacao + 1

            elif x > chindlerlong[y]:
                confirmacao2 = confirmacao2 + 1


            y = y + 1



        if chindlerlong[0]==chindlershort[0]:
                confirmation=confirmation+1
        if chindlerlong[0]!=chindlershort[0]:
                confirmation=confirmation+1


        MAlis=MAlis-1
        confirmacao=confirmacao+confirmation
        confirmacao2 = confirmacao2 + confirmation

        if confirmacao2 == 5:
            Ordem('Vender', "Media Movel")

        if confirmacao == 5:
            Ordem('Comprar', "Media Movel")

    if o == "Saida":
        Pose("Tipo")
        Decisao1(Malista,'normal')
        FecharOrdem(lot, 'Venda')
        FecharOrdem(lot, 'Compra')


def FechaBSMAFake():
    SMAshort(1)
    SMAlong(1)
    'se a ordem for do tipo compra então ela vende acima da média longa'
    'se o profit for negativo e a media curta estiver acima da média longa, então ele fechaa compra'
    if SMAshort(1)<SMAlong(1):
        Pose("Tipo")
        Decisao(Malista,"Fake")
        print(listadeordemC1)
        if listadeordemC1!="":
            FecharOrdem(lot,"Compra")

    'se a ordem for do tipo venda então ela compra abaixo  da média longa'
    'se o profit for negativo e a media curta estiver acima da média longa, então ele fechaa venda'
    if SMAshort(1) > SMAlong(1):
        Pose("Tipo")
        Decisao(Malista, "Fake")
        print(listadeordemV1)
        if listadeordemV1!="":
            FecharOrdem(lot,"Venda")



class Desvio:

    def DesvioPadrao(self,x):
        global dp
        self.x=x
        barras = len(x)
        dp = 0
        xola = 0
        mda = sum(x) / len(x)
        print("Mda",mda)
        for gh in x:
            lobis = (gh - mda) ** 2
            xola = (lobis) + xola
            print(mda)
        n = barras
        dp = xola / n
        dp = math.sqrt(dp)
        return dp

    def Variancia(self, x):
        'Quanto menor é a variância, mais próximos os valores estão da média; mas quanto maior ela é, mais os valores estão distantes da média'
        global V
        self.x = x
        barras = len(x)
        xola = 0
        mda = sum(x) / len(x)
        for gh in x:
            lobis = (gh - mda) ** 2
            xola = (lobis)+ xola
            print(mda)
        n = barras
        V = xola / n

        return V



#laris = mt5.copy_rates_from(ativo, time, datetime.now(), 5)
#close1 = laris['close']
#print(close1)
#price = mt5.symbol_info_tick(ativo).ask
#hj=Desvio().DesvioPadrao(close1)
#hj1=Desvio().Variancia(close1)
#print("Desvio padrão", hj)
#print("Variancia", hj1)
#tm.sleep(2)
#Ordem('Comprar','Media Movel')
#Ordem('Vender','Media Movel')
#tm.sleep(2)
#BSMA("Saida")
#Pose("Tipo")
#Decisao1(Malista, 'Normal')
#FecharOrdem(lot, 'Venda')

#FechaBSMAFake()

 if confirmacao2 == 1 and chindlershort[-1]< chindlerlong[-1]:
            print("YYYYYYY")
        if confirmacao == 1 and chindlershort[-1] > chindlerlong[-1]:
            print("XXXXXX")

SMAshort(25)
SMAlong(25)
print(chindlershort)
print(chindlerlong)
