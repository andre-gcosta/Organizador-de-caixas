
##=========================   Bibliotecas   ============================##

import time
from flask import Flask, render_template
import datetime
import time

##========================   Configurações   ===========================##
 
mem=0##Memória numerica
ms=0 ##Casas de memoria utilizada

aux1=0##|Auxiliares de seleção
aux2=0##|
aux3=0##|
aux4=0##|

aux5=0##|Auxiliares de avanço cil
aux6=0##|
aux7=0##|
aux8=0##|

mod=0##|Variável Seleção Modo
vc1=0##|Variáveis acionadas pela internet (manual)
vc2=0##|
vc3=0##|
vc4=0##|
vm1=0##|
vm2=0##|
vbot=0#|

mmem="0"##|Variáveis lidas pela internet (mensagens)
mms="0"##|
mc1="Desligado"##|
mc2="Desligado"##|
mc3="Desligado"##|
mc4="Desligado"##|
mm1="Desligado"##|
mm2="Desligado"##|
mmt="Nenhum registro"##|
mcindv1="0"##|
mcindv2="0"##|
mcindv3="0"##|
mcindv4="0"##|
mctotal="0"##|
mtime="Calculando..."##|
mrot1=""##|
mrot2=""##|
mcil1=""##|
mcil2=""##|
mcil3=""##|
mcil4=""##|
mcolor1=""##|
mcolor2=""##|
mcolor3=""##|
mcolor4=""##|
mcolor5=""##|
mcolor6=""##|
mcolor7=""##|
mcaixa1=""##|
mcaixa2=""##|
mcaixa3=""##|
mcaixa4=""##|
mcaixa5=""##|
mcaixa6=""##|
mcaixa7=""##|
mcaixa8=""##|
mcaixa9=""##|
mcaixa10=""##|

sensor_baixo=0##|Sensores de material
sensor_alto=0 ##|
sensor_metal=0##|

sc1=0##|Sensores de avanço cil
sc2=0##|
sc3=0##|
sc4=0##|

sensor_avanco_cilindro_01=0##|Sensores de avanço cilindro
sensor_avanco_cilindro_02=0##|
sensor_avanco_cilindro_03=0##|
sensor_avanco_cilindro_04=0##|

cilindro_01 = (False)##|Cilindros
cilindro_02 = (False)##|
cilindro_03 = (False)##|
cilindro_04 = (False)##|

motor_01 = (False)##|Motores
motor_02 = (False)##|

c1=0##|Auxiliares Cilindros
c2=0##|
c3=0##|
c4=0##|

m1=0##|Auxiliares Motores
m2=0##|

auxmod1=0##| Auxiliar modo manual
auxmod2=0
auxmod3=0
auxmod4=0

cn=0##| Auxiliares caixa
cr=0##|

t1=0##|Timers
t2=0##|
t3=0##|
t4=0##|
tp=0##|

cindv1=0##|Contadores
cindv2=0##|
cindv3=0##|
cindv4=0##|
ctotal=0##|
crot=1##|

bot=0##Botão emergência físico

##===========================   Timers   ==========================##
       
def timer1():
    global t1
    global cr
    time.sleep(0.001)
    t1=t1+1
    print('t1=')
    print(t1)
    if (t1==4):
        cr=cr+1
        times1()
    if (t1==6):
        t1=0
        timet1()
def times1():
    global t1
    global m1
    global m2
    global c1
    global cindv1
    global ctotal
    global mcindv1
    global mctotal
    cindv1=cindv1+1
    ctotal=ctotal+1
    mcindv1=str(cindv1)
    mctotal=str(ctotal)
    print('acionamento cilindro 1')
    motor_01 = (False)
    motor_02 = (False)
    cilindro_01 = (True)
    m1=0
    m2=0
    c1=1
def timet1():
    global t1
    global m1
    global m2
    global c1
    print('retorno cilindro 1')
    cilindro_01 = (False)
    motor_01 = (True)
    motor_02 = (True)
    c1=0
    m1=1
    m2=1
    t1=0

def timer2():
    global t2
    global cr
    time.sleep(0.001)
    t2=t2+1
    print('t2=')
    print(t2)
    if (t2==4):
        cr=cr+1
        times2()
    if (t2==6):
        t2=0
        timet2()
def times2():
    global t2
    global m1
    global m2
    global c2
    global cindv2
    global ctotal
    global mcindv2
    global mctotal
    cindv2=cindv2+1
    ctotal=ctotal+1
    mcindv2=str(cindv2)
    mctotal=str(ctotal)
    print('acionamento cilindro 2')
    motor_01 = ( False)
    motor_02 = (False)
    cilindro_02 = (True)
    m1=0
    m2=0
    c2=1
def timet2():
    global t2
    global m1
    global m2
    global c2
    print('retorno cilindro 2')
    cilindro_02 = (False)
    motor_01 = (True)
    motor_02 = (True)
    m1=1
    m2=1
    c2=0
    t2=0

def timer3():
    global t3
    global cr
    time.sleep(0.001)
    t3=t3+1
    print('t3=')
    print(t3)
    if (t3==4):
        cr=cr+1
        times3()
    if (t3==6):
        t3=0
        timet3()
def times3():
    global t3
    global m1
    global m2
    global c3
    global cindv3
    global ctotal
    global mcindv3
    global mctotal
    cindv3=cindv3+1
    ctotal=ctotal+1
    mcindv3=str(cindv3)
    mctotal=str(ctotal)
    print('acionamento cilindro 3')
    motor_01 = (False)
    motor_02 = (False)
    cilindro_03 = (True)
    m1=0
    m2=0
    c3=1
def timet3():
    global t3
    global m1
    global m2
    global c3
    print('retorno cilindro 3')
    cilindro_03 = (False)
    motor_01 = (True)
    motor_02 = (True)
    m1=1
    m2=1
    c3=0
    t3=0

def timer4():
    global t4
    global cr
    time.sleep(0.001)
    t4=t4+1
    print('t4=')
    print(t4)
    if (t4==4):
        cr=cr+1
        times4()
    if (t4==6):
        t4=0
        timet4()
def times4():
    global t4
    global m1
    global m2
    global c4
    global cindv4
    global ctotal
    global mcindv4
    global mctotal
    cindv4=cindv4+1
    ctotal=ctotal+1
    mcindv4=str(cindv4)
    mctotal=str(ctotal)
    print('acionamento cilindro 4')
    motor_02 = (False)
    motor_01 = (False)
    cilindro_04 = (True)
    m1=0
    m2=0
    c4=1
def timet4():
    global t4
    global m1
    global m2
    global c4
    print('retorno cilindro 4')
    cilindro_04 = (False)
    motor_01 = (True)
    motor_02 = (True)
    m1=1
    m2=1
    c4=0
    t4=0

