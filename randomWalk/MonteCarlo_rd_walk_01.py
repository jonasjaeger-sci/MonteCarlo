# -*- coding: utf-8 -*-
"Create a random Walk algorithm with Monte Carlo simulation"

import random as rd
import matplotlib.pyplot as plt

'''
1. Define a random walk function that lets one person walk in a 2D-grid. For starters
all directions (backtracking) are allowed
'''

def rd_walk(n): # input n as number of steps to take

    "initiate origin cartesian coordinates"
    x,y = 0,0
    
    for i in range(n):
        
        direction = rd.choice(["N","E","S","W"])
        
        if direction == "N":
            y += 1
        elif direction == "E":
            x += 1
        elif direction == "S":
            y += -1
        else:
            x += -1
            
    return(x,y) 



'''
2. Start a Monte Carlos simulation by initiating multiple random walks with 
different numbers of steps. By exploiting the law of large numbers we can infer 
the probabilty of how often we end up on the x or y axis, so north, 
east, south or west from the origin.
'''

n_rd_walks = 1000 # number of random walks performed per step length
max_steps = 100 # maximum step size of the random walk
n_sim = n_rd_walks*max_steps # number of performed simulations 
p_list = [] # initaite list of probabilities for plotting

for k in range(1,max_steps+1): 
    
    n_ortho_walks = 0 # initiate variable for counting last locations on x or y axis
    #p_list = [] # initaite list of probabilities for plotting
    
    for j in range(n_rd_walks):
        
        final_x,final_y = rd_walk(k)
        
        if final_x == 0 or final_y == 0:
                n_ortho_walks += 1
    
    p = n_ortho_walks/n_rd_walks
    p_list.append(p)
    
    print("probability of ending up N,E,S or W with ",str(k)," steps =",str(p))
 
n_list = list(range(1,max_steps+1))
#print(str(n_list))   
plt.plot(n_list,p_list)
plt.xlabel("Number of steps")
plt.ylabel("Probability of final location on x- or y-axis")
plt.ylim((0,1))
plt.show()
    

    
    
    
            
    

    