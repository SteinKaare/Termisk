# Dataanalyse frå labaktivitet 2 - Termisk fytsikk
import matplotlib.pyplot as plt
import numpy as np
import math
def linear_regresjon(x,y): #funksjon for lineær regresjon
    N=0
    for items in x:
        N+=1
        
    Sx=np.sum(x)
    Sy=np.sum(y)
    Sxx=(np.linalg.norm(x))**2
    Sxy=np.dot(x,y)
    Delta=N*Sxx-Sx**2
    
    a0=(Sy*Sxx-Sx*Sxy)/Delta
    a1=(N*Sxy-Sx*Sy)/Delta
    
    ny=a0+a1*x
    Dy=y-ny
    S=(np.linalg.norm(Dy))**2
    Da0=math.sqrt((1/(N-2))*((S*Sxx)/Delta))
    Da1=math.sqrt((N/(N-2))*(S/Delta))
    return(a0,a1,Da0,Da1)
    
#Legg inn alle eksperimentelle data og gjer dei om til arrays
T1=[0,60,120,180,240,300]
T1=np.array(T1)
M1=[59.142,56.963,54.868,52.782,50.761,48.90]
M1=np.array(M1)
T2=[480,540,600,660,720]
T2=np.array(T2)
M2=[44.762,43.128,41.5,39.928,38.396]
M2=np.array(M2)-6.125


#Lagar ein array som kan brukast til lineær regresjon
TR=[0,60,120,180,240,300,360,420,480,540,600,660,720]
TR=np.array(TR)


#Køyrer lineær regresjon på tala
(a0,a1,Da0,Da1) = linear_regresjon(T1,M1)
N1=a0+TR*a1

(b0,b1,Db0,Db1) = linear_regresjon(T2,M2)
N2=b0+TR*b1

#plottar eksperimentelle data og regrerte data i same graf
plt.plot(T1,M1,'ro',label="Masse før aluminiumsbit")
plt.plot(TR,N1,'k')
plt.plot(T2,M2,'bs',label="Masse etter aluminiumsbit")
plt.plot(TR,N2,'k')
plt.title('Masse til nitrogen og kopp som funksjon av tid')
plt.xlabel('$t$ / s')
plt.ylabel('$m$ / g')
plt.legend()

plt.show()

#lagar ein funksjon som returnerar deltam
def deltam(A0,A1,B0,B1,T1,T2):
    DT=(T1+T2)/2
    m1=A0+A1*DT
    m2=B0+B1*DT
    print('m1=',m1)
    print('m2=',m2)
    deltam=abs(m1-m2)
    dm1=m1-(A0+A1*(DT-0.5))
    dm2=m2-(B0+B1*(DT-5))
    print('dm1=',dm1)
    print('dm2=',dm2)
    print('m1-m2=',deltam)
    m1T1=A0+A1*T1
    m2T1=B0+B1*T1
    m1T2=A0+A1*T2
    m2T2=B0+B1*T2
    
    deltamT1=abs(m1T1-m2T1)
    deltamT2=abs(m1T2-m2T2)
    print('deltamT1=',deltamT1)
    print('deltamT2=',deltamT2)
    diffT1=abs(deltam-deltamT1)
    diffT2=abs(deltam-deltamT2)
    print('diffT1=',diffT1)
    print('diffT2=',diffT2)
    
    
deltam(a0,a1,b0,b1,360,420)


