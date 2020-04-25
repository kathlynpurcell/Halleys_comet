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
x=[]
y=[]
while t < 3963:
        x.append(rt[t]*math.cos(H[t]))
        y.append(rt[t]*math.sin(H[t]))
        t=t+1
        
#plt.scatter(x, y, label='Halleys Comet')
plt.polar(H, rt, label='Halleys Comet')
        

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
while t < 53:
    M.append(2*pi*(((t-tp)%P)/P))
    t = t+1

#2
n=0
En2=[]
t=0   
while t<53:
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
while t < 53:
    Q.append((math.sqrt((1-e)/(1+e)))*math.tan(En2[t]/2))
    t=t+1
   
#3b THIS IS IN RAD
t=0
H=[]
while t < 53:
    H.append(math.atan(Q[t])*2)
    t=t+1

#4
t=0
rt=[]
while t<53:
    rt.append((a*(1-e**2))/(1+e*math.cos(H[t])))
    t=t+1

#making the x,y coordinate system
t=0
x=[]
y=[]
while t < 52:
        x.append(rt[t]*math.cos(H[t]))
        y.append(rt[t]*math.sin(H[t]))
        t=t+1
        
#plt.scatter(x, y, label='Earth')
plt.polar(H,rt, label='Earth')


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
while t < 98:
    M.append(2*pi*(((t-tp)%P)/P))
    t = t+1

#2
n=0
En2=[]
t=0   
while t<98:
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
while t < 98:
    Q.append((math.sqrt((1-e)/(1+e)))*math.tan(En2[t]/2))
    t=t+1
   
#3b THIS IS IN RAD
t=0
H=[]
while t < 98:
    H.append(math.atan(Q[t])*2)
    t=t+1

#4
t=0
rt=[]
while t<98:
    rt.append((a*(1-e**2))/(1+e*math.cos(H[t])))
    t=t+1

#making the x,y coordinate system
t=0
x=[]
y=[]
while t < 98:
        x.append(rt[t]*math.cos(H[t]))
        y.append(rt[t]*math.sin(H[t]))
        t=t+1
        
#plt.scatter(x, y, label='Mars')
plt.polar(H,rt, label='Mars')


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
while t<620:
    rt.append((a*(1-e**2))/(1+e*math.cos(H[t])))
    t=t+1

#making the x,y coordinate system
t=0
x=[]
y=[]
while t < 620:
        x.append(rt[t]*math.cos(H[t]))
        y.append(rt[t]*math.sin(H[t]))
        t=t+1
        
#plt.scatter(x, y, label='Jupiter')
plt.polar(H,rt, label='Jupiter')


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
x=[]
y=[]
while t < 1500:
        x.append(rt[t]*math.cos(H[t]))
        y.append(rt[t]*math.sin(H[t]))
        t=t+1
        
#plt.scatter(x, y, label='Saturn')
plt.polar(H,rt, label='Saturn')



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
x=[]
y=[]
while t < 4400:
        x.append(rt[t]*math.cos(H[t]))
        y.append(rt[t]*math.sin(H[t]))
        t=t+1
    
  
#plt.scatter(x, y, label='Uranus')
plt.polar(H,rt, label='Uranus')

plt.scatter(0,0, label='Sun')
plt.legend(loc='upper center', ncol=3, fancybox=True)
plt.xlabel('Distance in AU')
plt.ylabel('Distance in AU')
#plt.xlim(right=3, left=-3)
#plt.ylim(bottom=-3, top=3)
plt.ylim([0,2])
plt.show()


'''
'''
#Halley
'''
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
