import numpy as np
import matplotlib.pyplot as plt

sigma = 10.0
beta = 8.0/3.0
h = 0.01 #Step size for RK4
def derivative(r,t,rho):
    x = r[0]
    y = r[1]
    z = r[2]
    return np.array([sigma * (y - x), x * (rho - z) - y, (x * y) - (beta * z)])


dr = 0.1  # parameter step size
rho = np.arange(-2, 200, dr)  # parameter range

# Save the plot points coordinates and plot the with a single call to plt.plot
# instead of plotting them one at a time, as it's much more efficient
r1_maxes = []
z_maxes = []
r1_mins = []
z_mins = []
r2_maxes = []
x_maxes = []
r2_mins = []
x_mins = []
r3_maxes = []
y_maxes = []
r3_mins = []
y_mins = []
r = np.array([0.0, 1.0, 1.05]) #Initial conditions array

for R in rho:
    t = 0 #Starting time
    tf = 40 #Ending time
    time = np.array([]) #Empty time array to fill for the x-axis
    x = np.array([]) #Empty array for x values
    y = np.array([]) #Empty array for y values
    z = np.array([]) #Empty array for z values

    # Print something to show everything is running
    #print(f"{R=:.2f}")
    while (t <= tf ):
        #Appending values to graph
        time = np.append(time, t)
        z = np.append(z, r[2])
        y = np.append(y, r[1])
        x = np.append(x, r[0])
        #RK4 Step method
        k1 = h*derivative(r,t,R)
        k2 = h*derivative(r+k1/2,t+h/2,R)
        k3 = h*derivative(r+k2/2,t+h/2,R)
        k4 = h*derivative(r+k3,t+h,R)
        r += (k1+2*k2+2*k3+k4)/6
        #Updating time value with step size
        t = t + h
    for i in range(1, len(z) - 1):
        # save the local maxima
        if z[i - 1] < z[i] and z[i] > z[i + 1]:
            r1_maxes.append(R)
            z_maxes.append(z[i])
        # save the local minima
        elif z[i - 1] > z[i] and z[i] < z[i + 1]:
            r1_mins.append(R)
            z_mins.append(z[i])
        if x[i - 1] < x[i] and x[i] > x[i + 1]:
            r2_maxes.append(R)
            x_maxes.append(x[i])
        # save the local minima
        elif x[i - 1] > x[i] and x[i] < x[i + 1]:
            r2_mins.append(R)
            x_mins.append(x[i])
        if y[i - 1] < y[i] and y[i] > y[i + 1]:
            r3_maxes.append(R)
            y_maxes.append(y[i])
        # save the local minima
        elif y[i - 1] > y[i] and y[i] < y[i + 1]:
            r3_mins.append(R)
            y_mins.append(y[i])

    # "use final values from one run as initial conditions for the next to stay near the attractor"
    r= np.array([x[i], y[i], z[i]])


plt.scatter(r1_maxes, z_maxes, color="black", s=0.5, alpha=0.2)
plt.scatter(r1_mins, z_mins, color="red", s=0.5, alpha=0.2)
plt.xlabel("r")
plt.ylabel("z")
plt.title("Bifurcation Diagram for the Lorenz attractor")
#plt.xlim(0, 200)
#plt.ylim(0, 400)
plt.show()
plt.scatter(r2_maxes, x_maxes, color="black", s=0.5, alpha=0.2)
plt.scatter(r2_mins, x_mins, color="red", s=0.5, alpha=0.2)
plt.xlabel("r")
plt.ylabel("x")
plt.title("Bifurcation Diagram for the Lorenz attractor")
#plt.xlim(0, 200)
#plt.ylim(0, 400)
plt.show()
plt.scatter(r3_maxes, y_maxes, color="black", s=0.5, alpha=0.2)
plt.scatter(r3_mins, y_mins, color="red", s=0.5, alpha=0.2)
plt.xlabel("r")
plt.ylabel("y")
plt.title("Bifurcation Diagram for the Lorenz attractor")
#plt.xlim(0, 200)
#plt.ylim(0, 400)
plt.show()
