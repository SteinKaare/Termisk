#Oppgave 2
import numpy as np
import matplotlib.pyplot as plt

R=8.314
e=2.72
T=np.arange(0,300,5)
Theta=280 #Einsteintemperatur aluminium
flist=[]
for i in range(len(T)):
    var=Theta/T[i]
    f=float(3*R*(var)**2*(e**var)/(e**var-1)**2)
    flist.append(f)

# cal K^-1 mol^-1 
C_vlist  = [0.022,0.054,0.112,0.203,0.332,0.500,0.698,0.912,1.375,1.846,2.298,2.714,3.094,3.422,3.704,3.943,4.165,4.361,4.536,4.690,4.823,4.938,5.039,5.122,5.198,5.268,5.329,5.383,5.436,5.483,5.523,5.562,5.592,5.599]
# Konverterer til J: 1 cal = 4.184 J

C_vlist_converted=[]
for i in range(len(C_vlist)):
    val=C_vlist[i]*4.184
    C_vlist_converted.append(val)

Tlist=[15,20,25,30,35,40,45,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,298,300]

plt.scatter(Tlist,C_vlist_converted, color='black', label='Eksperimentelt')
plt.plot(T,flist, color='red',label='Teori')
plt.ylabel('$c$ / J mol$^-1$ K$^-1$')
plt.xlabel('$T$ / K')
plt.title('Varmekapasitet som funksjon av temperatur')
plt.legend()
plt.show()
