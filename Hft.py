import MetaTrader5 as mt5
from datetime import datetime
from colorama import Fore
import math
import time as tm

mt5.initialize()

#Entrada de informações da para negociação
mexi=mt5.account_info()
laranja=mexi[24]
abacaxi=mexi[1]
print(Fore.LIGHTMAGENTA_EX,f'Bem Vindo  {laranja}!' '\n')

if abacaxi==0:
    print(Fore.RED, 'ESTÁ CONTA É MODO DEMO')
if abacaxi==2:
    print(Fore.RED, 'ESTÁ CONTA É MODO REAL')
if abacaxi==1:
    print(Fore.RED, 'ESTÁ CONTA É MODO CONTEST')

'nome do ativo'
print(Fore.CYAN,'Coloque o nome do Ativo:')
fh=input()
print('\n')
ativo=fh.upper()
'frame da cotação(dias,horas ou minutos)'
time = mt5.TIMEFRAME_M15


# informações de cotação do ativo e da conta'
"Algumas informações sobre Margem, alavancagem e equity"
def Mar_Bala_equi():
    global alavancagem
    global balanco
    global marginused
    global marginfree
    global equity
    mex = mt5.account_info()
    alavancagem = mex[2]
    balanco = mex[10]
    marginused = mex[14]
    marginfree = mex[15]
    equity = mex[13]


"Calculadora de Margem"
def CalcQntpMarg(close):
    global QntEntr
    Mar_Bala_equi()
    'fazer calculo de margem levando em consideração o dinheiro da conta e alavancagem'
    'apresenta quantas ordens consegue mandar conforme a margem do ativo eo saldo da conta'
    x=mt5.order_calc_margin(mt5.ORDER_TYPE_BUY, ativo, 0.01, close)
    qntd=marginfree/x
    QntEntr=round(qntd)
    return QntEntr


'gerenciador de ordem Libera Créditos para negociação'
def GerdOrd():
    global MAlis
    global SupeReslista
    global vwaplista
    global fibolista

    laris = mt5.copy_rates_from(ativo, time, datetime.now(), 1)
    Close = laris['close']

    CalcQntpMarg(Close)
    'Separa créditos de compra por tipo de estrátegia'
    'lista de créditos'

    '25%'
    MAlis=0
    '40%'
    SupeReslista=0
    '15%'
    vwaplista=0
    '20%'
    fibolista=0

    if QntEntr!=0:

        X1=round(QntEntr*0.6)

        if X1>0:
            MAlis=X1



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
        Malista.clear()
        hiu = mt5.positions_get(symbol=ativo)

        for hj2 in hiu:
            "tipo"
            tp=hj2[17]
            "Id"
            id = hj2[0]

            if tp == "Media Movel":
                Malista.append(id)



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
lot = 0.01
barreira=0



#Algoritmos de análise
"Calculo de Preço ponderado ao Volume Medio"
def VWAP():
    'Quando o preço está a baixo da VWAP é melhor fazer pequenas posições, quando está acima é melhor fazer longas operações'
    'EQUAÇÃO:'
    "VWAP=∑p*V/∑V"
    global eq
    laris = mt5.copy_rates_from(ativo, time, datetime.now(), 100)
    Close= laris['close']
    laris = mt5.copy_rates_from(ativo, time, datetime.now(), 100)
    Volume = laris['tick_volume']
    Sp=sum(Close)
    Sv=sum(Volume)
    eq=Sp+Sv/Sv
    return eq

"Calculo de Faixas de preço com Fibonnaci"
def Fibbonacci():
    "Fibonacci"
    'Equação:'
    'High-low=Diferença( Traçar levels com numeros Fibonacci. Ex:0.236, 0.382, 0.618, 1.618, 2.618, 4.236(tambem são usados: 0.5, 1.0, and 2.0)'
    'Traçar levels=diferença x numeros fibonacci'

    global V1,V2,V3,V4
    laris = mt5.copy_rates_from(ativo, time, datetime.now(), 100)
    Close = laris['close']
    Xh=max(Close)
    Xl=min(Close)
    Dif=Xh-Xl
    V1=Xh
    V2=Xl
    V3=Xh-(Dif*0.5)
    V4=Xh-(Dif*0.236)
    return V1,V2,V3,V4

