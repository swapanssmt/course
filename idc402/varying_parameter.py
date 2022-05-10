import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

rho1 = [-5,-1,0,1,5,13,15,20,24.734,50,170,300,500]
#sigma1=[-1,0,2,5,10,15,50,100]
#sigma1=[300]
for rho in rho1:
    #rho=28.0
    beta = 8.0 / 3.0
    sigma=10.0
    def f(state, t):
        x, y, z = state  # Unpack the state vector
        return sigma * (y - x), x * (rho - z) - y, x * y - beta * z  # Derivatives
    
    state0 = [0.0, 1.0, 1.05]
    t = np.arange(0.0, 50.0, 0.01)
    
    states = odeint(f, state0, t)
    
    fig = plt.figure()
    ax = fig.gca(projection="3d")
    ax.plot(states[:, 0], states[:, 1], states[:, 2])
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor $r$={}".format(rho))
    plt.draw()
    plt.show()
    x=states[:, 0]
    y=states[:, 1]
    z=states[:, 2]
    time=t
    fig, (ax1,ax2,ax3) = plt.subplots(1,3, figsize = (15, 5))
    ax1.plot(x, y)
    ax1.set_title("X & Y")
    ax1.set_xlabel("X Axis")
    ax1.set_ylabel("Y Axis")
    ax2.plot(x, z)
    ax2.set_title("X & Z")
    ax2.set_xlabel("X Axis")
    ax2.set_ylabel("Z Axis")
    ax3.plot(y, z)
    ax3.set_title("Y & Z")
    ax3.set_xlabel("Y Axis")
    ax3.set_ylabel("Z Axis")
    plt.show()
    fig, (ax1,ax2,ax3) = plt.subplots(1,3, figsize = (15, 5))
    ax1.plot(time, x)
    ax1.set_title("Time series for X(t)")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("X(t)")
    ax2.plot(time, y)
    ax2.set_title("Time series for Y(t)")
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Y(t)")
    ax3.plot(time, z)
    ax3.set_title("Time series for Z(t)")
    ax3.set_xlabel("Time")
    ax3.set_ylabel("Z(t)")
    plt.show()