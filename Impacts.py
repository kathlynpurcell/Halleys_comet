# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:30:28 2020

@author: kpurc
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 22:06:47 2020

@author: kpurc
"""

"""
HALLEYS COMET
"""

import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation
import numpy as np


pi = math.pi #pi
P = 3963 #3962.86 #weeks
tp = 0
t = 0 #time steps in weeks
e= 0.967
rp = 0.587 #AU
a = 17.78788 #AU
ra = 34.98876 #AU
tr = 3963 #timestep

#1
M = []
while t < tr:
    M.append(2*pi*(((t-tp)%P)/P))
    t = t+1

#2
n=0
En2=[]
t=0   
while t< tr:
    n=0
    En = M[t]
    while n < 100:
        En1 = En-((En-e*math.sin(En)-M[t])/(1-e*math.cos(En)))
        En = En1
        n = n+1
    En2.append(En1)
    t=t+1

#3a
Q=[]
t=0
while t < tr:
    Q.append((math.sqrt((1-e)/(1+e)))*math.tan(En2[t]/2))
    t=t+1
   
#3b THIS IS IN RAD
t=0
H=[]
while t < tr:
    H.append(math.atan(Q[t])*2)
    t=t+1

#4
t=0
rt=[]
while t< tr:
    rt.append((a*(1-e**2))/(1+e*math.cos(H[t])))
    t=t+1

#making the x,y coordinate system
t=0
xH=[]
yH=[]
while t < tr:
        xH.append(rt[t]*math.cos(H[t]))
        yH.append(rt[t]*math.sin(H[t]))
        t=t+1
        
#plt.scatter(xH, yH, label='Halleys Comet')

        

"""
EARTH
"""

import matplotlib.pyplot as plt
import math


pi = math.pi #pi
P = 52 #52.1429 #weeks
tp = 0
t = 0 #time steps in weeks
e= 0.0167

#find rp, ra and a
rp = 0.9832899 #AU
a = rp/(1-e) #AU
ra = a*(1+e) #AU

#1
M = []
while t < tr:
    M.append(2*pi*(((t-tp)%P)/P))
    t = t+1

#2
n=0
En2=[]
t=0   
while t<tr:
    n=0
    En = M[t]
    while n < 100:
        En1 = En-((En-e*math.sin(En)-M[t])/(1-e*math.cos(En)))
        En = En1
        n = n+1
    En2.append(En1)
    t=t+1

#3a
Q=[]
t=0
while t < tr:
    Q.append((math.sqrt((1-e)/(1+e)))*math.tan(En2[t]/2))
    t=t+1
   
#3b THIS IS IN RAD
t=0
H=[]
while t < tr:
    H.append(math.atan(Q[t])*2)
    t=t+1

#4
t=0
rt=[]
while t<tr:
    rt.append((a*(1-e**2))/(1+e*math.cos(H[t])))
    t=t+1

#making the x,y coordinate system
t=0
xE=[]
yE=[]
while t < tr:
        xE.append(rt[t]*math.cos(H[t]))
        yE.append(rt[t]*math.sin(H[t]))
        t=t+1
        
#plt.scatter(xE, yE, label='Earth')



"""
MARS
"""

import matplotlib.pyplot as plt
import math


pi = math.pi #pi
P = 98 #98.1 #weeks
tp = 0
t = 0 #time steps in weeks
e= 0.0934

#find rp, ra and a
rp = 1.38 #AU
a = rp/(1-e) #AU
ra = a*(1+e) #AU

#1
M = []
while t < tr:
    M.append(2*pi*(((t-tp)%P)/P))
    t = t+1

#2
n=0
En2=[]
t=0   
while t<tr:
    n=0
    En = M[t]
    while n < 100:
        En1 = En-((En-e*math.sin(En)-M[t])/(1-e*math.cos(En)))
        En = En1
        n = n+1
    En2.append(En1)
    t=t+1

#3a
Q=[]
t=0
while t < tr:
    Q.append((math.sqrt((1-e)/(1+e)))*math.tan(En2[t]/2))
    t=t+1
   
#3b THIS IS IN RAD
t=0
H=[]
while t < tr:
    H.append(math.atan(Q[t])*2)
    t=t+1

#4
t=0
rt=[]
while t<tr:
    rt.append((a*(1-e**2))/(1+e*math.cos(H[t])))
    t=t+1

#making the x,y coordinate system
t=0
xM=[]
yM=[]
while t < tr:
        xM.append(rt[t]*math.cos(H[t]))
        yM.append(rt[t]*math.sin(H[t]))
        t=t+1
        
#plt.scatter(xM, yM, label='Mars')



"""
JUPITER
"""

import matplotlib.pyplot as plt
import math


pi = math.pi #pi
P = 620 #620 #weeks
tp = 0
t = 0 #time steps in weeks
e= 0.048

#find rp, ra and a
rp = 4.95 #AU
a = rp/(1-e) #AU
ra = a*(1+e) #AU

#1
M = []
while t < tr:
    M.append(2*pi*(((t-tp)%P)/P))
    t = t+1

#2
n=0
En2=[]
t=0   
while t<tr:
    n=0
    En = M[t]
    while n < 100:
        En1 = En-((En-e*math.sin(En)-M[t])/(1-e*math.cos(En)))
        En = En1
        n = n+1
    En2.append(En1)
    t=t+1

#3a
Q=[]
t=0
while t < tr:
    Q.append((math.sqrt((1-e)/(1+e)))*math.tan(En2[t]/2))
    t=t+1
   
#3b THIS IS IN RAD
t=0
H=[]
while t < tr:
    H.append(math.atan(Q[t])*2)
    t=t+1

#4
t=0
rt=[]
while t< tr:
    rt.append((a*(1-e**2))/(1+e*math.cos(H[t])))
    t=t+1

#making the x,y coordinate system
t=0
xJ=[]
yJ=[]
while t < tr:
        xJ.append(rt[t]*math.cos(H[t]))
        yJ.append(rt[t]*math.sin(H[t]))
        t=t+1
        
#plt.scatter(xJ, yJ, label='Jupiter')



"""
SATURN
"""

import matplotlib.pyplot as plt
import math


pi = math.pi #pi
P = 1500 # 1500 weeks
tp = 0
t = 0 #time steps in weeks
e= 0.05555

#find rp, ra and a
rp = 9.01 #AU
a = rp/(1-e) #AU
ra = a*(1+e) #AU

#1
M = []
while t < tr:
    M.append(2*pi*(((t-tp)%P)/P))
    t = t+1

#2
n=0
En2=[]
t=0   
while t< tr:
    n=0
    En = M[t]
    while n < 100:
        En1 = En-((En-e*math.sin(En)-M[t])/(1-e*math.cos(En)))
        En = En1
        n = n+1
    En2.append(En1)
    t=t+1

#3a
Q=[]
t=0
while t < tr:
    Q.append((math.sqrt((1-e)/(1+e)))*math.tan(En2[t]/2))
    t=t+1
   
#3b THIS IS IN RAD
t=0
H=[]
while t < tr:
    H.append(math.atan(Q[t])*2)
    t=t+1

#4
t=0
rt=[]
while t< tr:
    rt.append((a*(1-e**2))/(1+e*math.cos(H[t])))
    t=t+1

#making the x,y coordinate system
t=0
xS=[]
yS=[]
while t < tr:
        xS.append(rt[t]*math.cos(H[t]))
        yS.append(rt[t]*math.sin(H[t]))
        t=t+1
        
#plt.scatter(xS, yS, label='Saturn')




"""
URANUS
"""


import matplotlib.pyplot as plt
import math


pi = math.pi #pi
P = 4400 # 1500 weeks
tp = 0
t = 0 #time steps in weeks
e= 0.0473

#find rp, ra and a
rp = 18.4 #AU
a = rp/(1-e) #AU
ra = a*(1+e) #AU

#1
M = []
while t < tr:
    M.append(2*pi*(((t-tp)%P)/P))
    t = t+1

#2
n=0
En2=[]
t=0   
while t<tr:
    n=0
    En = M[t]
    while n < 100:
        En1 = En-((En-e*math.sin(En)-M[t])/(1-e*math.cos(En)))
        En = En1
        n = n+1
    En2.append(En1)
    t=t+1

#3a
Q=[]
t=0
while t < tr:
    Q.append((math.sqrt((1-e)/(1+e)))*math.tan(En2[t]/2))
    t=t+1
   
#3b THIS IS IN RAD
t=0
H=[]
while t < tr:
    H.append(math.atan(Q[t])*2)
    t=t+1

#4
t=0
rt=[]
while t<tr:
    rt.append((a*(1-e**2))/(1+e*math.cos(H[t])))
    t=t+1

#making the x,y coordinate system
t=0
xU=[]
yU=[]
while t < tr:
        xU.append(rt[t]*math.cos(H[t]))
        yU.append(rt[t]*math.sin(H[t]))
        t=t+1
    
  
#plt.scatter(xU, yU, label='Uranus')


'''

#Halley Animations

fig, ax = plt.subplots()
ln, = plt.plot([], [], 'ro') 

def init():
    ax.set_xlim(-40, 5)
    ax.set_ylim(-5, 5)
    return ln,

def update(frame):
    ln.set_data(x[:frame], y[:frame])
    return ln,

ani = FuncAnimation(fig, update, frames=np.arange(0, 3963, 70),
                    init_func=init, blit=True)
plt.scatter(x,y, 1)
plt.scatter(0,0)
plt.show()
'''






"""
###
##Near Earth Objects with respect to Orbital Radius
## How many times will Halley colide with planets?
###

