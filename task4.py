import random 
import numpy as np 
import matplotlib.pyplot as plt
from random import choices
from scipy.stats import uniform

def path_finder(steps, prob, path):
    pos = 0
    for i in range(steps):
        choice = uniform.rvs(size=1, loc = 0, scale=1)  #Selects 1 & -1 with the corresponding probabilties specified in prob list. 
        choice = choice[0]
        pos = path[-1] + choice
        path.append(pos)
    return path

p = float(input("Enter the probability to move right (p): "))
steps = int(input("Enter the number of steps taken: "))
start_pos = int(input("Enter the starting position: "))
prob = [p, round(float(1.0-p), 1)] #p = prob to move right and 1-p = prob to move left
print(prob)
path = [start_pos]
path2 = path_finder(steps, prob, path)
print("Starting position = ", start_pos)
print("Distance from starting position = ", round(float(path[-1]),2))
plt.plot(path)
plt.xlabel("Steps")
plt.ylabel("Distance from starting position")
plt.show()
