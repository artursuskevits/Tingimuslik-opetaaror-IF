from base64 import b16decode
from math import *

#try: #task 1
#    name = (input("what is your name? "))
#    if name.lower() == "juku" :
#        print("Lähme kinno")
#        vanus = int(input("kui vana sa oled? "))
#        if vanus>=0 or vanus <=100:
#            print("viga andmetega")
#        elif vanus <6:
#            print("tasuta")
#        elif vanus>=6 and vanus <=14:
#            print("lastepilet")
#        elif vanus>=15 and vanus <65:
#            print("täispilet")
#        elif vanus>=65:
#            print("sooduspilet")
#    else:
#        print("Otsime Juku")
#except:
#    print("Vale Andmetüb") 
   

#nimi1 = input("mis on sinu nimi ?") #task2
#nimi2 = input("ja mis on sinu nimi? ")
#if nimi1.isalpha() and nimi2.isalpha():
#    if nimi1.lower()=="dilan" and nimi2.lower()=="artur":
#        print(f"{nimi1} ja {nimi2} istute koos ")
#    elif nimi1.lower()=="artur" and nimi2.lower()=="dilan":
#        print(f"{nimi1} ja {nimi2} istute koos ")
#    else:
#        print("wrong names")
#else:
#    print("viga!")


#try: #task3
#    a = float(input("külje pikkus a? ")) 
#    b = float(input("külje pikkus b? "))
#    if a>0 and b>0:
#        S=round(a*b,2)
#        print(f"põrandapind = {S}m2")
#        answer = int(input("soovite remonti teha? 1-jah, other-ei?"))
#        if answer==1:
#            metr=float(input("kui palju on ruutmeeter"))
#            if a>0:
#                cost= round(S*metr,2)
#                print (f"remont costa={cost} eurot")
#            else:
#                print("viga")
#        else:
#            print("kui kahju")
#    else:
#        print("viga")
#except:
#    print("viga")

#try: #task4
#    maksab = float(input("mis hinna on ? "))
#    if maksab >0:
#        if maksab > 700:
#            hinna = (maksab*0.7,2)
#            print(f"Soodushind on {hinna} ")
#        else:
#            print("viga")
#    else: 
#        print("viga")
#except:
#    print("viga")

#try: #task5
#    temperatuur = float(input("mis temepreatuur on? "))
#    if temperatuur >18:
#        print("see on hea temperatuur")
#    else:
#        print("see ei ole hea temperatuur")
#except:
#    print("viga")



#try: #task7
#    sugu= int(input("kas sa oled tüdrukud 1-JAH, OTHER - NO"))
#    if sugu==1:
#        pikkus = float(input("mis on sinu pikkus? "))
#        if pikkus <100 or pikkus >250:
#            if pikkus >100:
#                print ("sa oled madal")
#            elif pikkus >=160 and pikkus <=180:
#                print ("sa oled keskmine")
#            elif pikkus >180:
#                print ("sa oled kõrge")
#        else:("vale pikkus")
#    else:
#        pikkus = float(input("mis on sinu pikkus? "))
#        if pikkus <100 or pikkus >250:
#            if pikkus >100:
#                print ("sa oled madal")
#            elif pikkus >=170and pikkus <=185:
#                print ("sa oled keskmine")
#            elif pikkus >190:
#                print ("sa oled kõrge")
#        else:("vale pikkus")
#except:
#    print("viga")

try: #task6
    pikkus = float(input("mis on sinu pikkus? "))
    if pikkus <100 or pikkus >250:
        if  pikkus >100 and pikkus<160:
            print ("sa oled madal")
        elif pikkus >=160 and pikkus <=180:
            print ("sa oled keskmine")
        elif pikkus >180 and pikkus < 250:
            print ("sa oled kõrge")
    else:("vale pikkus")
except:
    print("viga")