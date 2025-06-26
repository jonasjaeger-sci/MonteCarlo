# -*- coding: utf-8 -*-
"""
"Create a random Walk algorithm with Monte Carlo simulation"
"""

import random as rd
import matplotlib.pyplot as plt

"""
1. Define a function to generate a random walk on a 2D-grid with n as input 
for the number of steps to take. The steps are discrete and asigned randomly 
from a uniform distribution, meaning a step in any direction is equally likely.
"""

#x = [6,4,2,10,26,9]; dx = -1; 
#x.append(x[-1]+dx)
#print(x[-1])

#dx,dy = rd.choice(([1,0],[0,-1],[-1,0],[0,1]))
#print(dx);print(dy)

#'''

def rd_walk(n):
    x,y = [0],[0] # initiate origin cartesian coordinates in lists
    
    for i in range(n):
        #dx,dy = rd.choice(([1,0],[0,-1],[-1,0],[0,1])) # random discrete step selection
        dx,dy = rd.uniform(-1,1),rd.uniform(-1,1) # random "continuous" step selection
        #x += dx
        #y += dy
        
        # add step in x- and y-direction to last coordinate and update list
        x.append(x[-1] + dx) ; y.append(y[-1] + dy)
        
    return(x,y)

#'''
n_test = 10
x_test,y_test = rd_walk(n_test)
plt.scatter(x_test,y_test)
plt.grid("true")
plt.ylim([-n_test,n_test])
plt.xlim([-n_test,n_test])
plt.show()

#'''