while True:
    ##=======================   Rotina HTML   ========================##
    app = Flask(__name__)
    @app.route("/user")
    def user():
        templateData={
        }
        return render_template('user.html', **templateData)
    @app.route("/main")
    def main():
        global mod
        mod=0
        prog()
        templateData={
            'mem':mmem,
            'ms':mms,
            'mmt':mmt,
            'mtime':mtime
        }
        return render_template('main.html', **templateData)
    @app.route("/mod2")
    def mod2():
        global mod
        global vbot
        global mmem
        global mms
        global mmt
        global mcindv1
        global mcindv2
        global mcindv3
        global mcindv4
        global mctotal
        global cindv1
        global cindv2
        global cindv3
        global cindv4
        global ctotal
        global mtime
        global mc1
        global mc2
        global mc3
        global mc4
        global mm1
        global mm2
        global crot
        global mrot1
        global mrot2
        global mcil1
        global mcil2
        global mcil3
        global mcil4
        global mcaixa1
        global mcaixa2
        global mcaixa3
        global mcaixa4
        global mcaixa5
        global mcaixa6
        global mcaixa7
        global mcaixa8
        global mcaixa9
        global mcaixa10
        global cn
        global mcolor7
        global ms
        global vc1
        global vc2
        global vc3
        global vc4
        global vm1
        global vm2
        global cr
        mod=2
        print(ms)
        print(cn)
        crot=crot+1
        if (crot==4):
            crot=1
        if (vm1==1):
            if (crot==1):
                mrot1="rot1-green.png"
            if (crot==2):
                mrot1="rot2-green.png"
            if (crot==3):
                mrot1="rot3-green.png"
            if (crot==4):
                mrot1="rot4-green.png"
        if (vm2==1):
            if (crot==1):
                mrot2="rot1-green.png"
            if (crot==2):
                mrot2="rot2-green.png"
            if (crot==3):
                mrot2="rot3-green.png"
            if (crot==4):
                mrot2="rot4-green.png"
        if (vm1==0):
            mrot1="green.png"
        if (vm2==0):
            mrot2="green.png"
        if (vc1==1):
            mcil1="cil-acionado-green.jpg"
        if (vc1==0):
            mcil1="cil-desacionado-green.jpg"
        if (vc2==1):
            mcil2="cil-acionado-green.jpg"
        if (vc2==0):
            mcil2="cil-desacionado-green.jpg"
        if (vc3==1):
            mcil3="cil-acionado-green.jpg"
        if (vc3==0):
            mcil3="cil-desacionado-green.jpg"
        if (vc4==1):
            mcil4="cil-acionado-green.jpg"
        if (vc4==0):
            mcil4="cil-desacionado-green.jpg"
        if (ms==0):
            mcaixa1="green.png"
            mcaixa2="green.png"
            mcaixa3="green.png"
            mcaixa4="green.png"
            mcaixa5="green.png"
            mcaixa6="green.png"
            mcaixa7="green.png"
            mcaixa8="green.png"
            mcaixa9="green.png"
            mcaixa10="green.png" 
        print(cr)
        if (ms==1):
            if (cn==1):
                mcaixa1="caixa-madeirabaixa.png"
                ####
            if (cn==2):
                mcaixa1="caixa-madeiraalta.png"
                
            if (cn==3):
                mcaixa1="caixa-metalbaixa.png"
                
            if (cn==4):
                mcaixa1="caixa-metalalta.png"
                
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2="green.png"
                cr=cr-1### tentar arrumar o bug fazendo o cr ate 10
        if (ms==2):
            if (cn==1):
                mcaixa2="caixa-madeirabaixa.png"
                cn=0
            if (cn==2):
                mcaixa2="caixa-madeiraalta.png"
                cn=0
            if (cn==3):
                mcaixa2="caixa-metalbaixa.png"
                cn=0
            if (cn==4):
                mcaixa2="caixa-metalalta.png"
                cn=0
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3="green.png"
                cr=cr-1
        if (ms==3): 
            if (cn==1):
                mcaixa3="caixa-madeirabaixa.png"
                cn=0
            if (cn==2):
                mcaixa3="caixa-madeiraalta.png"
                cn=0
            if (cn==3):
                mcaixa3="caixa-metalbaixa.png"
                cn=0
            if (cn==4):
                mcaixa3="caixa-metalalta.png"
                cn=0
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3=mcaixa4
                mcaixa4="green.png"
                cr=cr-1            
        if (ms==4):
            if (cn==1):
                mcaixa4="caixa-madeirabaixa.png"
                cn=0
            if (cn==2):
                mcaixa4="caixa-madeiraalta.png"
                cn=0
            if (cn==3):
                mcaixa4="caixa-metalbaixa.png"
                cn=0
            if (cn==4):
                mcaixa4="caixa-metalalta.png"
                cn=0
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3=mcaixa4
                mcaixa4=mcaixa5
                mcaixa5="green.png"
                cr=cr-1
        if (ms==5):
            if (cn==1):
                mcaixa5="caixa-madeirabaixa.png"
                cn=0
            if (cn==2):
                mcaixa5="caixa-madeiraalta.png"
                cn=0
            if (cn==3):
                mcaixa5="caixa-metalbaixa.png"
                cn=0
            if (cn==4):
                mcaixa5="caixa-metalalta.png"
                cn=0
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3=mcaixa4
                mcaixa4=mcaixa5
                mcaixa5=mcaixa6
                mcaixa6="green.png"
                cr=cr-1
        if (ms==6):           
            if (cn==1):
                mcaixa6="caixa-madeirabaixa.png"
                cn=0
            if (cn==2):
                mcaixa6="caixa-madeiraalta.png"
                cn=0
            if (cn==3):
                mcaixa6="caixa-metalbaixa.png"
                cn=0
            if (cn==4):
                mcaixa6="caixa-metalalta.png"
                cn=0
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3=mcaixa4
                mcaixa4=mcaixa5
                mcaixa5=mcaixa6
                mcaixa6=mcaixa7
                mcaixa7="green.png"
                cr=cr-1
        if (ms==7):
            if (cn==1):
                mcaixa7="caixa-madeirabaixa.png"
                cn=0
            if (cn==2):
                mcaixa7="caixa-madeiraalta.png"
                cn=0
            if (cn==3):
                mcaixa7="caixa-metalbaixa.png"
                cn=0
            if (cn==4):
                mcaixa7="caixa-metalalta.png"
                cn=0
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3=mcaixa4
                mcaixa4=mcaixa5
                mcaixa5=mcaixa6
                mcaixa6=mcaixa7
                mcaixa7=mcaixa8
                mcaixa8="green.png"
                cr=cr-1
        if (ms==8):
            if (cn==1):
                mcaixa8="caixa-madeirabaixa.png"
            if (cn==2):
                mcaixa8="caixa-madeiraalta.png"
            if (cn==3):
                mcaixa8="caixa-metalbaixa.png"
            if (cn==4):
                mcaixa8="caixa-metalalta.png"
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3=mcaixa4
                mcaixa4=mcaixa5
                mcaixa5=mcaixa6
                mcaixa6=mcaixa7
                mcaixa7=mcaixa8
                mcaixa8=mcaixa9
                mcaixa9="green.png"
                cr=cr-1
        if (ms==9):
            mcaixa10="green.png"
            if (cn==1):
                mcaixa9="caixa-madeirabaixa.png"
                cn=0
            if (cn==2):
                mcaixa9="caixa-madeiraalta.png"
                cn=0
            if (cn==3):
                mcaixa9="caixa-metalbaixa.png"
                cn=0
            if (cn==4):
                mcaixa9="caixa-metalalta.png"
                cn=0
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3=mcaixa4
                mcaixa4=mcaixa5
                mcaixa5=mcaixa6
                mcaixa6=mcaixa7
                mcaixa7=mcaixa8
                mcaixa8=mcaixa9
                mcaixa9=mcaixa10
                mcaixa10="green.png"
                cr=cr-1
        if (ms==10):
            if (cn==1):
                mcaixa10="caixa-madeirabaixa.png"
                cn=0
            if (cn==2):
                mcaixa10="caixa-madeiraalta.png"
                cn=0
            if (cn==3):
                mcaixa10="caixa-metalbaixa.png"
                cn=0
            if (cn==4):
                mcaixa10="caixa-metalalta.png"
                cn=0
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3=mcaixa4
                mcaixa4=mcaixa5
                mcaixa5=mcaixa6
                mcaixa6=mcaixa7
                mcaixa7=mcaixa8
                mcaixa8=mcaixa9
                mcaixa9=mcaixa10
                cr=cr-1
        if (vm1==1 and vm2==1):
            mcolor7="lime"
        if (vm1==0 and vm2==0):
            mcolor7="red"
        print('entro mod2')
        prog()
        templateData={
            'mem':mmem,
            'ms':mms,
            'mmt':mmt,
            'mcindv1':mcindv1,
            'mcindv2':mcindv2,
            'mcindv3':mcindv3,
            'mcindv4':mcindv4,
            'mctotal':mctotal,
            'mtime':mtime,
            'mc1':mc1,
            'mc2':mc2,
            'mc3':mc3,
            'mc4':mc4,
            'mm1':mm1,
            'mm2':mm2,
            'mrot1':mrot1,
            'mrot2':mrot2,
            'mcil1':mcil1,
            'mcil2':mcil2,
            'mcil3':mcil3,
            'mcil4':mcil4,
            'mcaixa1':mcaixa1,
            'mcaixa2':mcaixa2,
            'mcaixa3':mcaixa3,
            'mcaixa4':mcaixa4,
            'mcaixa5':mcaixa5,
            'mcaixa6':mcaixa6,
            'mcaixa7':mcaixa7,
            'mcaixa8':mcaixa8,
            'mcaixa9':mcaixa9,
            'mcaixa10':mcaixa10,
            'mcolor7':mcolor7
        }
        return render_template('mod2.html', **templateData)
    @app.route("/vbotd")
    def vbotd():
        global mod
        global vbot
        global mmem
        global mms
        global mmt
        global mcindv1
        global mcindv2
        global mcindv3
        global mcindv4
        global mctotal
        global cindv1
        global cindv2
        global cindv3
        global cindv4
        global ctotal
        global mtime
        global mc1
        global mc2
        global mc3
        global mc4
        global mm1
        global mm2
        global crot
        global mrot1
        global mrot2
        global mcil1
        global mcil2
        global mcil3
        global mcil4
        global mcaixa1
        global mcaixa2
        global mcaixa3
        global mcaixa4
        global mcaixa5
        global mcaixa6
        global mcaixa7
        global mcaixa8
        global mcaixa9
        global mcaixa10
        global cn
        global mcolor7
        global ms
        global vc1
        global vc2
        global vc3
        global vc4
        global vm1
        global vm2
        global cr
        mod=2
        vbot=1
        crot=crot+1
        if (crot==4):
            crot=1
        if (vm1==1):
            if (crot==1):
                mrot1="rot1-green.png"
            if (crot==2):
                mrot1="rot2-green.png"
            if (crot==3):
                mrot1="rot3-green.png"
            if (crot==4):
                mrot1="rot4-green.png"
        if (vm2==1):
            if (crot==1):
                mrot2="rot1-green.png"
            if (crot==2):
                mrot2="rot2-green.png"
            if (crot==3):
                mrot2="rot3-green.png"
            if (crot==4):
                mrot2="rot4-green.png"
        if (vm1==0):
            mrot1="green.png"
        if (vm2==0):
            mrot2="green.png"
        if (vc1==1):
            mcil1="cil-acionado-green.jpg"
        if (vc1==0):
            mcil1="cil-desacionado-green.jpg"
        if (vc2==1):
            mcil2="cil-acionado-green.jpg"
        if (vc2==0):
            mcil2="cil-desacionado-green.jpg"
        if (vc3==1):
            mcil3="cil-acionado-green.jpg"
        if (vc3==0):
            mcil3="cil-desacionado-green.jpg"
        if (vc4==1):
            mcil4="cil-acionado-green.jpg"
        if (vc4==0):
            mcil4="cil-desacionado-green.jpg"
        if (ms==0):
            mcaixa1="green.png"
            mcaixa2="green.png"
            mcaixa3="green.png"
            mcaixa4="green.png"
            mcaixa5="green.png"
            mcaixa6="green.png"
            mcaixa7="green.png"
            mcaixa8="green.png"
            mcaixa9="green.png"
            mcaixa10="green.png" 
        print(cr)
        if (ms==1):
            if (cn==1):
                mcaixa1="caixa-madeirabaixa.png"
                ####
            if (cn==2):
                mcaixa1="caixa-madeiraalta.png"
                
            if (cn==3):
                mcaixa1="caixa-metalbaixa.png"
                
            if (cn==4):
                mcaixa1="caixa-metalalta.png"
                
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2="green.png"
                cr=cr-1### tentar arrumar o bug fazendo o cr ate 10
        if (ms==2):
            if (cn==1):
                mcaixa2="caixa-madeirabaixa.png"
                cn=0
            if (cn==2):
                mcaixa2="caixa-madeiraalta.png"
                cn=0
            if (cn==3):
                mcaixa2="caixa-metalbaixa.png"
                cn=0
            if (cn==4):
                mcaixa2="caixa-metalalta.png"
                cn=0
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3="green.png"
                cr=cr-1
        if (ms==3): 
            if (cn==1):
                mcaixa3="caixa-madeirabaixa.png"
                cn=0
            if (cn==2):
                mcaixa3="caixa-madeiraalta.png"
                cn=0
            if (cn==3):
                mcaixa3="caixa-metalbaixa.png"
                cn=0
            if (cn==4):
                mcaixa3="caixa-metalalta.png"
                cn=0
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3=mcaixa4
                mcaixa4="green.png"
                cr=cr-1            
        if (ms==4):
            if (cn==1):
                mcaixa4="caixa-madeirabaixa.png"
                cn=0
            if (cn==2):
                mcaixa4="caixa-madeiraalta.png"
                cn=0
            if (cn==3):
                mcaixa4="caixa-metalbaixa.png"
                cn=0
            if (cn==4):
                mcaixa4="caixa-metalalta.png"
                cn=0
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3=mcaixa4
                mcaixa4=mcaixa5
                mcaixa5="green.png"
                cr=cr-1
        if (ms==5):
            if (cn==1):
                mcaixa5="caixa-madeirabaixa.png"
                cn=0
            if (cn==2):
                mcaixa5="caixa-madeiraalta.png"
                cn=0
            if (cn==3):
                mcaixa5="caixa-metalbaixa.png"
                cn=0
            if (cn==4):
                mcaixa5="caixa-metalalta.png"
                cn=0
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3=mcaixa4
                mcaixa4=mcaixa5
                mcaixa5=mcaixa6
                mcaixa6="green.png"
                cr=cr-1
        if (ms==6):           
            if (cn==1):
                mcaixa6="caixa-madeirabaixa.png"
                cn=0
            if (cn==2):
                mcaixa6="caixa-madeiraalta.png"
                cn=0
            if (cn==3):
                mcaixa6="caixa-metalbaixa.png"
                cn=0
            if (cn==4):
                mcaixa6="caixa-metalalta.png"
                cn=0
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3=mcaixa4
                mcaixa4=mcaixa5
                mcaixa5=mcaixa6
                mcaixa6=mcaixa7
                mcaixa7="green.png"
                cr=cr-1
        if (ms==7):
            if (cn==1):
                mcaixa7="caixa-madeirabaixa.png"
                cn=0
            if (cn==2):
                mcaixa7="caixa-madeiraalta.png"
                cn=0
            if (cn==3):
                mcaixa7="caixa-metalbaixa.png"
                cn=0
            if (cn==4):
                mcaixa7="caixa-metalalta.png"
                cn=0
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3=mcaixa4
                mcaixa4=mcaixa5
                mcaixa5=mcaixa6
                mcaixa6=mcaixa7
                mcaixa7=mcaixa8
                mcaixa8="green.png"
                cr=cr-1
        if (ms==8):
            if (cn==1):
                mcaixa8="caixa-madeirabaixa.png"
            if (cn==2):
                mcaixa8="caixa-madeiraalta.png"
            if (cn==3):
                mcaixa8="caixa-metalbaixa.png"
            if (cn==4):
                mcaixa8="caixa-metalalta.png"
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3=mcaixa4
                mcaixa4=mcaixa5
                mcaixa5=mcaixa6
                mcaixa6=mcaixa7
                mcaixa7=mcaixa8
                mcaixa8=mcaixa9
                mcaixa9="green.png"
                cr=cr-1
        if (ms==9):
            mcaixa10="green.png"
            if (cn==1):
                mcaixa9="caixa-madeirabaixa.png"
                cn=0
            if (cn==2):
                mcaixa9="caixa-madeiraalta.png"
                cn=0
            if (cn==3):
                mcaixa9="caixa-metalbaixa.png"
                cn=0
            if (cn==4):
                mcaixa9="caixa-metalalta.png"
                cn=0
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3=mcaixa4
                mcaixa4=mcaixa5
                mcaixa5=mcaixa6
                mcaixa6=mcaixa7
                mcaixa7=mcaixa8
                mcaixa8=mcaixa9
                mcaixa9=mcaixa10
                mcaixa10="green.png"
                cr=cr-1
        if (ms==10):
            if (cn==1):
                mcaixa10="caixa-madeirabaixa.png"
                cn=0
            if (cn==2):
                mcaixa10="caixa-madeiraalta.png"
                cn=0
            if (cn==3):
                mcaixa10="caixa-metalbaixa.png"
                cn=0
            if (cn==4):
                mcaixa10="caixa-metalalta.png"
                cn=0
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3=mcaixa4
                mcaixa4=mcaixa5
                mcaixa5=mcaixa6
                mcaixa6=mcaixa7
                mcaixa7=mcaixa8
                mcaixa8=mcaixa9
                mcaixa9=mcaixa10
                cr=cr-1
        if (vm1==1 and vm2==1):
            mcolor7="lime"
        if (vm1==0 and vm2==0):
            mcolor7="red"
        print('entro mod2')
        prog()
        templateData={
            'mem':mmem,
            'ms':mms,
            'mmt':mmt,
            'mcindv1':mcindv1,
            'mcindv2':mcindv2,
            'mcindv3':mcindv3,
            'mcindv4':mcindv4,
            'mctotal':mctotal,
            'mtime':mtime,
            'mc1':mc1,
            'mc2':mc2,
            'mc3':mc3,
            'mc4':mc4,
            'mm1':mm1,
            'mm2':mm2,
            'mrot1':mrot1,
            'mrot2':mrot2,
            'mcil1':mcil1,
            'mcil2':mcil2,
            'mcil3':mcil3,
            'mcil4':mcil4,
            'mcaixa1':mcaixa1,
            'mcaixa2':mcaixa2,
            'mcaixa3':mcaixa3,
            'mcaixa4':mcaixa4,
            'mcaixa5':mcaixa5,
            'mcaixa6':mcaixa6,
            'mcaixa7':mcaixa7,
            'mcaixa8':mcaixa8,
            'mcaixa9':mcaixa9,
            'mcaixa10':mcaixa10,
            'mcolor7':mcolor7
        }
        return render_template('mod2.html', **templateData)
    @app.route("/vbotl")
    def vbotl():
        global mod
        global vbot
        global mmem
        global mms
        global mmt
        global mcindv1
        global mcindv2
        global mcindv3
        global mcindv4
        global mctotal
        global cindv1
        global cindv2
        global cindv3
        global cindv4
        global ctotal
        global mtime
        global mc1
        global mc2
        global mc3
        global mc4
        global mm1
        global mm2
        global crot
        global mrot1
        global mrot2
        global mcil1
        global mcil2
        global mcil3
        global mcil4
        global mcaixa1
        global mcaixa2
        global mcaixa3
        global mcaixa4
        global mcaixa5
        global mcaixa6
        global mcaixa7
        global mcaixa8
        global mcaixa9
        global mcaixa10
        global cn
        global mcolor7
        global ms
        global vc1
        global vc2
        global vc3
        global vc4
        global vm1
        global vm2
        global cr
        mod=2
        vbot=0
        crot=crot+1
        if (crot==4):
            crot=1
        if (vm1==1):
            if (crot==1):
                mrot1="rot1-green.png"
            if (crot==2):
                mrot1="rot2-green.png"
            if (crot==3):
                mrot1="rot3-green.png"
            if (crot==4):
                mrot1="rot4-green.png"
        if (vm2==1):
            if (crot==1):
                mrot2="rot1-green.png"
            if (crot==2):
                mrot2="rot2-green.png"
            if (crot==3):
                mrot2="rot3-green.png"
            if (crot==4):
                mrot2="rot4-green.png"
        if (vm1==0):
            mrot1="green.png"
        if (vm2==0):
            mrot2="green.png"
        if (vc1==1):
            mcil1="cil-acionado-green.jpg"
        if (vc1==0):
            mcil1="cil-desacionado-green.jpg"
        if (vc2==1):
            mcil2="cil-acionado-green.jpg"
        if (vc2==0):
            mcil2="cil-desacionado-green.jpg"
        if (vc3==1):
            mcil3="cil-acionado-green.jpg"
        if (vc3==0):
            mcil3="cil-desacionado-green.jpg"
        if (vc4==1):
            mcil4="cil-acionado-green.jpg"
        if (vc4==0):
            mcil4="cil-desacionado-green.jpg"
        if (ms==0):
            mcaixa1="green.png"
            mcaixa2="green.png"
            mcaixa3="green.png"
            mcaixa4="green.png"
            mcaixa5="green.png"
            mcaixa6="green.png"
            mcaixa7="green.png"
            mcaixa8="green.png"
            mcaixa9="green.png"
            mcaixa10="green.png" 
        print(cr)
        if (ms==1):
            if (cn==1):
                mcaixa1="caixa-madeirabaixa.png"
                ####
            if (cn==2):
                mcaixa1="caixa-madeiraalta.png"
                
            if (cn==3):
                mcaixa1="caixa-metalbaixa.png"
                
            if (cn==4):
                mcaixa1="caixa-metalalta.png"
                
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2="green.png"
                cr=cr-1### tentar arrumar o bug fazendo o cr ate 10
        if (ms==2):
            if (cn==1):
                mcaixa2="caixa-madeirabaixa.png"
                cn=0
            if (cn==2):
                mcaixa2="caixa-madeiraalta.png"
                cn=0
            if (cn==3):
                mcaixa2="caixa-metalbaixa.png"
                cn=0
            if (cn==4):
                mcaixa2="caixa-metalalta.png"
                cn=0
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3="green.png"
                cr=cr-1
        if (ms==3): 
            if (cn==1):
                mcaixa3="caixa-madeirabaixa.png"
                cn=0
            if (cn==2):
                mcaixa3="caixa-madeiraalta.png"
                cn=0
            if (cn==3):
                mcaixa3="caixa-metalbaixa.png"
                cn=0
            if (cn==4):
                mcaixa3="caixa-metalalta.png"
                cn=0
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3=mcaixa4
                mcaixa4="green.png"
                cr=cr-1            
        if (ms==4):
            if (cn==1):
                mcaixa4="caixa-madeirabaixa.png"
                cn=0
            if (cn==2):
                mcaixa4="caixa-madeiraalta.png"
                cn=0
            if (cn==3):
                mcaixa4="caixa-metalbaixa.png"
                cn=0
            if (cn==4):
                mcaixa4="caixa-metalalta.png"
                cn=0
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3=mcaixa4
                mcaixa4=mcaixa5
                mcaixa5="green.png"
                cr=cr-1
        if (ms==5):
            if (cn==1):
                mcaixa5="caixa-madeirabaixa.png"
                cn=0
            if (cn==2):
                mcaixa5="caixa-madeiraalta.png"
                cn=0
            if (cn==3):
                mcaixa5="caixa-metalbaixa.png"
                cn=0
            if (cn==4):
                mcaixa5="caixa-metalalta.png"
                cn=0
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3=mcaixa4
                mcaixa4=mcaixa5
                mcaixa5=mcaixa6
                mcaixa6="green.png"
                cr=cr-1
        if (ms==6):           
            if (cn==1):
                mcaixa6="caixa-madeirabaixa.png"
                cn=0
            if (cn==2):
                mcaixa6="caixa-madeiraalta.png"
                cn=0
            if (cn==3):
                mcaixa6="caixa-metalbaixa.png"
                cn=0
            if (cn==4):
                mcaixa6="caixa-metalalta.png"
                cn=0
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3=mcaixa4
                mcaixa4=mcaixa5
                mcaixa5=mcaixa6
                mcaixa6=mcaixa7
                mcaixa7="green.png"
                cr=cr-1
        if (ms==7):
            if (cn==1):
                mcaixa7="caixa-madeirabaixa.png"
                cn=0
            if (cn==2):
                mcaixa7="caixa-madeiraalta.png"
                cn=0
            if (cn==3):
                mcaixa7="caixa-metalbaixa.png"
                cn=0
            if (cn==4):
                mcaixa7="caixa-metalalta.png"
                cn=0
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3=mcaixa4
                mcaixa4=mcaixa5
                mcaixa5=mcaixa6
                mcaixa6=mcaixa7
                mcaixa7=mcaixa8
                mcaixa8="green.png"
                cr=cr-1
        if (ms==8):
            if (cn==1):
                mcaixa8="caixa-madeirabaixa.png"
            if (cn==2):
                mcaixa8="caixa-madeiraalta.png"
            if (cn==3):
                mcaixa8="caixa-metalbaixa.png"
            if (cn==4):
                mcaixa8="caixa-metalalta.png"
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3=mcaixa4
                mcaixa4=mcaixa5
                mcaixa5=mcaixa6
                mcaixa6=mcaixa7
                mcaixa7=mcaixa8
                mcaixa8=mcaixa9
                mcaixa9="green.png"
                cr=cr-1
        if (ms==9):
            mcaixa10="green.png"
            if (cn==1):
                mcaixa9="caixa-madeirabaixa.png"
                cn=0
            if (cn==2):
                mcaixa9="caixa-madeiraalta.png"
                cn=0
            if (cn==3):
                mcaixa9="caixa-metalbaixa.png"
                cn=0
            if (cn==4):
                mcaixa9="caixa-metalalta.png"
                cn=0
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3=mcaixa4
                mcaixa4=mcaixa5
                mcaixa5=mcaixa6
                mcaixa6=mcaixa7
                mcaixa7=mcaixa8
                mcaixa8=mcaixa9
                mcaixa9=mcaixa10
                mcaixa10="green.png"
                cr=cr-1
        if (ms==10):
            if (cn==1):
                mcaixa10="caixa-madeirabaixa.png"
                cn=0
            if (cn==2):
                mcaixa10="caixa-madeiraalta.png"
                cn=0
            if (cn==3):
                mcaixa10="caixa-metalbaixa.png"
                cn=0
            if (cn==4):
                mcaixa10="caixa-metalalta.png"
                cn=0
            if (cr>=1):
                mcaixa1=mcaixa2
                mcaixa2=mcaixa3
                mcaixa3=mcaixa4
                mcaixa4=mcaixa5
                mcaixa5=mcaixa6
                mcaixa6=mcaixa7
                mcaixa7=mcaixa8
                mcaixa8=mcaixa9
                mcaixa9=mcaixa10
                cr=cr-1
        if (vm1==1 and vm2==1):
            mcolor7="lime"
        if (vm1==0 and vm2==0):
            mcolor7="red"
        print('entro mod2')
        prog()
        templateData={
            'mem':mmem,
            'ms':mms,
            'mmt':mmt,
            'mcindv1':mcindv1,
            'mcindv2':mcindv2,
            'mcindv3':mcindv3,
            'mcindv4':mcindv4,
            'mctotal':mctotal,
            'mtime':mtime,
            'mc1':mc1,
            'mc2':mc2,
            'mc3':mc3,
            'mc4':mc4,
            'mm1':mm1,
            'mm2':mm2,
            'mrot1':mrot1,
            'mrot2':mrot2,
            'mcil1':mcil1,
            'mcil2':mcil2,
            'mcil3':mcil3,
            'mcil4':mcil4,
            'mcaixa1':mcaixa1,
            'mcaixa2':mcaixa2,
            'mcaixa3':mcaixa3,
            'mcaixa4':mcaixa4,
            'mcaixa5':mcaixa5,
            'mcaixa6':mcaixa6,
            'mcaixa7':mcaixa7,
            'mcaixa8':mcaixa8,
            'mcaixa9':mcaixa9,
            'mcaixa10':mcaixa10,
            'mcolor7':mcolor7
        }
        return render_template('mod2.html', **templateData)
    @app.route("/mod1")
    def mod1():
        global mod
        global mcindv1
        global mcindv2
        global mcindv3
        global mcindv4
        global mctotal
        global cindv1
        global cindv2
        global cindv3
        global cindv4
        global ctotal
        global mtime
        global mc1
        global mc2
        global mc3
        global mc4
        global mm1
        global mm2
        global vc1
        global vc2
        global vc3
        global vc4
        global vm1
        global vm2
        global crot
        global mrot1
        global mrot2
        global mcil1
        global mcil2
        global mcil3
        global mcil4
        global mcolor1
        global mcolor2
        global mcolor3
        global mcolor4
        global mcolor5
        global mcolor6
        mod=1
        crot=crot+1
        if (crot==4):
            crot=1
        if (vm1==1):
            if (crot==1):
                mrot1="rot1-blue.png"
            if (crot==2):
                mrot1="rot2-blue.png"
            if (crot==3):
                mrot1="rot3-blue.png"
            if (crot==4):
                mrot1="rot4-blue.png"
            mcolor1="lime"
        if (vm1==0):
            mrot1="blue.png"
            mcolor1="red"
        if (vm2==1):
            if (crot==1):
                mrot2="rot1-blue.png"
            if (crot==2):
                mrot2="rot2-blue.png"
            if (crot==3):
                mrot2="rot3-blue.png"
            if (crot==4):
                mrot2="rot4-blue.png"
            mcolor2="lime"
        if (vm2==0):
            mrot2="blue.png"
            mcolor2="red"
        if (vc1==1):
            mcil1="cil-acionado-blue.jpg"
            mcolor3="lime"
        if (vc1==0):
            mcil1="cil-desacionado-blue.jpg"
            mcolor3="red"
        if (vc2==1):
            mcil2="cil-acionado-blue.jpg"
            mcolor4="lime"
        if (vc2==0):
            mcil2="cil-desacionado-blue.jpg"
            mcolor4="red"
        if (vc3==1):
            mcil3="cil-acionado-blue.jpg"
            mcolor5="lime"
        if (vc3==0):
            mcil3="cil-desacionado-blue.jpg"
            mcolor5="red"
        if (vc4==1):
            mcil4="cil-acionado-blue.jpg"
            mcolor6="lime"
        if (vc4==0):
            mcil4="cil-desacionado-blue.jpg"
            mcolor6="red"
        print('entro mod1')
        prog()
        templateData={
            'mcindv1':mcindv1,
            'mcindv2':mcindv2,
            'mcindv3':mcindv3,
            'mcindv4':mcindv4,
            'mctotal':mctotal,
            'mtime':mtime,
            'mc1':mc1,
            'mc2':mc2,
            'mc3':mc3,
            'mc4':mc4,
            'mm1':mm1,
            'mm2':mm2,
            'mrot1':mrot1,
            'mrot2':mrot2,
            'mcil1':mcil1,
            'mcil2':mcil2,
            'mcil3':mcil3,
            'mcil4':mcil4,
            'mcolor1':mcolor1,
            'mcolor2':mcolor2,
            'mcolor3':mcolor3,
            'mcolor4':mcolor4,
            'mcolor5':mcolor5,
            'mcolor6':mcolor6
        }
        return render_template('mod1.html', **templateData)
    @app.route("/mod1stop")
    def mod1stop():
        global mod
        global mcindv1
        global mcindv2
        global mcindv3
        global mcindv4
        global mctotal
        global cindv1
        global cindv2
        global cindv3
        global cindv4
        global ctotal
        global mtime
        global mc1
        global mc2
        global mc3
        global mc4
        global mm1
        global mm2
        global vc1
        global vc2
        global vc3
        global vc4
        global vm1
        global vm2
        global crot
        global mrot1
        global mrot2
        global mcil1
        global mcil2
        global mcil3
        global mcil4
        global mcolor1
        global mcolor2
        global mcolor3
        global mcolor4
        global mcolor5
        global mcolor6
        global vbot
        mod=1
        vbot=1
        crot=crot+1
        if (crot==4):
            crot=1
        if (vm1==1):
            if (crot==1):
                mrot1="rot1-blue.png"
            if (crot==2):
                mrot1="rot2-blue.png"
            if (crot==3):
                mrot1="rot3-blue.png"
            if (crot==4):
                mrot1="rot4-blue.png"
            mcolor1="lime"
        if (vm1==0):
            mrot1="blue.png"
            mcolor1="red"
        if (vm2==1):
            if (crot==1):
                mrot2="rot1-blue.png"
            if (crot==2):
                mrot2="rot2-blue.png"
            if (crot==3):
                mrot2="rot3-blue.png"
            if (crot==4):
                mrot2="rot4-blue.png"
            mcolor2="lime"
        if (vm2==0):
            mrot2="blue.png"
            mcolor2="red"
        if (vc1==1):
            mcil1="cil-acionado-blue.jpg"
            mcolor3="lime"
        if (vc1==0):
            mcil1="cil-desacionado-blue.jpg"
            mcolor3="red"
        if (vc2==1):
            mcil2="cil-acionado-blue.jpg"
            mcolor4="lime"
        if (vc2==0):
            mcil2="cil-desacionado-blue.jpg"
            mcolor4="red"
        if (vc3==1):
            mcil3="cil-acionado-blue.jpg"
            mcolor5="lime"
        if (vc3==0):
            mcil3="cil-desacionado-blue.jpg"
            mcolor5="red"
        if (vc4==1):
            mcil4="cil-acionado-blue.jpg"
            mcolor6="lime"
        if (vc4==0):
            mcil4="cil-desacionado-blue.jpg"
            mcolor6="red"
        print('entro mod1')
        prog()
        templateData={
            'mcindv1':mcindv1,
            'mcindv2':mcindv2,
            'mcindv3':mcindv3,
            'mcindv4':mcindv4,
            'mctotal':mctotal,
            'mtime':mtime,
            'mc1':mc1,
            'mc2':mc2,
            'mc3':mc3,
            'mc4':mc4,
            'mm1':mm1,
            'mm2':mm2,
            'mrot1':mrot1,
            'mrot2':mrot2,
            'mcil1':mcil1,
            'mcil2':mcil2,
            'mcil3':mcil3,
            'mcil4':mcil4,
            'mcolor1':mcolor1,
            'mcolor2':mcolor2,
            'mcolor3':mcolor3,
            'mcolor4':mcolor4,
            'mcolor5':mcolor5,
            'mcolor6':mcolor6
        }
        return render_template('mod1.html', **templateData)
    @app.route("/vc1l")
    def vc1l():
        global mod
        global mcindv1
        global mcindv2
        global mcindv3
        global mcindv4
        global mctotal
        global cindv1
        global cindv2
        global cindv3
        global cindv4
        global ctotal
        global mtime
        global mc1
        global mc2
        global mc3
        global mc4
        global mm1
        global mm2
        global vc1
        global vc2
        global vc3
        global vc4
        global vm1
        global vm2
        global crot
        global mrot1
        global mrot2
        global mcil1
        global mcil2
        global mcil3
        global mcil4
        global mcolor1
        global mcolor2
        global mcolor3
        global mcolor4
        global mcolor5
        global mcolor6
        mod=1
        vc1=1
        crot=crot+1
        if (crot==4):
            crot=1
        if (vm1==1):
            if (crot==1):
                mrot1="rot1-blue.png"
            if (crot==2):
                mrot1="rot2-blue.png"
            if (crot==3):
                mrot1="rot3-blue.png"
            if (crot==4):
                mrot1="rot4-blue.png"
            mcolor1="lime"
        if (vm1==0):
            mrot1="blue.png"
            mcolor1="red"
        if (vm2==1):
            if (crot==1):
                mrot2="rot1-blue.png"
            if (crot==2):
                mrot2="rot2-blue.png"
            if (crot==3):
                mrot2="rot3-blue.png"
            if (crot==4):
                mrot2="rot4-blue.png"
            mcolor2="lime"
        if (vm2==0):
            mrot2="blue.png"
            mcolor2="red"
        if (vc1==1):
            mcil1="cil-acionado-blue.jpg"
            mcolor3="lime"
        if (vc1==0):
            mcil1="cil-desacionado-blue.jpg"
            mcolor3="red"
        if (vc2==1):
            mcil2="cil-acionado-blue.jpg"
            mcolor4="lime"
        if (vc2==0):
            mcil2="cil-desacionado-blue.jpg"
            mcolor4="red"
        if (vc3==1):
            mcil3="cil-acionado-blue.jpg"
            mcolor5="lime"
        if (vc3==0):
            mcil3="cil-desacionado-blue.jpg"
            mcolor5="red"
        if (vc4==1):
            mcil4="cil-acionado-blue.jpg"
            mcolor6="lime"
        if (vc4==0):
            mcil4="cil-desacionado-blue.jpg"
            mcolor6="red"
        print('entro mod1')
        prog()
        templateData={
            'mcindv1':mcindv1,
            'mcindv2':mcindv2,
            'mcindv3':mcindv3,
            'mcindv4':mcindv4,
            'mctotal':mctotal,
            'mtime':mtime,
            'mc1':mc1,
            'mc2':mc2,
            'mc3':mc3,
            'mc4':mc4,
            'mm1':mm1,
            'mm2':mm2,
            'mrot1':mrot1,
            'mrot2':mrot2,
            'mcil1':mcil1,
            'mcil2':mcil2,
            'mcil3':mcil3,
            'mcil4':mcil4,
            'mcolor1':mcolor1,
            'mcolor2':mcolor2,
            'mcolor3':mcolor3,
            'mcolor4':mcolor4,
            'mcolor5':mcolor5,
            'mcolor6':mcolor6
        }
        return render_template('mod1.html', **templateData)
    @app.route("/vc1d")
    def vc1d():
        global mod
        global mcindv1
        global mcindv2
        global mcindv3
        global mcindv4
        global mctotal
        global cindv1
        global cindv2
        global cindv3
        global cindv4
        global ctotal
        global mtime
        global mc1
        global mc2
        global mc3
        global mc4
        global mm1
        global mm2
        global vc1
        global vc2
        global vc3
        global vc4
        global vm1
        global vm2
        global crot
        global mrot1
        global mrot2
        global mcil1
        global mcil2
        global mcil3
        global mcil4
        global mcolor1
        global mcolor2
        global mcolor3
        global mcolor4
        global mcolor5
        global mcolor6
        mod=1
        vc1=0
        crot=crot+1
        if (crot==4):
            crot=1
        if (vm1==1):
            if (crot==1):
                mrot1="rot1-blue.png"
            if (crot==2):
                mrot1="rot2-blue.png"
            if (crot==3):
                mrot1="rot3-blue.png"
            if (crot==4):
                mrot1="rot4-blue.png"
            mcolor1="lime"
        if (vm1==0):
            mrot1="blue.png"
            mcolor1="red"
        if (vm2==1):
            if (crot==1):
                mrot2="rot1-blue.png"
            if (crot==2):
                mrot2="rot2-blue.png"
            if (crot==3):
                mrot2="rot3-blue.png"
            if (crot==4):
                mrot2="rot4-blue.png"
            mcolor2="lime"
        if (vm2==0):
            mrot2="blue.png"
            mcolor2="red"
        if (vc1==1):
            mcil1="cil-acionado-blue.jpg"
            mcolor3="lime"
        if (vc1==0):
            mcil1="cil-desacionado-blue.jpg"
            mcolor3="red"
        if (vc2==1):
            mcil2="cil-acionado-blue.jpg"
            mcolor4="lime"
        if (vc2==0):
            mcil2="cil-desacionado-blue.jpg"
            mcolor4="red"
        if (vc3==1):
            mcil3="cil-acionado-blue.jpg"
            mcolor5="lime"
        if (vc3==0):
            mcil3="cil-desacionado-blue.jpg"
            mcolor5="red"
        if (vc4==1):
            mcil4="cil-acionado-blue.jpg"
            mcolor6="lime"
        if (vc4==0):
            mcil4="cil-desacionado-blue.jpg"
            mcolor6="red"
        print('entro mod1')
        prog()
        templateData={
            'mcindv1':mcindv1,
            'mcindv2':mcindv2,
            'mcindv3':mcindv3,
            'mcindv4':mcindv4,
            'mctotal':mctotal,
            'mtime':mtime,
            'mc1':mc1,
            'mc2':mc2,
            'mc3':mc3,
            'mc4':mc4,
            'mm1':mm1,
            'mm2':mm2,
            'mrot1':mrot1,
            'mrot2':mrot2,
            'mcil1':mcil1,
            'mcil2':mcil2,
            'mcil3':mcil3,
            'mcil4':mcil4,
            'mcolor1':mcolor1,
            'mcolor2':mcolor2,
            'mcolor3':mcolor3,
            'mcolor4':mcolor4,
            'mcolor5':mcolor5,
            'mcolor6':mcolor6
        }
        return render_template('mod1.html', **templateData)
    @app.route("/vc2l")
    def vc2l():
        global mod
        global mcindv1
        global mcindv2
        global mcindv3
        global mcindv4
        global mctotal
        global cindv1
        global cindv2
        global cindv3
        global cindv4
        global ctotal
        global mtime
        global mc1
        global mc2
        global mc3
        global mc4
        global mm1
        global mm2
        global vc1
        global vc2
        global vc3
        global vc4
        global vm1
        global vm2
        global crot
        global mrot1
        global mrot2
        global mcil1
        global mcil2
        global mcil3
        global mcil4
        global mcolor1
        global mcolor2
        global mcolor3
        global mcolor4
        global mcolor5
        global mcolor6
        mod=1
        vc2=1
        crot=crot+1
        if (crot==4):
            crot=1
        if (vm1==1):
            if (crot==1):
                mrot1="rot1-blue.png"
            if (crot==2):
                mrot1="rot2-blue.png"
            if (crot==3):
                mrot1="rot3-blue.png"
            if (crot==4):
                mrot1="rot4-blue.png"
            mcolor1="lime"
        if (vm1==0):
            mrot1="blue.png"
            mcolor1="red"
        if (vm2==1):
            if (crot==1):
                mrot2="rot1-blue.png"
            if (crot==2):
                mrot2="rot2-blue.png"
            if (crot==3):
                mrot2="rot3-blue.png"
            if (crot==4):
                mrot2="rot4-blue.png"
            mcolor2="lime"
        if (vm2==0):
            mrot2="blue.png"
            mcolor2="red"
        if (vc1==1):
            mcil1="cil-acionado-blue.jpg"
            mcolor3="lime"
        if (vc1==0):
            mcil1="cil-desacionado-blue.jpg"
            mcolor3="red"
        if (vc2==1):
            mcil2="cil-acionado-blue.jpg"
            mcolor4="lime"
        if (vc2==0):
            mcil2="cil-desacionado-blue.jpg"
            mcolor4="red"
        if (vc3==1):
            mcil3="cil-acionado-blue.jpg"
            mcolor5="lime"
        if (vc3==0):
            mcil3="cil-desacionado-blue.jpg"
            mcolor5="red"
        if (vc4==1):
            mcil4="cil-acionado-blue.jpg"
            mcolor6="lime"
        if (vc4==0):
            mcil4="cil-desacionado-blue.jpg"
            mcolor6="red"
        print('entro mod1')
        prog()
        templateData={
            'mcindv1':mcindv1,
            'mcindv2':mcindv2,
            'mcindv3':mcindv3,
            'mcindv4':mcindv4,
            'mctotal':mctotal,
            'mtime':mtime,
            'mc1':mc1,
            'mc2':mc2,
            'mc3':mc3,
            'mc4':mc4,
            'mm1':mm1,
            'mm2':mm2,
            'mrot1':mrot1,
            'mrot2':mrot2,
            'mcil1':mcil1,
            'mcil2':mcil2,
            'mcil3':mcil3,
            'mcil4':mcil4,
            'mcolor1':mcolor1,
            'mcolor2':mcolor2,
            'mcolor3':mcolor3,
            'mcolor4':mcolor4,
            'mcolor5':mcolor5,
            'mcolor6':mcolor6
        }
        return render_template('mod1.html', **templateData)
    @app.route("/vc2d")
    def vc2d():
        global mod
        global mcindv1
        global mcindv2
        global mcindv3
        global mcindv4
        global mctotal
        global cindv1
        global cindv2
        global cindv3
        global cindv4
        global ctotal
        global mtime
        global mc1
        global mc2
        global mc3
        global mc4
        global mm1
        global mm2
        global vc1
        global vc2
        global vc3
        global vc4
        global vm1
        global vm2
        global crot
        global mrot1
        global mrot2
        global mcil1
        global mcil2
        global mcil3
        global mcil4
        global mcolor1
        global mcolor2
        global mcolor3
        global mcolor4
        global mcolor5
        global mcolor6
        mod=1
        vc2=0
        crot=crot+1
        if (crot==4):
            crot=1
        if (vm1==1):
            if (crot==1):
                mrot1="rot1-blue.png"
            if (crot==2):
                mrot1="rot2-blue.png"
            if (crot==3):
                mrot1="rot3-blue.png"
            if (crot==4):
                mrot1="rot4-blue.png"
            mcolor1="lime"
        if (vm1==0):
            mrot1="blue.png"
            mcolor1="red"
        if (vm2==1):
            if (crot==1):
                mrot2="rot1-blue.png"
            if (crot==2):
                mrot2="rot2-blue.png"
            if (crot==3):
                mrot2="rot3-blue.png"
            if (crot==4):
                mrot2="rot4-blue.png"
            mcolor2="lime"
        if (vm2==0):
            mrot2="blue.png"
            mcolor2="red"
        if (vc1==1):
            mcil1="cil-acionado-blue.jpg"
            mcolor3="lime"
        if (vc1==0):
            mcil1="cil-desacionado-blue.jpg"
            mcolor3="red"
        if (vc2==1):
            mcil2="cil-acionado-blue.jpg"
            mcolor4="lime"
        if (vc2==0):
            mcil2="cil-desacionado-blue.jpg"
            mcolor4="red"
        if (vc3==1):
            mcil3="cil-acionado-blue.jpg"
            mcolor5="lime"
        if (vc3==0):
            mcil3="cil-desacionado-blue.jpg"
            mcolor5="red"
        if (vc4==1):
            mcil4="cil-acionado-blue.jpg"
            mcolor6="lime"
        if (vc4==0):
            mcil4="cil-desacionado-blue.jpg"
            mcolor6="red"
        print('entro mod1')
        prog()
        templateData={
            'mcindv1':mcindv1,
            'mcindv2':mcindv2,
            'mcindv3':mcindv3,
            'mcindv4':mcindv4,
            'mctotal':mctotal,
            'mtime':mtime,
            'mc1':mc1,
            'mc2':mc2,
            'mc3':mc3,
            'mc4':mc4,
            'mm1':mm1,
            'mm2':mm2,
            'mrot1':mrot1,
            'mrot2':mrot2,
            'mcil1':mcil1,
            'mcil2':mcil2,
            'mcil3':mcil3,
            'mcil4':mcil4,
            'mcolor1':mcolor1,
            'mcolor2':mcolor2,
            'mcolor3':mcolor3,
            'mcolor4':mcolor4,
            'mcolor5':mcolor5,
            'mcolor6':mcolor6
        }
        return render_template('mod1.html', **templateData)
    @app.route("/vc3l")
    def vc3l():
        global mod
        global mcindv1
        global mcindv2
        global mcindv3
        global mcindv4
        global mctotal
        global cindv1
        global cindv2
        global cindv3
        global cindv4
        global ctotal
        global mtime
        global mc1
        global mc2
        global mc3
        global mc4
        global mm1
        global mm2
        global vc1
        global vc2
        global vc3
        global vc4
        global vm1
        global vm2
        global crot
        global mrot1
        global mrot2
        global mcil1
        global mcil2
        global mcil3
        global mcil4
        global mcolor1
        global mcolor2
        global mcolor3
        global mcolor4
        global mcolor5
        global mcolor6
        mod=1
        vc3=1
        crot=crot+1
        if (crot==4):
            crot=1
        if (vm1==1):
            if (crot==1):
                mrot1="rot1-blue.png"
            if (crot==2):
                mrot1="rot2-blue.png"
            if (crot==3):
                mrot1="rot3-blue.png"
            if (crot==4):
                mrot1="rot4-blue.png"
            mcolor1="lime"
        if (vm1==0):
            mrot1="blue.png"
            mcolor1="red"
        if (vm2==1):
            if (crot==1):
                mrot2="rot1-blue.png"
            if (crot==2):
                mrot2="rot2-blue.png"
            if (crot==3):
                mrot2="rot3-blue.png"
            if (crot==4):
                mrot2="rot4-blue.png"
            mcolor2="lime"
        if (vm2==0):
            mrot2="blue.png"
            mcolor2="red"
        if (vc1==1):
            mcil1="cil-acionado-blue.jpg"
            mcolor3="lime"
        if (vc1==0):
            mcil1="cil-desacionado-blue.jpg"
            mcolor3="red"
        if (vc2==1):
            mcil2="cil-acionado-blue.jpg"
            mcolor4="lime"
        if (vc2==0):
            mcil2="cil-desacionado-blue.jpg"
            mcolor4="red"
        if (vc3==1):
            mcil3="cil-acionado-blue.jpg"
            mcolor5="lime"
        if (vc3==0):
            mcil3="cil-desacionado-blue.jpg"
            mcolor5="red"
        if (vc4==1):
            mcil4="cil-acionado-blue.jpg"
            mcolor6="lime"
        if (vc4==0):
            mcil4="cil-desacionado-blue.jpg"
            mcolor6="red"
        print('entro mod1')
        prog()
        templateData={
            'mcindv1':mcindv1,
            'mcindv2':mcindv2,
            'mcindv3':mcindv3,
            'mcindv4':mcindv4,
            'mctotal':mctotal,
            'mtime':mtime,
            'mc1':mc1,
            'mc2':mc2,
            'mc3':mc3,
            'mc4':mc4,
            'mm1':mm1,
            'mm2':mm2,
            'mrot1':mrot1,
            'mrot2':mrot2,
            'mcil1':mcil1,
            'mcil2':mcil2,
            'mcil3':mcil3,
            'mcil4':mcil4,
            'mcolor1':mcolor1,
            'mcolor2':mcolor2,
            'mcolor3':mcolor3,
            'mcolor4':mcolor4,
            'mcolor5':mcolor5,
            'mcolor6':mcolor6
        }
        return render_template('mod1.html', **templateData)
    @app.route("/vc3d")
    def vc3d():
        global mod
        global mcindv1
        global mcindv2
        global mcindv3
        global mcindv4
        global mctotal
        global cindv1
        global cindv2
        global cindv3
        global cindv4
        global ctotal
        global mtime
        global mc1
        global mc2
        global mc3
        global mc4
        global mm1
        global mm2
        global vc1
        global vc2
        global vc3
        global vc4
        global vm1
        global vm2
        global crot
        global mrot1
        global mrot2
        global mcil1
        global mcil2
        global mcil3
        global mcil4
        global mcolor1
        global mcolor2
        global mcolor3
        global mcolor4
        global mcolor5
        global mcolor6
        mod=1
        vc3=0
        crot=crot+1
        if (crot==4):
            crot=1
        if (vm1==1):
            if (crot==1):
                mrot1="rot1-blue.png"
            if (crot==2):
                mrot1="rot2-blue.png"
            if (crot==3):
                mrot1="rot3-blue.png"
            if (crot==4):
                mrot1="rot4-blue.png"
            mcolor1="lime"
        if (vm1==0):
            mrot1="blue.png"
            mcolor1="red"
        if (vm2==1):
            if (crot==1):
                mrot2="rot1-blue.png"
            if (crot==2):
                mrot2="rot2-blue.png"
            if (crot==3):
                mrot2="rot3-blue.png"
            if (crot==4):
                mrot2="rot4-blue.png"
            mcolor2="lime"
        if (vm2==0):
            mrot2="blue.png"
            mcolor2="red"
        if (vc1==1):
            mcil1="cil-acionado-blue.jpg"
            mcolor3="lime"
        if (vc1==0):
            mcil1="cil-desacionado-blue.jpg"
            mcolor3="red"
        if (vc2==1):
            mcil2="cil-acionado-blue.jpg"
            mcolor4="lime"
        if (vc2==0):
            mcil2="cil-desacionado-blue.jpg"
            mcolor4="red"
        if (vc3==1):
            mcil3="cil-acionado-blue.jpg"
            mcolor5="lime"
        if (vc3==0):
            mcil3="cil-desacionado-blue.jpg"
            mcolor5="red"
        if (vc4==1):
            mcil4="cil-acionado-blue.jpg"
            mcolor6="lime"
        if (vc4==0):
            mcil4="cil-desacionado-blue.jpg"
            mcolor6="red"
        print('entro mod1')
        prog()
        templateData={
            'mcindv1':mcindv1,
            'mcindv2':mcindv2,
            'mcindv3':mcindv3,
            'mcindv4':mcindv4,
            'mctotal':mctotal,
            'mtime':mtime,
            'mc1':mc1,
            'mc2':mc2,
            'mc3':mc3,
            'mc4':mc4,
            'mm1':mm1,
            'mm2':mm2,
            'mrot1':mrot1,
            'mrot2':mrot2,
            'mcil1':mcil1,
            'mcil2':mcil2,
            'mcil3':mcil3,
            'mcil4':mcil4,
            'mcolor1':mcolor1,
            'mcolor2':mcolor2,
            'mcolor3':mcolor3,
            'mcolor4':mcolor4,
            'mcolor5':mcolor5,
            'mcolor6':mcolor6
        }
        return render_template('mod1.html', **templateData)
    @app.route("/vc4l")
    def vc4l():
        global mod
        global mcindv1
        global mcindv2
        global mcindv3
        global mcindv4
        global mctotal
        global cindv1
        global cindv2
        global cindv3
        global cindv4
        global ctotal
        global mtime
        global mc1
        global mc2
        global mc3
        global mc4
        global mm1
        global mm2
        global vc1
        global vc2
        global vc3
        global vc4
        global vm1
        global vm2
        global crot
        global mrot1
        global mrot2
        global mcil1
        global mcil2
        global mcil3
        global mcil4
        global mcolor1
        global mcolor2
        global mcolor3
        global mcolor4
        global mcolor5
        global mcolor6
        mod=1
        vc4=1
        crot=crot+1
        if (crot==4):
            crot=1
        if (vm1==1):
            if (crot==1):
                mrot1="rot1-blue.png"
            if (crot==2):
                mrot1="rot2-blue.png"
            if (crot==3):
                mrot1="rot3-blue.png"
            if (crot==4):
                mrot1="rot4-blue.png"
            mcolor1="lime"
        if (vm1==0):
            mrot1="blue.png"
            mcolor1="red"
        if (vm2==1):
            if (crot==1):
                mrot2="rot1-blue.png"
            if (crot==2):
                mrot2="rot2-blue.png"
            if (crot==3):
                mrot2="rot3-blue.png"
            if (crot==4):
                mrot2="rot4-blue.png"
            mcolor2="lime"
        if (vm2==0):
            mrot2="blue.png"
            mcolor2="red"
        if (vc1==1):
            mcil1="cil-acionado-blue.jpg"
            mcolor3="lime"
        if (vc1==0):
            mcil1="cil-desacionado-blue.jpg"
            mcolor3="red"
        if (vc2==1):
            mcil2="cil-acionado-blue.jpg"
            mcolor4="lime"
        if (vc2==0):
            mcil2="cil-desacionado-blue.jpg"
            mcolor4="red"
        if (vc3==1):
            mcil3="cil-acionado-blue.jpg"
            mcolor5="lime"
        if (vc3==0):
            mcil3="cil-desacionado-blue.jpg"
            mcolor5="red"
        if (vc4==1):
            mcil4="cil-acionado-blue.jpg"
            mcolor6="lime"
        if (vc4==0):
            mcil4="cil-desacionado-blue.jpg"
            mcolor6="red"
        print('entro mod1')
        prog()
        templateData={
            'mcindv1':mcindv1,
            'mcindv2':mcindv2,
            'mcindv3':mcindv3,
            'mcindv4':mcindv4,
            'mctotal':mctotal,
            'mtime':mtime,
            'mc1':mc1,
            'mc2':mc2,
            'mc3':mc3,
            'mc4':mc4,
            'mm1':mm1,
            'mm2':mm2,
            'mrot1':mrot1,
            'mrot2':mrot2,
            'mcil1':mcil1,
            'mcil2':mcil2,
            'mcil3':mcil3,
            'mcil4':mcil4,
            'mcolor1':mcolor1,
            'mcolor2':mcolor2,
            'mcolor3':mcolor3,
            'mcolor4':mcolor4,
            'mcolor5':mcolor5,
            'mcolor6':mcolor6
        }
        return render_template('mod1.html', **templateData)
    @app.route("/vc4d")
    def vc4d():
        global mod
        global mcindv1
        global mcindv2
        global mcindv3
        global mcindv4
        global mctotal
        global cindv1
        global cindv2
        global cindv3
        global cindv4
        global ctotal
        global mtime
        global mc1
        global mc2
        global mc3
        global mc4
        global mm1
        global mm2
        global vc1
        global vc2
        global vc3
        global vc4
        global vm1
        global vm2
        global crot
        global mrot1
        global mrot2
        global mcil1
        global mcil2
        global mcil3
        global mcil4
        global mcolor1
        global mcolor2
        global mcolor3
        global mcolor4
        global mcolor5
        global mcolor6
        mod=1
        vc4=0
        crot=crot+1
        if (crot==4):
            crot=1
        if (vm1==1):
            if (crot==1):
                mrot1="rot1-blue.png"
            if (crot==2):
                mrot1="rot2-blue.png"
            if (crot==3):
                mrot1="rot3-blue.png"
            if (crot==4):
                mrot1="rot4-blue.png"
            mcolor1="lime"
        if (vm1==0):
            mrot1="blue.png"
            mcolor1="red"
        if (vm2==1):
            if (crot==1):
                mrot2="rot1-blue.png"
            if (crot==2):
                mrot2="rot2-blue.png"
            if (crot==3):
                mrot2="rot3-blue.png"
            if (crot==4):
                mrot2="rot4-blue.png"
            mcolor2="lime"
        if (vm2==0):
            mrot2="blue.png"
            mcolor2="red"
        if (vc1==1):
            mcil1="cil-acionado-blue.jpg"
            mcolor3="lime"
        if (vc1==0):
            mcil1="cil-desacionado-blue.jpg"
            mcolor3="red"
        if (vc2==1):
            mcil2="cil-acionado-blue.jpg"
            mcolor4="lime"
        if (vc2==0):
            mcil2="cil-desacionado-blue.jpg"
            mcolor4="red"
        if (vc3==1):
            mcil3="cil-acionado-blue.jpg"
            mcolor5="lime"
        if (vc3==0):
            mcil3="cil-desacionado-blue.jpg"
            mcolor5="red"
        if (vc4==1):
            mcil4="cil-acionado-blue.jpg"
            mcolor6="lime"
        if (vc4==0):
            mcil4="cil-desacionado-blue.jpg"
            mcolor6="red"
        print('entro mod1')
        prog()
        templateData={
            'mcindv1':mcindv1,
            'mcindv2':mcindv2,
            'mcindv3':mcindv3,
            'mcindv4':mcindv4,
            'mctotal':mctotal,
            'mtime':mtime,
            'mc1':mc1,
            'mc2':mc2,
            'mc3':mc3,
            'mc4':mc4,
            'mm1':mm1,
            'mm2':mm2,
            'mrot1':mrot1,
            'mrot2':mrot2,
            'mcil1':mcil1,
            'mcil2':mcil2,
            'mcil3':mcil3,
            'mcil4':mcil4,
            'mcolor1':mcolor1,
            'mcolor2':mcolor2,
            'mcolor3':mcolor3,
            'mcolor4':mcolor4,
            'mcolor5':mcolor5,
            'mcolor6':mcolor6
        }
        return render_template('mod1.html', **templateData)
    @app.route("/vm1l")
    def vm1l():
        global mod
        global mcindv1
        global mcindv2
        global mcindv3
        global mcindv4
        global mctotal
        global cindv1
        global cindv2
        global cindv3
        global cindv4
        global ctotal
        global mtime
        global mc1
        global mc2
        global mc3
        global mc4
        global mm1
        global mm2
        global vc1
        global vc2
        global vc3
        global vc4
        global vm1
        global vm2
        global crot
        global mrot1
        global mrot2
        global mcil1
        global mcil2
        global mcil3
        global mcil4
        global mcolor1
        global mcolor2
        global mcolor3
        global mcolor4
        global mcolor5
        global mcolor6
        mod=1
        vm1=1
        crot=crot+1
        if (crot==4):
            crot=1
        if (vm1==1):
            if (crot==1):
                mrot1="rot1-blue.png"
            if (crot==2):
                mrot1="rot2-blue.png"
            if (crot==3):
                mrot1="rot3-blue.png"
            if (crot==4):
                mrot1="rot4-blue.png"
            mcolor1="lime"
        if (vm1==0):
            mrot1="blue.png"
            mcolor1="red"
        if (vm2==1):
            if (crot==1):
                mrot2="rot1-blue.png"
            if (crot==2):
                mrot2="rot2-blue.png"
            if (crot==3):
                mrot2="rot3-blue.png"
            if (crot==4):
                mrot2="rot4-blue.png"
            mcolor2="lime"
        if (vm2==0):
            mrot2="blue.png"
            mcolor2="red"
        if (vc1==1):
            mcil1="cil-acionado-blue.jpg"
            mcolor3="lime"
        if (vc1==0):
            mcil1="cil-desacionado-blue.jpg"
            mcolor3="red"
        if (vc2==1):
            mcil2="cil-acionado-blue.jpg"
            mcolor4="lime"
        if (vc2==0):
            mcil2="cil-desacionado-blue.jpg"
            mcolor4="red"
        if (vc3==1):
            mcil3="cil-acionado-blue.jpg"
            mcolor5="lime"
        if (vc3==0):
            mcil3="cil-desacionado-blue.jpg"
            mcolor5="red"
        if (vc4==1):
            mcil4="cil-acionado-blue.jpg"
            mcolor6="lime"
        if (vc4==0):
            mcil4="cil-desacionado-blue.jpg"
            mcolor6="red"
        print('entro mod1')
        prog()
        templateData={
            'mcindv1':mcindv1,
            'mcindv2':mcindv2,
            'mcindv3':mcindv3,
            'mcindv4':mcindv4,
            'mctotal':mctotal,
            'mtime':mtime,
            'mc1':mc1,
            'mc2':mc2,
            'mc3':mc3,
            'mc4':mc4,
            'mm1':mm1,
            'mm2':mm2,
            'mrot1':mrot1,
            'mrot2':mrot2,
            'mcil1':mcil1,
            'mcil2':mcil2,
            'mcil3':mcil3,
            'mcil4':mcil4,
            'mcolor1':mcolor1,
            'mcolor2':mcolor2,
            'mcolor3':mcolor3,
            'mcolor4':mcolor4,
            'mcolor5':mcolor5,
            'mcolor6':mcolor6
        }
        return render_template('mod1.html', **templateData)
    @app.route("/vm1d")
    def vm1d():
        global mod
        global mcindv1
        global mcindv2
        global mcindv3
        global mcindv4
        global mctotal
        global cindv1
        global cindv2
        global cindv3
        global cindv4
        global ctotal
        global mtime
        global mc1
        global mc2
        global mc3
        global mc4
        global mm1
        global mm2
        global vc1
        global vc2
        global vc3
        global vc4
        global vm1
        global vm2
        global crot
        global mrot1
        global mrot2
        global mcil1
        global mcil2
        global mcil3
        global mcil4
        global mcolor1
        global mcolor2
        global mcolor3
        global mcolor4
        global mcolor5
        global mcolor6
        mod=1
        vm1=0
        crot=crot+1
        if (crot==4):
            crot=1
        if (vm1==1):
            if (crot==1):
                mrot1="rot1-blue.png"
            if (crot==2):
                mrot1="rot2-blue.png"
            if (crot==3):
                mrot1="rot3-blue.png"
            if (crot==4):
                mrot1="rot4-blue.png"
            mcolor1="lime"
        if (vm1==0):
            mrot1="blue.png"
            mcolor1="red"
        if (vm2==1):
            if (crot==1):
                mrot2="rot1-blue.png"
            if (crot==2):
                mrot2="rot2-blue.png"
            if (crot==3):
                mrot2="rot3-blue.png"
            if (crot==4):
                mrot2="rot4-blue.png"
            mcolor2="lime"
        if (vm2==0):
            mrot2="blue.png"
            mcolor2="red"
        if (vc1==1):
            mcil1="cil-acionado-blue.jpg"
            mcolor3="lime"
        if (vc1==0):
            mcil1="cil-desacionado-blue.jpg"
            mcolor3="red"
        if (vc2==1):
            mcil2="cil-acionado-blue.jpg"
            mcolor4="lime"
        if (vc2==0):
            mcil2="cil-desacionado-blue.jpg"
            mcolor4="red"
        if (vc3==1):
            mcil3="cil-acionado-blue.jpg"
            mcolor5="lime"
        if (vc3==0):
            mcil3="cil-desacionado-blue.jpg"
            mcolor5="red"
        if (vc4==1):
            mcil4="cil-acionado-blue.jpg"
            mcolor6="lime"
        if (vc4==0):
            mcil4="cil-desacionado-blue.jpg"
            mcolor6="red"
        print('entro mod1')
        prog()
        templateData={
            'mcindv1':mcindv1,
            'mcindv2':mcindv2,
            'mcindv3':mcindv3,
            'mcindv4':mcindv4,
            'mctotal':mctotal,
            'mtime':mtime,
            'mc1':mc1,
            'mc2':mc2,
            'mc3':mc3,
            'mc4':mc4,
            'mm1':mm1,
            'mm2':mm2,
            'mrot1':mrot1,
            'mrot2':mrot2,
            'mcil1':mcil1,
            'mcil2':mcil2,
            'mcil3':mcil3,
            'mcil4':mcil4,
            'mcolor1':mcolor1,
            'mcolor2':mcolor2,
            'mcolor3':mcolor3,
            'mcolor4':mcolor4,
            'mcolor5':mcolor5,
            'mcolor6':mcolor6
        }
        return render_template('mod1.html', **templateData)
    @app.route("/vm2l")
    def vm2l():
        global mod
        global mcindv1
        global mcindv2
        global mcindv3
        global mcindv4
        global mctotal
        global cindv1
        global cindv2
        global cindv3
        global cindv4
        global ctotal
        global mtime
        global mc1
        global mc2
        global mc3
        global mc4
        global mm1
        global mm2
        global vc1
        global vc2
        global vc3
        global vc4
        global vm1
        global vm2
        global crot
        global mrot1
        global mrot2
        global mcil1
        global mcil2
        global mcil3
        global mcil4
        global mcolor1
        global mcolor2
        global mcolor3
        global mcolor4
        global mcolor5
        global mcolor6
        mod=1
        vm2=1
        crot=crot+1
        if (crot==4):
            crot=1
        if (vm1==1):
            if (crot==1):
                mrot1="rot1-blue.png"
            if (crot==2):
                mrot1="rot2-blue.png"
            if (crot==3):
                mrot1="rot3-blue.png"
            if (crot==4):
                mrot1="rot4-blue.png"
            mcolor1="lime"
        if (vm1==0):
            mrot1="blue.png"
            mcolor1="red"
        if (vm2==1):
            if (crot==1):
                mrot2="rot1-blue.png"
            if (crot==2):
                mrot2="rot2-blue.png"
            if (crot==3):
                mrot2="rot3-blue.png"
            if (crot==4):
                mrot2="rot4-blue.png"
            mcolor2="lime"
        if (vm2==0):
            mrot2="blue.png"
            mcolor2="red"
        if (vc1==1):
            mcil1="cil-acionado-blue.jpg"
            mcolor3="lime"
        if (vc1==0):
            mcil1="cil-desacionado-blue.jpg"
            mcolor3="red"
        if (vc2==1):
            mcil2="cil-acionado-blue.jpg"
            mcolor4="lime"
        if (vc2==0):
            mcil2="cil-desacionado-blue.jpg"
            mcolor4="red"
        if (vc3==1):
            mcil3="cil-acionado-blue.jpg"
            mcolor5="lime"
        if (vc3==0):
            mcil3="cil-desacionado-blue.jpg"
            mcolor5="red"
        if (vc4==1):
            mcil4="cil-acionado-blue.jpg"
            mcolor6="lime"
        if (vc4==0):
            mcil4="cil-desacionado-blue.jpg"
            mcolor6="red"
        print('entro mod1')
        prog()
        templateData={
            'mcindv1':mcindv1,
            'mcindv2':mcindv2,
            'mcindv3':mcindv3,
            'mcindv4':mcindv4,
            'mctotal':mctotal,
            'mtime':mtime,
            'mc1':mc1,
            'mc2':mc2,
            'mc3':mc3,
            'mc4':mc4,
            'mm1':mm1,
            'mm2':mm2,
            'mrot1':mrot1,
            'mrot2':mrot2,
            'mcil1':mcil1,
            'mcil2':mcil2,
            'mcil3':mcil3,
            'mcil4':mcil4,
            'mcolor1':mcolor1,
            'mcolor2':mcolor2,
            'mcolor3':mcolor3,
            'mcolor4':mcolor4,
            'mcolor5':mcolor5,
            'mcolor6':mcolor6
        }
        return render_template('mod1.html', **templateData)
    @app.route("/vm2d")
    def vm2d():
        global mod
        global mcindv1
        global mcindv2
        global mcindv3
        global mcindv4
        global mctotal
        global cindv1
        global cindv2
        global cindv3
        global cindv4
        global ctotal
        global mtime
        global mc1
        global mc2
        global mc3
        global mc4
        global mm1
        global mm2
        global vc1
        global vc2
        global vc3
        global vc4
        global vm1
        global vm2
        global crot
        global mrot1
        global mrot2
        global mcil1
        global mcil2
        global mcil3
        global mcil4
        global mcolor1
        global mcolor2
        global mcolor3
        global mcolor4
        global mcolor5
        global mcolor6
        mod=1
        vm2=0
        crot=crot+1
        if (crot==4):
            crot=1
        if (vm1==1):
            if (crot==1):
                mrot1="rot1-blue.png"
            if (crot==2):
                mrot1="rot2-blue.png"
            if (crot==3):
                mrot1="rot3-blue.png"
            if (crot==4):
                mrot1="rot4-blue.png"
            mcolor1="lime"
        if (vm1==0):
            mrot1="blue.png"
            mcolor1="red"
        if (vm2==1):
            if (crot==1):
                mrot2="rot1-blue.png"
            if (crot==2):
                mrot2="rot2-blue.png"
            if (crot==3):
                mrot2="rot3-blue.png"
            if (crot==4):
                mrot2="rot4-blue.png"
            mcolor2="lime"
        if (vm2==0):
            mrot2="blue.png"
            mcolor2="red"
        if (vc1==1):
            mcil1="cil-acionado-blue.jpg"
            mcolor3="lime"
        if (vc1==0):
            mcil1="cil-desacionado-blue.jpg"
            mcolor3="red"
        if (vc2==1):
            mcil2="cil-acionado-blue.jpg"
            mcolor4="lime"
        if (vc2==0):
            mcil2="cil-desacionado-blue.jpg"
            mcolor4="red"
        if (vc3==1):
            mcil3="cil-acionado-blue.jpg"
            mcolor5="lime"
        if (vc3==0):
            mcil3="cil-desacionado-blue.jpg"
            mcolor5="red"
        if (vc4==1):
            mcil4="cil-acionado-blue.jpg"
            mcolor6="lime"
        if (vc4==0):
            mcil4="cil-desacionado-blue.jpg"
            mcolor6="red"
        print('entro mod1')
        prog()
        templateData={
            'mcindv1':mcindv1,
            'mcindv2':mcindv2,
            'mcindv3':mcindv3,
            'mcindv4':mcindv4,
            'mctotal':mctotal,
            'mtime':mtime,
            'mc1':mc1,
            'mc2':mc2,
            'mc3':mc3,
            'mc4':mc4,
            'mm1':mm1,
            'mm2':mm2,
            'mrot1':mrot1,
            'mrot2':mrot2,
            'mcil1':mcil1,
            'mcil2':mcil2,
            'mcil3':mcil3,
            'mcil4':mcil4,
            'mcolor1':mcolor1,
            'mcolor2':mcolor2,
            'mcolor3':mcolor3,
            'mcolor4':mcolor4,
            'mcolor5':mcolor5,
            'mcolor6':mcolor6
        }
        return render_template('mod1.html', **templateData)
    @app.route("/mod0")
    def mod0():
        global mod
        global cindv1
        global cindv2
        global cindv3
        global cindv4
        global ctotal
        global mcindv1
        global mcindv2
        global mcindv3
        global mcindv4
        global mctotal
        global mem
        global ms
        global cn
        global cr
        cn=0
        cr=0
        cindv1=0
        cindv2=0
        cindv3=0
        cindv4=0
        ctotal=0
        mcindv1=0
        mcindv2=0
        mcindv3=0
        mcindv4=0
        mctotal=0
        mem=0
        ms=0
        mod=0    
        print('entro mod0')
        #prog()
        return render_template('mod0.html')
    ##======================   Rotina Processamento   ===================##
    def prog():
        global mem
        global ms
        global aux1
        global aux2
        global aux3
        global aux4
        global aux5
        global aux6
        global aux7
        global aux8
        global mod
        global vc1
        global vc2
        global vc3
        global vc4
        global vm1
        global vm2
        global vbot
        global s1
        global s2
        global s3
        global sc1
        global sc2
        global sc3
        global sc4
        global c1
        global c2
        global c3
        global c4
        global m1
        global m2
        global t1
        global t2
        global t3
        global t4
        global tp
        global cindv1
        global cindv2
        global cindv3
        global cindv4
        global ctotal
        global bot
        global mmem
        global mms
        global mc1
        global mc2
        global mc3
        global mc4
        global mm1
        global mm2
        global mmt
        global mtime
        global auxmod1
        global auxmod2
        global auxmod3
        global auxmod4
        global mcindv1
        global mcindv2
        global mcindv3
        global mcindv4
        global mctotal
        global cn
        global cr
        now=datetime.datetime.now()
        mtime=now.strftime("%d de %m de %Y, %H:%M:%S")
        if (mod==0):
            mod=0
            cilindro_03 = (False)
            cilindro_04 = (False)
            motor_01 = (False)
            motor_02 = (False)
            cilindro_01 = (False)
            cilindro_02 = (False)
            vm1=0
            vm2=0
            vc1=0
            vc3=0
            vc4=0
            mem=0
            ms=0
            ###mod=int(input('Selecione o modo manual (1) ou Automatico (2)'                
        if (mod==1):
            mod=1
            #vc1=int(input('digite vc1: '))
            #vc2=int(input('digite vc2: '))
            #vc3=int(input('digite vc3: '))
            #vc4=int(input('digite vc4: '))
            #vm1=int(input('digite vm1: '))
            #vm2=int(input('digite vm2: '))
            #vbot=int(input('digite 1 para parar: '))
            if(vc1==1 and vbot==0):
                mc1="Ligado"
                cilindro_01 = (True)
                if auxmod1==0:
                    auxmod1=1
                    cindv1=cindv1+1
                    mcindv1=str(cindv1)
                    ctotal=ctotal+1
                    mctotal=str(ctotal)
            if(vc2==1 and vbot==0):
                mc2="Ligado"
                cilindro_02 = (True)
                if auxmod2==0:
                    auxmod2=1
                    cindv2=cindv2+1
                    mcindv2=str(cindv2)
                    ctotal=ctotal+1
                    mctotal=str(ctotal)
            if(vc3==1 and vbot==0):
                mc3="Ligado"
                cilindro_03 = (True)
                if auxmod3==0:
                    auxmod3=1
                    cindv3=cindv3+1
                    mcindv3=str(cindv3)
                    ctotal=ctotal+1
                    mctotal=str(ctotal)
            if(vc4==1 and vbot==0):
                mc4="Ligado"
                cilindro_04 = (True)
                if auxmod4==0:
                    auxmod4=1
                    cindv4=cindv4+1
                    mcindv4=str(cindv4)
                    ctotal=ctotal+1
                    mctotal=str(ctotal)
            if(vc1==0):
                mc1="Desligado"
                cilindro_01 = (False)
                auxmod1=0
            if(vc2==0):
                mc2="Desligado"
                cilindro_02 = (False)
                auxmod2=0
            if(vc3==0):
                mc3="Desligado"
                cilindro_03 = (False)
                auxmod3=0
            if(vc4==0):
                mc4="Desligado"
                cilindro_04 = (False)
                auxmod4=0
            if(vm1==1 and vbot==0):
                mm1="Ligado"
                motor_01 = (True)
            if(vm2==1 and vbot==0):
                mm2="Ligado"
                motor_02 = (True)
            if(vm1==0):
                mm1="Desligado"
                motor_01 = (False)
            if(vm2==0):
                mm2="Desligado"
                motor_02 = (False)
            if(vbot==1):
                motor_01 = (False)
                motor_02 = (False)
                vc1=0
                vc2=0
                vc3=0
                vc4=0
                vm1=0
                vm2=0
                c1=0
                c2=0
                c3=0
                c4=0
                mm1="Desligado"
                mm2="Desligado"
                mc1="Desligado"
                mc2="Desligado"
                mc3="Desligado"
                mc4="Desligado"
                vbot=0#No caso do manual so para quando clica o botao, depois retorna a receber valores nas variaveis
        if (mod==3):
            mod=3
            time.sleep(0.001)
            sc1=sensor_avanco_cilindro_01
            if (sc1==1):
                print('sc1')
                cilindro_01 = (True)
            if (sensor_avanco_cilindro_02==True):
                print('sc2')
                cilindro_02 = (True)
            if (sensor_avanco_cilindro_03==True):
                print('sc3')
                cilindro_03 = (True)
            if (sensor_avanco_cilindro_04==True):
                print('sc4')
                cilindro_04 = (True)
            if (sensor_baixo==True):
                print('s1')
                motor_01 = (True)
            if (sensor_alto==True):
                print('s2')
                motor_02 = (True)
            if (sensor_metal==True):
                print('s3')
                motor_01 = (False)
                motor_02 = (False)
                cilindro_01 = (False)
                cilindro_02 = (False)
                cilindro_03 = (False)
                cilindro_04 = (False)
            
        if (mod==2):
            mod=2
            print('Memoria: ')
            print(mem)
            print('Casas de memoria utilizadas: ')
            print(ms)
            mmem=str(mem)
            mms=str(ms)
            if (c1==0) and (c2==0) and (c3==0) and (c4==0) and vbot==0:
                motor_01 = (True)
                motor_02 = (True)
                vm1=1
                vm2=1
                vc1=0
                vc2=0
                vc3=0
                vc4=0
                mm1="Ligado"
                mm2="Ligado"
                mc1="Desligado"
                mc2="Desligado"
                mc3="Desligado"
                mc4="Desligado"
            if (c1==1 and vbot==0):
                cilindro_01 = (True)
                motor_01 = (False)
                motor_02 = (False)
                vc1=1
                vm1=0
                vm2=0
                mc1="Ligado"
                mm1="Desligado"
                mm2="Desligado"
            if (c2==1 and vbot==0):
                cilindro_02 = (True)
                motor_01 = (False)
                motor_02 = (False)
                mc2="Ligado"
                vc2=1
                vm1=0
                vm2=0
                mm1="Desligado"
                mm2="Desligado"
            if (c3==1 and vbot==0):
                mc3="Ligado"
                mm1="Desligado"
                mm2="Desligado"
                vc3=1
                vm1=0
                vm2=0
                cilindro_03 = (True)
                motor_01 = (False)
                motor_02 = (False)
            if (c4==1 and vbot==0):
                cilindro_04 = (True)
                motor_01 = (False)
                motor_02 = (False)
                vc4=1
                vm1=0
                vm2=0
                mc4="Ligado"
                mm1="Desligado"
                mm2="Desligado"
            #print('Memoria: ')
            #print(mem)
            #print('Casas de memoria utilizadas: ')
            #print(ms)
            print("Digite o valor lógico para os sensores: baixo, alto, metal (em sequência) Ex:111")
            sensor_baixo, sensor_alto, sensor_metal = input()
            #s1=int(input('digite s1: '))
            #s2=int(input('digite s2: '))
            #s3=int(input('digite s3: '))
            #sc1=int(input('digite sc1: '))
            #sc2=int(input('digite sc2: '))
            #sc3=int(input('digite sc3: '))
            #sc4=int(input('digite sc4: '))
            #vbot=int(input('digite 1 para parar: '))
            #t1=int(input('digite t1'))
            #t2=int(input('digite t2'))
            #t3=int(input('digite t3'))
            #t4=int(input('digite t4'))
            if ((sensor_baixo==1) and (sensor_alto==0) and (sensor_metal==0) and (aux1==0)):##não metal baixa
                aux1=1
            if ((sensor_baixo==1) and (sensor_alto==1) and (sensor_metal==0) and (aux2==0)):##não metal alta
                aux2=1
            if ((sensor_baixo==1) and (sensor_alto==0) and (sensor_metal==1) and (aux3==0)):##metal baixa
                aux3=1
            if ((sensor_baixo==1) and (sensor_alto==1) and (sensor_metal==1) and (aux4==0)):##metal alta
                aux4=1
            if (sensor_baixo==0 and sensor_alto==0 and sensor_metal==0):
                if(aux1==1 and aux2==0 and aux3==0 and aux4==0):
                    aux1=0
                    mmt="Caixa baixa nao metalica"
                    cn=1
                    ms=ms+1
                    if (ms==10):
                        mem=mem+1
                    if (ms==9):
                        mem=mem+10
                    if (ms==8):
                        mem=mem+100
                    if (ms==7):
                        mem=mem+1000
                    if (ms==6):
                        mem=mem+10000
                    if (ms==5):
                        mem=mem+100000
                    if (ms==4):
                        mem=mem+1000000
                    if (ms==3):
                        mem=mem+10000000
                    if (ms==2):
                        mem=mem+100000000
                    if (ms==1):
                        mem=mem+1000000000
                if((aux1==1 and aux2==1 and aux3==0 and aux4==0) or (aux1==0 and aux2==1 and aux3==0 and aux4==0)):
                    aux1=0
                    aux2=0
                    mmt="Caixa alta nao metalica "
                    cn=2
                    ms=ms+1
                    if (ms==10):
                        mem=mem+2
                    if (ms==9):
                        mem=mem+20
                    if (ms==8):
                        mem=mem+200
                    if (ms==7):
                        mem=mem+2000
                    if (ms==6):
                        mem=mem+20000
                    if (ms==5):
                        mem=mem+200000
                    if (ms==4):
                        mem=mem+2000000
                    if (ms==3):
                        mem=mem+20000000
                    if (ms==2):
                        mem=mem+200000000
                    if (ms==1):
                        mem=mem+2000000000
                if((aux1==1 and aux2==0 and aux3==1 and aux4==0) or (aux1==0 and aux2==0 and aux3==1 and aux4==0)):
                    aux1=0
                    aux3=0
                    mmt="Caixa baixa metalica    "
                    cn=3
                    ms=ms+1
                    if (ms==10):
                        mem=mem+3
                    if (ms==9):
                        mem=mem+30
                    if (ms==8):
                        mem=mem+300
                    if (ms==7):
                        mem=mem+3000
                    if (ms==6):
                        mem=mem+30000
                    if (ms==5):
                        mem=mem+300000
                    if (ms==4):
                        mem=mem+3000000
                    if (ms==3):
                        mem=mem+30000000
                    if (ms==2):
                        mem=mem+300000000
                    if (ms==1):
                        mem=mem+3000000000
                if(aux4==1):
                    aux1=0
                    aux2=0
                    aux3=0
                    aux4=0
                    mmt="Caixa alta metalica     "
                    cn=4
                    ms=ms+1
                    if (ms==10):
                        mem=mem+4
                    if (ms==9):
                        mem=mem+40
                    if (ms==8):
                        mem=mem+400
                    if (ms==7):
                        mem=mem+4000
                    if (ms==6):
                        mem=mem+40000
                    if (ms==5):
                        mem=mem+400000
                    if (ms==4):
                        mem=mem+4000000
                    if (ms==3):
                        mem=mem+40000000
                    if (ms==2):
                        mem=mem+400000000
                    if (ms==1):
                        mem=mem+4000000000
            if (sensor_avanco_cilindro_01==1 and aux5==0):
                aux5=1
            if (sensor_avanco_cilindro_02==1 and aux6==0):
                aux6=1
            if (sensor_avanco_cilindro_03==1 and aux7==0):
                aux7=1
            if (sensor_avanco_cilindro_04==1 and aux8==0):
                aux8=1
            if (sensor_avanco_cilindro_01==0 and aux5==1 and t1==0):
                aux5=0
                if (mem==1):
                    mem=mem-1
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t1=1
                    timer1()
                if (mem>=10 and mem<=19):
                    mem=mem-10
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t1=1
                    timer1()
                if (mem>=100 and mem<=199):
                    mem=mem-100
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t1=1
                    timer1()
                if (mem>=1000 and mem<=1999):
                    mem=mem-1000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t1=1
                    timer1()
                if (mem>=10000 and mem<=19999):
                    mem=mem-10000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t1=1
                    timer1()
                if (mem>=100000 and mem<=199999):
                    mem=mem-100000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t1=1
                    timer1()
                if (mem>=1000000 and mem<=1999999):
                    mem=mem-1000000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t1=1
                    timer1()
                if (mem>=10000000 and mem<=19999999):
                    mem=mem-10000000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t1=1
                    timer1()
                if (mem>=100000000 and mem<=199999999):
                    mem=mem-100000000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t1=1
                    timer1()
                if (mem>=1000000000 and mem<=1999999999):
                    mem=mem-1000000000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t1=1
                    timer1()
            if (sensor_avanco_cilindro_02==0 and aux6==1 and t2==0):
                aux6=0
                if (mem==2):
                    mem=mem-2
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t2=1
                    timer2()
                if (mem>=20 and mem<=29):
                    mem=mem-20
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t2=1
                    timer2()
                if (mem>=200 and mem<=299):
                    mem=mem-200
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t2=1
                    timer2()
                if (mem>=2000 and mem<=2999):
                    mem=mem-2000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t2=1
                    timer2()
                if (mem>=20000 and mem<=29999):
                    mem=mem-20000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t2=1
                    timer2()
                if (mem>=200000 and mem<=299999):
                    mem=mem-200000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t2=1
                    timer2()
                if (mem>=2000000 and mem<=2999999):
                    mem=mem-2000000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t2=1
                    timer2()
                if (mem>=20000000 and mem<=29999999):
                    mem=mem-20000000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t2=1
                    timer2()
                if (mem>=200000000 and mem<=299999999):
                    mem=mem-200000000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t2=1
                    timer2()
                if (mem>=2000000000 and mem<=2999999999):
                    mem=mem-2000000000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t2=1
                    timer2()
            if (sensor_avanco_cilindro_03==0 and aux7==1 and t3==0):
                aux7=0
                if (mem==3):
                    mem=mem-3
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t3=1
                    timer3()
                if (mem>=30 and mem<=39):
                    mem=mem-30
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t3=1
                    timer3()
                if (mem>=300 and mem<=399):
                    mem=mem-300
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t3=1
                    timer3()
                if (mem>=3000 and mem<=3999):
                    mem=mem-3000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t3=1
                    timer3()
                if (mem>=30000 and mem<=39999):
                    mem=mem-30000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t3=1
                    timer3()
                if (mem>=300000 and mem<=399999):
                    mem=mem-300000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t3=1
                    timer3()
                if (mem>=3000000 and mem<=3999999):
                    mem=mem-3000000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t3=1
                    timer3()
                if (mem>=30000000 and mem<=39999999):
                    mem=mem-30000000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t3=1
                    timer3()
                if (mem>=300000000 and mem<=399999999):
                    mem=mem-300000000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t3=1
                    timer3()
                if (mem>=3000000000 and mem<=3999999999):
                    mem=mem-3000000000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t3=1
                    timer3()
            if (sensor_avanco_cilindro_04==0 and aux8==1 and t4==0):
                aux8=0
                if (mem==4):
                    mem=mem-4
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t4=1
                    timer4()
                if (mem>=40 and mem<=49):
                    mem=mem-40
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t4=1
                    timer4()
                if (mem>=400 and mem<=499):
                    mem=mem-400
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t4=1
                    timer4()
                if (mem>=4000 and mem<=4999):
                    mem=mem-4000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t4=1
                    timer4()
                if (mem>=40000 and mem<=49999):
                    mem=mem-40000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t4=1
                    timer4()
                if (mem>=400000 and mem<=499999):
                    mem=mem-400000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t4=1
                    timer4()
                if (mem>=4000000 and mem<=4999999):
                    mem=mem-4000000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t4=1
                    timer4()
                if (mem>=40000000 and mem<=49999999):
                    mem=mem-40000000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t4=1
                    timer4()
                if (mem>=400000000 and mem<=499999999):
                    mem=mem-400000000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t4=1
                    timer4()
                if (mem>=4000000000 and mem<=4999999999):
                    mem=mem-4000000000
                    mem=mem*10##correcao casas da memoria
                    ms=ms-1
                    #t4=1
                    timer4()
            if (ms>10):
                print('Erro: Memoria cheia')
                mmem="Erro: Memoria cheia"
                motor_01 = (False)
                motor_02 = (False)
                vm1=0
                vm2=0
                mm1="Desligado"
                mm2="Desligado"
            if(vbot==1):
                motor_01 = (False)
                motor_02 = (False)
                c1=0
                c2=0
                c3=0
                c4=0
                mm1="Desligado"
                mm2="Desligado"
                mc1="Desligado"
                mc2="Desligado"
                mc3="Desligado"
                mc4="Desligado"
                vm1=0
                vm2=0
                vc1=0
                vc2=0
                vc3=0
                vc4=0
        if (t1>=1):
            timer1()
        if (t2>=1):
            timer2()
        if (t3>=1):
            timer3()
        if (t4>=1):
            timer4()
        return()
    app.run(host='', port=5000, debug=True)
