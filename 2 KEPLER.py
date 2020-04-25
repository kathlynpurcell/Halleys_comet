# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 20:13:08 2020

@author: kpurc
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy
#from scipy import stats
#from scipy import signal
import math
from matplotlib.animation import FuncAnimation

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
while t < 3963:
    M.append(2*pi*(((t-tp)%P)/P))
    t = t+1
stand = [i for i in range(3963)]
#plt.scatter(M, stand)

#2
n=0
En2=[]
t=0   
while t<3963:
    n=0
    En = M[t]
    while n < 100:
        En1 = En-((En-(e*math.sin(En))-M[t])/(1-(e*math.cos(En))))
        En = En1
        n = n+1
    En2.append(En1)
    t=t+1
#plt.scatter(En2, stand)


#3a
Q=[]
t=0
while t < 3963:
    Q.append((math.sqrt((1+e)/(1-e)))*math.tan(En2[t]/2))
    t=t+1
   
#3b THIS IS IN RAD
t=0
H=[]
while t < 3963:
    H.append(math.atan(Q[t])*2)
    t=t+1
#plt.scatter(H, stand)

#4
t=0
rt=[]
while t<3963:
    rt.append((a*(1-e**2))/(1+e*math.cos(H[t])))
    t=t+1
#plt.scatter(rt, stand)

#making the x,y coordinate system
t=0
x=[]
y=[]
while t < 3963:
        x.append(rt[t]*math.cos(H[t]))
        y.append(rt[t]*math.sin(H[t]))
        t=t+1

fig1=plt.figure(1)
plt.polar(H,rt)
plt.polar(0,0)
plt.show()
print(np.sort(x))

    
fig2=plt.figure(2)
plt.scatter(x, y)
plt.scatter(0,0)
plt.title('Halleys Comet Orbit around the Sun')
plt.xlabel('Distance in AU')
plt.ylabel('Distance in AU')
#plt.xlim(right=3, left=-3)
#plt.ylim(bottom=-3, top=3)


'''
#ANIMATING
'''

fig, ax = plt.subplots()
ln, = plt.plot([], [], 'go') 

def init():
    ax.set_xlim(-40, 5)
    ax.set_ylim(-5, 5)
    return ln,

def update(frame):
    ln.set_data(x[:frame], y[:frame])
    return ln,

ani = FuncAnimation(fig, update, frames=np.arange(0, 3963, 30),
                    init_func=init, blit=True)

plt.title('Halleys Comet Orbit around the Sun')
plt.xlabel('Distance in AU')
plt.ylabel('Distance in AU')
plt.scatter(x,y, 1)
plt.scatter(0,0)
plt.show()



  


