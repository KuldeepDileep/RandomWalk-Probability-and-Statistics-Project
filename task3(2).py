import random
from random import choice
import math
import numpy as np 
import matplotlib.pyplot as plt

r = 100
dis = [0, 0.5, 1]
pathx = [0]
pathy = [0]
steps = 10000
circle_theta = np.linspace(0, 2*np.pi)
x1 = r*np.cos(circle_theta)
y1 = r*np.sin(circle_theta)
for i in range(steps):
    check = False
    #theta = random.choices([((0*math.pi)/180),((60*math.pi)/180),((120*math.pi)/180),((180*math.pi)/180),((240*math.pi)/180),((300*math.pi)/180),((360*math.pi)/180)])
    theta = random.randint(0,361)
    #print(theta, "\n")
    theta = (theta*math.pi)/180
    #print(theta, "\n")
    u1 = random.choice(dis)
    u2 = random.choice(dis)
    h = pathx[-1]
    k = pathy[-1]
    r2 = ((u1+h)**2 + (u2+k)**2)**(1/2)
    x2 = r2*math.cos(theta)
    y2 = r2*math.sin(theta)
    while (check == False):
        if (x2**2 + y2**2) > r**2:
            x3 = r*math.cos(theta)
            y3 = r*math.sin(theta)
            pathx.append(x3)
            pathy.append(y3)
            if ((int(x2) > 0 & int(y2) > 0) | (int(x2) > 0 & int(y2) < 0)): #When point is outside but in first and fourth quadrant 
                x2 = x3 - (x2 - x3)
                y2 = y3
            else:
                x2 = x3 + (x3 - x2)
                y2 = y3
            pathx.append(x2)
            pathy.append(y2)
        else:
            pathx.append(x2)
            pathy.append(y2)
            check = True
fig, ax = plt.subplots(1)
ax.plot(x1, y1)
circle = plt.Circle((0, 0), 1)
plt.plot(pathx,pathy)
plt.legend(["Circle", "Plot"])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
