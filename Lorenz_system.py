import numpy as np
import matplotlib.pyplot as plt
import warnings
from IPython.display import display, HTML
warnings.filterwarnings("ignore")
from scipy.integrate import odeint  #FORTRAN Back

def Lorenz(inital_conditions,t,sigma,r,b):
    x,y,z = inital_conditions[0],inital_conditions[1],inital_conditions[2]
    x_dot = sigma*(y-x)
    y_dot = -x*z + r*x - y
    z_dot = x*y - b*z
    return np.array([x_dot,y_dot,z_dot])

def Integral(func,inital_conditions,t,sigma,r,b):
    solution = odeint(func,inital_conditions,t,args = (sigma,r,b)).T
    return solution

#inital_condition
inital_conditions = [0.5,0.51,0.5]   # x_0, y_0, z_0
sigma,r,b = 10, 28, 8/3

t = np.linspace(0,100,500)
sol = Integral(Lorenz,inital_conditions,t,sigma,r,b)

fig = plt.figure(figsize=(18, 15))
for s,axis,c,name in zip(sol,range(1,4),['lightseagreen','crimson','slateblue'],['X','Y','Z']):
    ax =  fig.add_subplot(3, 1, axis )
    plt.plot(t,s,color=c)
    plt.xlabel('time')
    plt.title(name)
plt.show()

sol1 = Integral(Lorenz,inital_conditions,t,sigma,5,b)
sol2 = Integral(Lorenz,inital_conditions,t,sigma,10,b)
sol3 = Integral(Lorenz,inital_conditions,t,sigma,25,b)

fig = plt.figure(figsize=(18, 7))
for s,c,name in zip([sol1[2],sol2[2],sol3[2]],['lightseagreen','crimson','slateblue'],['r=5','r=10','r=25']):
    plt.plot(t,s,color=c,label=name)
    plt.xlabel('time')
    plt.title('Lorenz model z versus time ')
plt.legend(loc='best')
plt.show()

#inital_condition
inital_conditions = [5,5,5]   # x_0, y_0, z_0
sigma,r,b = 10, 28, 8/3

t = np.linspace(0,100,20000)
sol = Integral(Lorenz,inital_conditions,t,sigma,r,b)

fig = plt.figure(figsize=(7,7))

ax = fig.add_subplot(111, projection='3d')
ax.plot(sol[0], sol[1], sol[2],lw=0.5,color='brown')
ax.set_xlabel('X') ;ax.set_ylabel('Y'); ax.set_zlabel('Z')
plt.show()

#inital_condition
inital_conditions = [5,5,5]   # x_0, y_0, z_0
sigma,r,b = 10, 13, 8/3

t = np.linspace(0,100,20000)
sol = Integral(Lorenz,inital_conditions,t,sigma,r,b)

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(sol[0], sol[1], sol[2],lw=1,color='darkblue')
ax.set_xlabel('X') ;ax.set_ylabel('Y'); ax.set_zlabel('Z')
plt.show()
