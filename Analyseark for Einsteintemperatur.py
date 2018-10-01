#Analyse
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from pylab import *
from math import exp

R=8.314
L=2.0*10**5
deltam=4.6913*10**-3
T0=297.25
Tf=77
deltaQ=L*deltam
n=0.224 #moltall

#Hjelpefunksjon for neste funksjon
def E(y):
    return y/(exp(y)-1)
#Funksjon som kan regne ut nullpunkt
def rootfunction(Theta):
    return 3*n*R*(T0*E(Theta/T0)-Tf*E(Theta/Tf))-deltaQ
    
#Regner ut nullpunktet med anslått einsteintemperatur som utgangspunkt
Theta0=fsolve(rootfunction, 280)
print(Theta0)

#Løkke som beregner omtrentlig hvilke verdier for einsteintemperaturen som gir et nullpunkt  
T=np.arange(0,500,1)  
rootlist=[]  
Tlist=[]
for i in range(len(T)):
    root=rootfunction(T[i])
    if -5<root<5:
        Tlist.append(T[i])
        rootlist.append(root)
        
print(rootlist)
print(Tlist)