#all initialized to starting potisiton of y=0, at perhelion
t=0
E, M, J, S, U = 0,0,0,0,0

#as a funcion of the period
while t < 3963:
    if (xE[t]-0.3)<= xH[t]<= (xE[t]+0.3) and (yE[t]-0.3)<= yH[t]<= (yE[t]+0.3):
        print("time:", t, "Halley:", xH[t], yH[t], "Earth:", xE[t], yE[t])
        plt.scatter(xH[t], yH[t], color='r')
        E=E+1
    if (xM[t]-.45)<= xH[t]<= (xM[t]+0.45) and (yM[t]-0.45)<= yH[t]<= (yM[t]+0.45):
        print("time:", t, "Halley:", xH[t], yH[t], "Mars:", xM[t], yM[t])
        plt.scatter(xH[t], yH[t], color='b')
        M=M+1
    if (xJ[t]-1.56)<= xH[t]<= (xJ[t]+1.56) and (yJ[t]-1.56)<= yH[t]<= (yJ[t]+1.56):
        print("time:", t, "Halley:", xH[t], yH[t], "Jupiter:", xJ[t], yJ[t])
        plt.scatter(xH[t], yH[t], color='r')
        J=J+1
    if (xS[t]-2.85)<= xH[t]<= (xS[t]+2.85) and (yS[t]-2.85)<= yH[t]<= (yS[t]+2.85):
        print("time:", t, "Halley:", xH[t], yH[t], "Saturn:", xS[t], yS[t])
        plt.scatter(xH[t], yH[t], color='r')
        S=S+1
    if (xU[t]-5.7)<= xH[t]<= (xU[t]+5.7) and (yU[t]-5.7)<= yH[t]<= (yU[t]+5.7):
        print("time:", t, "Halley:", xH[t], yH[t], "Uranus:", xU[t], yU[t])
        plt.scatter(xH[t], yH[t], color='r')
        U=U+1
    t = t+1
    