"Médias Móveis"

'curta'
def SMAshort(y):
    chindlershort.clear()
    p=9
    x = 0
    n=0
    while x!= y:
         laris = mt5.copy_rates_from_pos(ativo, time,n, p)
         close = laris['close']
         'Fazer o calculo'
         calculo = sum(close) /9
         chindlershort.append("{:.2f}".format(calculo))
         n=n+1
         x = x + 1
    return chindlershort

'media'
def SMAave(y):
    chindlerave.clear()
    p=3
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
    n=0
    while x!=y:
        laris = mt5.copy_rates_from_pos(ativo, time, n, p)
        close = laris['close']
        calculo = sum(close) /34
        chindlerlong.append("{:.2f}".format(calculo))
        x = x + 1
        n = n + 1
    return chindlerlong


"Função de Desvio Padrão e Variancia"
class Desvio:

    def DesvioPadrao(self,x):
        global dp
        self.x=x
        barras = len(x)
        dp = 0
        xola = 0
        mda = sum(x) / len(x)

        for gh in x:
            lobis = (gh - mda) ** 2
            xola = lobis + xola
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
            xola = lobis + xola
        n = barras
        V = xola / n

        return V

    def Media(self, x):
        global M
        self.x = x
        barras = len(x)
        xola = 0
        M = sum(x) / len(x)
        return M

"Suporte e Resistencia"
class SupeRes:

    def Res(self,lista):
        global la
        self.lista=lista
        la=max(lista)
        "{:.2f}".format(la)

        return la

    def Sup(self,lista):
        global lo
        self.lista = lista
        lo = min(lista)
        "{:.2f}".format(lo)

        return lo

    def Med(self,lista):
        global k
        self.lista = lista
        pa=max(lista)
        po=min(lista)
        k=(pa+po)/2
        "{:.2f}".format(k)

        return k



#Estrátegias de compra e venda e análise

"Calculadora de Stop Loss"
def CalcStpLoss(x):
    if x=='Stop de Compra':
        global Stoploss1
        'Stop loss com Desvio padrão'
        laris = mt5.copy_rates_from(ativo, time, datetime.now(), 200)
        close1 = laris['close']
        price = mt5.symbol_info_tick(ativo).ask
        point = mt5.symbol_info(ativo).point
        Desvio().DesvioPadrao(close1)
        Stoploss1 = price -dp
        return Stoploss1

    if x=='Stop de Venda':
        global Stoploss
        'Stop loss com Desvio padrão'
        laris = mt5.copy_rates_from(ativo, time, datetime.now(), 200)
        close1 = laris['close']
        price = mt5.symbol_info_tick(ativo).bid
        point = mt5.symbol_info(ativo).point
        Desvio().DesvioPadrao(close1)
        Stoploss = price + dp
        return Stoploss

"Algoritmo de Fechamento de Ordem"
def FecharOrdem(lot, Tipo):

    if Tipo == "Compra":
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
            print("3. close position #{}: sell {} {} lots at {} ".format(position_id, ativo, lot,price, ))

    if Tipo == "Venda":
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
                "3. close position #{}: sell {} {} lots at {} ".format(position_id, ativo, lot,
                                                                                               price))


"Decide se fecha uma operação ou não"


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

    if g=="normal":

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
                                if prof >=1.6:
                                    listadeordemC.append(id2)

                            if Cv == 1:
                                if prof >=1.5:
                                    listadeordemV.append(id2)
                            y = y + 1

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

                            if Cv == 1:
                                    listadeordemV.append(id2)
                            y = y + 1



