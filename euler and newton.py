# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 18:04:54 2020

@author: kpurc
"""

### comparing different methods
### euler, neuton, runka kutta
### some precess and some dont, some are bigger, see results 


import matplotlib.pyplot as plt
import numpy as np
import scipy
#from scipy import stats
#from scipy import signal
import math
from matplotlib.animation import FuncAnimation

stand = [i for i in range(3963)]

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
#stand = [i for i in range(3963)]
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
xI=[]
yI=[]
while t < 3963:
        xI.append(rt[t]*math.cos(H[t]))
        yI.append(rt[t]*math.sin(H[t]))
        t=t+1
        
        
import pylab
import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib.animation import FuncAnimation

G=4*math.pi**2	# define G.

## Set initial position and speed of satellite.
M  = 1.0	# mass of the central mass

# give info to help user decide on initial conditions 
#Ro = 1.0	# Radius of the orbit 
#v =math.sqrt(G*M/Ro)	# v assuming circular orbit
#print("For circular orbit of r = %g, and v = %g." % (Ro,v)) 

# propt user for initial conditions times
x0 = 0.587 #AU 'Initial radius'
a = 17.78788
vy0 = math.sqrt((G*M)*((2/x0)-(1/a))) #AU/s #'Initial tangential velocity'
y0 = 0.
vx0 = 0.

t0 = 0.
tf = 1000 #input("Enter final time: ")
tau = .01 #input("Enter time step: ")

## Create arrays needed to store the results for plotting
x_plt = np.array([x0])
y_plt = np.array([y0])
vx_plt = np.array([vx0])
vy_plt = np.array([vy0])
t_plt = np.array([t0])

## Execute Euler method
# set starting points for iteration to initial conditions
x_old = x0	
y_old = y0
vx = vx0
vy = vy0
t = t0	# set starting time to 0

while (t < tf):
	x = x_old + vx*tau		# implement Euler step
	y = y_old + vy*tau
	r = math.sqrt(x**2 + y**2)
	vx = vx - tau*(G*M*x)/r**3
	vy = vy - tau*(G*M*y)/r**3
	
	x_plt = np.append(x_plt,x) # Append new points to the arrays
	y_plt = np.append(y_plt,y)
	vx_plt = np.append(vx_plt,vx)
	vy_plt = np.append(vy_plt,vy)
	t_plt = np.append(t_plt,t)
	
	x_old = x				# Update x_old and y_old for next Euler step
	y_old = y
	t = t + tau				# Increment time

## Plot the results
#plt.figure(1)
#plt.clf()

# Plot the orbit
#plt.subplot(2,1,1)	# subplot() lets you put multiple plots on a single page
#plt.title(r'Euler Method with $x$ = %g, $v_y$ = %g, and $\tau$ = %g' % (x0,vy0,tau))
#plt.plot(x_plt,y_plt)

"""
RK
"""
import math
from scipy.integrate import odeint

def twoBody(y, t, mu):
    r = math.sqrt(y[0]**2 + y[1]**2)

    ydot = np.empty((4,))

    ydot[0] = y[2]
    ydot[1] = y[3]
    ydot[2] = (-mu/(r**3))*y[0]
    ydot[3] = (-mu/(r**3))*y[1]
    return ydot

G=4*math.pi**2	# define G.
M  = 1.0	# mass of the central mass this is the sun
a = 17.78788

x0= 0.587 #AU 'Initial radius'
y0=0
vx0=0
vy0 = math.sqrt((G*M)*((2/x0)-(1/a)))

Y0 = np.array([x0, y0, vx0, vy0])

mu = G*M

solution = odeint(twoBody, Y0, np.linspace(0, 3963, 3963), args=(mu, ))

myX=solution[:,0]
myY=solution[:,1]

#rR=(myX**2-myY**2)**.5
#errorR=rt-np.sort(rR)



rE = (x_plt**2 + y_plt**2)**.5
#errorE = rt-rE
'''
plt.scatter(stand, errorE, label="Iterative - Euler")
plt.xlabel('t value')
plt.ylabel('Error')
plt.legend(loc='upper right', ncol=3, fancybox=True)
plt.title("Error Over time for Iterative v. Euler")
'''
plt.scatter(x_plt,y_plt, label='Euler')
plt.scatter(xI,yI, label='Iterative')
plt.scatter(myX,myY, label="Runga Kutta")
plt.xlabel('X distance')
plt.ylabel('Y distance')
plt.legend(loc='upper right', ncol=3, fancybox=True)
plt.title("Iterative v. Euler v. Runga Plot")

plt.show

