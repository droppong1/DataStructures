# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 06:28:41 2023

@author: user
"""

#Currency used is Great British Pound
Jeep = ("Wrangler","Compass","Renegade" ,"Gladiator" , "Wagooner" , "Jeep Meridian")
Volvo ={"S90","V60","Cross Country"}
Honda ={"Civic ","CR-V","Accord"}
Suzuki ={"Swift","Vitara","Ignis"}
Hyundai ={"Elantra","Sonata","Accent"}
Volkswagen ={"Golf","Passat","Tiguan"}
Porsche ={"Cayenne","Panamera","Taycan"}
Ferrari ={"FerrariS58 Italia","FerrariS59","FerrariLaFerrari" , "Ferrari Enzo", 
          " Ferrari Portofino" , "Ferrari California"}
BMW ={"BMW X2","BMW X4","BMWiX"}
carType =  (input("Please enter the car type:"))
if carType is Jeep:
    print ("The price of model Wrangler is 55.00")
    print ("The price of model Compass is 50.00")
    print ("The price of model Renegade is 35.00" )
    print("The price of Gladiator is 35.00")
    print("The price of Wagooner is 25.00")
    print("The price of Jeep Meridian is 35.00")
elif carType is Honda:
    print("The price of Civic is 45.00")
    print("The price of CR-V  is 45.00")
    print("The price of Accord is 55.00")
elif carType is Volvo:
    print("The price of S90 is 5.00")
    print("The price of V60 is 10.00")
    print("The price of Cross Country is 15.00")    
elif carType is Suzuki:
     print("The price of Swift is 20.00")
     print("The price of Vitara is 25.00")
     print("The price of Ignis is 25.00")   
elif carType is Hyundai:
    print("The price of Elantra is 15.00")
    print("The price of Sonata is 20.00")
    print("The price of Accent is 10.00")  
elif carType is Volkwagen:
    print("The price of Golf is 5.00")
    print("The price of Passat is 10.00")
    print("The price of Tiguan is 5.00")
elif carType is Porsche:
    print("The price of Cayenne is 30.00")
    print("The price of Panamera is 30.00")
    print("The price of Taycan is 60.00")
elif carType is  Ferrari:
    print("The price of FerrariS58 Italia is 75.00")
    print("The price of Ferrari599 is 75.00")
    print("The price of Ferrari LaFerrari is 85.00")
    print("The price of Ferrari Enzo is 120.00")
    print("The price of Ferrari Portofino is 70.00")
    print("The price of Ferrari California is 70.00")