"Algoritmo para mandar Request de compra ou venda"
def Ordem(x,Tipo):
    global lot

    # Mandar Orderm compra
    if x == "Comprar":
        price = mt5.symbol_info_tick(ativo).ask
        CalcStpLoss('Stop de Compra')
        st=Stoploss1
        deviation = 5
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": ativo,
            "volume": lot,
            "type": mt5.ORDER_TYPE_BUY,
            "price": price,
            "sl":st,
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
        CalcStpLoss('Stop de Venda')
        st = Stoploss
        deviation =5
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": ativo,
            "volume": lot,
            "type": mt5.ORDER_TYPE_SELL,
            "price": price,
            "sl": st,
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



#Códigos de Compra e Venda das Estrátegias
'Cógigo de compra e venda com o Média Móvel'
def BSMA(o):
    global MAlis
    ' fazer calculo de compra com média móvel para trades curtos e longos'
    chindlerlong.clear()
    chindlershort.clear()
    confirmacao = 0
    confirmacao2 = 0
    y = 0

    if o=="Entrada":
        SMAshort(25)
        SMAlong(25)

        for x in chindlershort:

            if x < chindlerlong[y]:
                confirmacao = confirmacao + 1
            elif x > chindlerlong[y]:
                confirmacao2 = confirmacao2 + 1
            y = y + 1

        if confirmacao2 == 4 and chindlershort[0]< chindlerlong[0]:
            Ordem('Vender', "Media Movel")
        if confirmacao == 4 and chindlershort[0] > chindlerlong[0]:
            Ordem('Comprar', "Media Movel")


    if o == "Saida":
        Pose("Tipo")
        Decisao1(Malista,'normal')
        FecharOrdem(lot, 'Venda')
        FecharOrdem(lot, 'Compra')

def CloseFake():
    chindlerlong.clear()
    chindlershort.clear()
    SMAshort(1)
    SMAlong(1)

    confirmacao = 0
    confirmacao2 = 0

    y = 0

    for x in chindlershort:

        if x < chindlerlong[y]:
            confirmacao = confirmacao + 1

        elif x > chindlerlong[y]:
            confirmacao2 = confirmacao2 + 1
        elif x == chindlerlong[y]:
            confirmacao = confirmacao + 3
            confirmacao2 = confirmacao2 + 3


        y = y + 1

    if confirmacao2 == 1:
        Pose("Tipo")
        Decisao1(Malista, 'fake')
        FecharOrdem(lot, 'Compra')
    if confirmacao == 1:
        Pose("Tipo")
        Decisao1(Malista, 'fake')
        FecharOrdem(lot, 'Venda')

#Orientação Estruturada Com looping

"Looper de Análise"
horas = datetime.now().__getattribute__('hour')
laris3 = mt5.copy_rates_from(ativo, time, datetime.now(),100)
close3 = laris3['close']
SupeRes().Res(close3)
SupeRes().Med(close3)
SupeRes().Sup(close3)


while horas!=19:
    minutos = datetime.now().__getattribute__('minute')
    segundos=datetime.now().__getattribute__('second')
    laris3 = mt5.copy_rates_from(ativo, time, datetime.now(),1)
    close1 = laris3['close']

    "O looping precisa atualizar as listas de tipo"

    Pose("Tipo")
    if Malista!="":
        BSMA('Saida')
        CloseFake()

    if minutos == 30 or minutos == 0:
        SupeRes().Res(close3)
        SupeRes().Med(close3)
        SupeRes().Sup(close3)


    print(Fore.RESET, 'Preço de Fechamento:', close1, '| Horário: ', horas, ':', minutos, ':', segundos)
    print(Fore.YELLOW, f"Resistência {la}")
    print(Fore.CYAN, f"Mediana {k}")
    print(Fore.MAGENTA, f"Suporte {lo}")
    Pose('info')

    "Looping de Ordens Conforme os créditos"
    Pose("Tipo")

    BSMA('Entrada')
