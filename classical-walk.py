import cirq
import random
import numpy as np
from matplotlib import pyplot as plt
import scipy
import scipy.special


N = 50    
pr = 0.5  
i = 0     

def random_walk(pr, N, i):

    position = i

    for j in range(N):

        coin_flip = list(np.random.choice(2, 1, p=[1-pr, pr])) 
        position += 2*coin_flip[0]-1 
    return position

def dist(runs, N):

    positions = range(-1*N, N+1)
    instances = [0 for i in range(-1*N, N+1)]

    for k in range(runs):

        result = random_walk(pr, N, i)
        instances[positions.index(result)] += 1

    plt.bar(positions, [n/runs for n in instances])
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()
    plt.show()

run_range = [50, 1000, 10000]
for run in run_range:
    dist(run, N)


