# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 00:40:11 2020

@author: kpurc
"""



import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation
import numpy as np
from matplotlib import animation


###this is really long and could be MUCH shorter. It could have been done using loops, but instead I copy pasted
#### for all the planets to keep them straight in my mind when I was conceptualizing it
#### The animation could be included in the bottom, but it needs tweaking since it is jumpy



pi = math.pi #pi
P = 3963 #3962.86 #weeks
tp = 0
t = 0 #time steps in weeks
e= 0.967
rp = 0.587 #AU
a = 17.78788 #AU
ra = 34.98876 #AU

#1
M = []
while t < 3964:
    M.append(2*pi*(((t-tp)%P)/P))
    t = t+1

#2
n=0
En2=[]
t=0   
while t<3964:
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
while t < 3964:
    Q.append((math.sqrt((1-e)/(1+e)))*math.tan(En2[t]/2))
    t=t+1
   
#3b THIS IS IN RAD
t=0
H=[]
while t < 3964:
    H.append(math.atan(Q[t])*2)
    t=t+1

#4
t=0
rt=[]
while t<3964:
    rt.append((a*(1-e**2))/(1+e*math.cos(H[t])))
    t=t+1

#making the x,y coordinate system
t=0
xH=[]
yH=[]
while t < 3963:
        xH.append(rt[t]*math.cos(H[t]))
        yH.append(rt[t]*math.sin(H[t]))
        t=t+1
        
#plt.scatter(xH, yH, 1, label='Halleys Comet')

        

"""
EARTH
"""

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
while t < 3963:
    M.append(2*pi*(((t-tp)%P)/P))
    t = t+1

#2
n=0
En2=[]
t=0   
while t<3963:
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
while t < 3963:
    Q.append((math.sqrt((1-e)/(1+e)))*math.tan(En2[t]/2))
    t=t+1
   
#3b THIS IS IN RAD
t=0
H=[]
while t < 3963:
    H.append(math.atan(Q[t])*2)
    t=t+1

#4
t=0
rt=[]
while t<3963:
    rt.append((a*(1-e**2))/(1+e*math.cos(H[t])))
    t=t+1

#making the x,y coordinate system
t=0
xE=[]
yE=[]
while t < 3963:
        xE.append(rt[t]*math.cos(H[t]))
        yE.append(rt[t]*math.sin(H[t]))
        t=t+1
        
#plt.scatter(x, y, label='Earth')



"""
MARS
"""



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
while t < 3963:
    M.append(2*pi*(((t-tp)%P)/P))
    t = t+1

#2
n=0
En2=[]
t=0   
while t<3963:
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
while t < 3963:
    Q.append((math.sqrt((1-e)/(1+e)))*math.tan(En2[t]/2))
    t=t+1
   
#3b THIS IS IN RAD
t=0
H=[]
while t < 3963:
    H.append(math.atan(Q[t])*2)
    t=t+1

#4
t=0
rt=[]
while t<3963:
    rt.append((a*(1-e**2))/(1+e*math.cos(H[t])))
    t=t+1

#making the x,y coordinate system
t=0
xM=[]
yM=[]
while t < 3963:
        xM.append(rt[t]*math.cos(H[t]))
        yM.append(rt[t]*math.sin(H[t]))
        t=t+1
        
#plt.scatter(x, y, label='Mars')



"""
JUPITER
"""


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
while t < 620:
    M.append(2*pi*(((t-tp)%P)/P))
    t = t+1

#2
n=0
En2=[]
t=0   
while t<620:
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
while t < 620:
    Q.append((math.sqrt((1-e)/(1+e)))*math.tan(En2[t]/2))
    t=t+1
   
#3b THIS IS IN RAD
t=0
H=[]
while t < 620:
    H.append(math.atan(Q[t])*2)
    t=t+1

#4
t=0
rt=[]
while t< 620:
    rt.append((a*(1-e**2))/(1+e*math.cos(H[t])))
    t=t+1

#making the x,y coordinate system
t=0
xJ=[]
yJ=[]
while t < 620:
        xJ.append(rt[t]*math.cos(H[t]))
        yJ.append(rt[t]*math.sin(H[t]))
        t=t+1
        
#plt.scatter(x, y, label='Jupiter')



"""
SATURN
"""



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
while t < 1500:
    M.append(2*pi*(((t-tp)%P)/P))
    t = t+1

#2
n=0
En2=[]
t=0   
while t<1500:
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
while t < 1500:
    Q.append((math.sqrt((1-e)/(1+e)))*math.tan(En2[t]/2))
    t=t+1
   
#3b THIS IS IN RAD
t=0
H=[]
while t < 1500:
    H.append(math.atan(Q[t])*2)
    t=t+1

#4
t=0
rt=[]
while t<1500:
    rt.append((a*(1-e**2))/(1+e*math.cos(H[t])))
    t=t+1

#making the x,y coordinate system
t=0
xS=[]
yS=[]
while t < 1500:
        xS.append(rt[t]*math.cos(H[t]))
        yS.append(rt[t]*math.sin(H[t]))
        t=t+1
        
#plt.scatter(x, y, label='Saturn')




"""
URANUS
"""

pi = math.pi #pi
P = 4400 # 4400 weeks
tp = 0
t = 0 #time steps in weeks
e= 0.0473

#find rp, ra and a
rp = 18.4 #AU
a = rp/(1-e) #AU
ra = a*(1+e) #AU

#1
M = []
while t < 4400:
    M.append(2*pi*(((t-tp)%P)/P))
    t = t+1

#2
n=0
En2=[]
t=0   
while t<4400:
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
while t < 4400:
    Q.append((math.sqrt((1-e)/(1+e)))*math.tan(En2[t]/2))
    t=t+1
   
#3b THIS IS IN RAD
t=0
H=[]
while t < 4400:
    H.append(math.atan(Q[t])*2)
    t=t+1

#4
t=0
rt=[]
while t<4400:
    rt.append((a*(1-e**2))/(1+e*math.cos(H[t])))
    t=t+1

#making the x,y coordinate system
t=0
xU=[]
yU=[]
while t < 4400:
        xU.append(rt[t]*math.cos(H[t]))
        yU.append(rt[t]*math.sin(H[t]))
        t=t+1
    
  
#plt.scatter(x, y, label='Uranus')

'''
plt.scatter(0,0, label='Sun')
plt.legend(loc='upper center', ncol=3, fancybox=True)
plt.xlabel('Distance in AU')
plt.ylabel('Distance in AU')
#plt.xlim(right=3, left=-3)
#plt.ylim(bottom=-3, top=3)
plt.show()
'''

'''
'''
#Halley
'''
fig, ax = plt.subplots()
ln, = plt.plot([], [], 'ro') 

def init():
    ax.set_xlim(-40, 20)
    ax.set_ylim(-20, 20)
    return ln,

def updateH(frame):
    ln.set_data(xH[:frame], yH[:frame])
    return ln,

aniH = FuncAnimation(fig, updateH, frames=np.arange(500, 3963, 100),
                    init_func=init, blit=True)


'''
#Earth
'''
#fig, ax = plt.subplots()
ln, = plt.plot([], [], 'r-') 

def init():
    ax.set_xlim(-40, 20)
    ax.set_ylim(-20, 20)
    return ln,

def updateE(frame):
    ln.set_data(xE[:frame], yE[:frame])
    return ln,

aniE = FuncAnimation(fig, updateE, frames=np.arange(0, 52, 1),
                    init_func=init, blit=True)

'''
#Mars
'''
#fig, ax = plt.subplots()
ln, = plt.plot([], [], 'ro') 

def init():
    ax.set_xlim(-40, 20)
    ax.set_ylim(-20, 20)
    return ln,

def updateM(frame):
    ln.set_data(xM[:frame], yM[:frame])
    return ln,

aniM = FuncAnimation(fig, updateM, frames=np.arange(0, 98, 2),
                    init_func=init, blit=True)

'''
#Jupiter
'''
#fig, ax = plt.subplots()
ln, = plt.plot([], [], 'ro') 

def init():
    ax.set_xlim(-40, 20)
    ax.set_ylim(-20, 20)
    return ln,

def updateJ(frame):
    ln.set_data(xJ[:frame], yJ[:frame])
    return ln,

aniJ = FuncAnimation(fig, updateJ, frames=np.arange(0, 620, 75),
                    init_func=init, blit=True)

'''
#Saturn
'''
#fig, ax = plt.subplots()
ln, = plt.plot([], [], 'ro') 

def init():
    ax.set_xlim(-40, 20)
    ax.set_ylim(-20, 20)
    return ln,

def updateS(frame):
    ln.set_data(xS[:frame], yS[:frame])
    return ln,

aniS = FuncAnimation(fig, updateS, frames=np.arange(0, 1500, 100),
                    init_func=init, blit=True)

'''
#Uranus
'''
#fig, ax = plt.subplots()
ln, = plt.plot([], [], 'ro') 

def init():
    ax.set_xlim(-40, 20)
    ax.set_ylim(-20, 20)
    return ln,

def updateU(frame):
    ln.set_data(xU[:frame], yU[:frame])
    return ln,

aniU = FuncAnimation(fig, updateU, frames=np.arange(0, 4400, 110),
                    init_func=init, blit=True)
'''
"""
Graph
"""
plt.scatter(xH, yH, 1, label='Halleys Comet')
plt.scatter(xE, yE, 1, label='Earth')
plt.scatter(xM, yM, 1, label='Mars')
plt.scatter(xJ, yJ, 1, label='Jupiter')
plt.scatter(xS, yS, 1, label='Saturn')
plt.scatter(xU, yU, 1, label='Uranus')
plt.scatter(0,0)
plt.legend(loc='upper center', ncol=3, fancybox=True)
#aniU.save('myanimation.gif', writer='imagemagick', fps=None)
#plt.show()


