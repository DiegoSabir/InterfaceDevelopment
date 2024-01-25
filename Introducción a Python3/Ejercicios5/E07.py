import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

colors = [ 'gray', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds']

def changeColorMap():
    plt.figure()
    color = random.choice(colors)
    plt.pcolormesh(np.random.rand(60, 60), cmap=color)
    plt.title("Color Map: " + color)
    plt.show(block= False)
    plt.pause(5)

for i in range(6):  
    changeColorMap()
