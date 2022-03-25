import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import make_blobs
import random
import numpy as np
#1
def generate_baby(amount):
    data = []
    
    for x in range(amount):
        baby_age = random.randint(0,24)
        baby_height = random.randint(40,60)
        baby_weight = random.randint(2,5)
        data.append((baby_age,baby_height,baby_weight))
    
    print(data)
    return np.asarray(data)    
        
#2
def plot_baby(baby):
    data_3d, _ = make_blobs(n_samples=2500, centers=baby, cluster_std=0.37)
    x,y,z = baby[:,0], baby[:,1], baby[:2]
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, linewidth=0.2)

    plt.show()


plot_baby(generate_baby(15))    