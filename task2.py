import random 
import numpy as np 
import matplotlib.pyplot as plt
import time
import math
from random import choices
from random import choices

p1 = float(input("Enter the right probability of person 1: "))
p2 = float(input("Enter the right probability of person 2: "))
s1 = int(input("Enter the starting position of person 1: "))
s2 = int(input("Enter the starting position of person 2: "))
prob1 = [p1, round(float(1-p1),1)]
prob2 = [p2, round(float(1-p2),1)]
x = abs(s1-s2)
path1 = [s1]
path2 = [s2]
check = False
pos1 = 0
pos2 = 0
#start_time = time.time()   
time = 0    #Assumption = This time is equivalent to real time so if time = 5 then it is equal to 5 seconds.

while (check == False):
    choice1 = choices([1,-1], prob1)  #Selects 1 & -1 with the corresponding probabilties specified in prob1 list. 
    choice2 = choices([1,-1], prob2)  #Selects 1 & -1 with the corresponding probabilties specified in prob2 list.
    #print("Choice: ", choice)
    pos1 = path1[-1] + choice1[0]
    pos2 = path2[-1] + choice2[0]
    path1.append(pos1)
    path2.append(pos2)
    time+=1
    if path1[-1] == path2[-1]:
        check = True
    #if (time.time()-start_time) > 300:
        #raise Exception("Sorry, 5 minutes have passed and they don't meet.")
        #break
    #end_time = time.time()
    if time == 300:
        break
#time = math.ceil(end_time - start_time)
#print(time)
time = list(range(0, time+1))
print("Time taken = ", time)
print("Starting position of p1 = ", s1)
print("Starting position of p2 = ", s2)
print("Path1 = ", path1)
print("Path2= ", path2)
print("Time to meet in seconds = ", time[-1])
plt.plot(time, path1, 'r--', time, path2, 'r')
plt.xlabel("Time(s)")
plt.ylabel("Distance from starting position")
plt.show()