print("E", E, 'M', M, 'J', J, 'S', S, 'U', U)
plt.scatter(xH, yH, 1, label='Halleys Comet')
plt.scatter(xE, yE, 1, label='Earth')
plt.scatter(xM, yM, 1, label='Mars')
plt.scatter(xJ, yJ, 1, label='Jupiter')
plt.scatter(xS, yS, 1, label='Saturn')
plt.scatter(xU, yU, 1, label='Uranus')
    
plt.scatter(0,0, label='Sun')
plt.legend(loc='upper center', ncol=3, fancybox=True)
plt.xlabel('Distance in AU')
plt.ylabel('Distance in AU')
plt.xlim(right=3, left=-3)
plt.ylim(bottom=-3, top=3)
plt.show()
"""

###
###Direct Hits
####Same as above block but with no 'nearby' radius
###
t=0
E, M, J, S, U = 0,0,0,0,0
while t < tr:
    if (xE[t]-0)<= xH[t]<= (xE[t]+0) and (yE[t]-0)<= yH[t]<= (yE[t]+0):
        print("time:", t, "Halley:", xH[t], yH[t], "Earth:", xE[t], yE[t])
        plt.scatter(xH[t], yH[t], color='r')
        E=E+1
    if (xM[t])<= xH[t]<= (xM[t]+0) and (yM[t]-0)<= yH[t]<= (yM[t]+0):
        print("time:", t, "Halley:", xH[t], yH[t], "Mars:", xM[t], yM[t])
        plt.scatter(xH[t], yH[t], color='b')
        M=M+1
    if (xJ[t])<= xH[t]<= (xJ[t]) and (yJ[t])<= yH[t]<= (yJ[t]):
        print("time:", t, "Halley:", xH[t], yH[t], "Jupiter:", xJ[t], yJ[t])
        plt.scatter(xH[t], yH[t], color='r')
        J=J+1
    if (xS[t])<= xH[t]<= (xS[t]) and (yS[t])<= yH[t]<= (yS[t]):
        print("time:", t, "Halley:", xH[t], yH[t], "Saturn:", xS[t], yS[t])
        plt.scatter(xH[t], yH[t], color='r')
        S=S+1
    if (xU[t])<= xH[t]<= (xU[t]) and (yU[t])<= yH[t]<= (yU[t]):
        print("time:", t, "Halley:", xH[t], yH[t], "Uranus:", xU[t], yU[t])
        plt.scatter(xH[t], yH[t], color='r')
        U=U+1
    t = t+1
    
print("E", E, 'M', M, 'J', J, 'S', S, 'U', U)
plt.scatter(xH, yH, 1, label='Halleys Comet')
plt.scatter(xE, yE, 1, label='Earth')
plt.scatter(xM, yM, 1, label='Mars')
plt.scatter(xJ, yJ, 1, label='Jupiter')
plt.scatter(xS, yS, 1, label='Saturn')
plt.scatter(xU, yU, 1, label='Uranus')

plt.scatter(0,0, label='Sun')
plt.legend(loc='upper center', ncol=3, fancybox=True)
plt.xlabel('Distance in AU')
plt.ylabel('Distance in AU')
plt.xlim(right=3, left=-3)
plt.ylim(bottom=-3, top=3)
plt.show()