import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def surface(r):
    """This function calculates the surface of a circle"""
    area = np.pi*r**2
    return area

def circumference(r):
    """This function calculates the circumference"""
    return 2*np.pi*r

def f(x):
    return np.sin(x)

def plot(a,b,c):
    x= np.arange(a,b,c)
    plt.plot(x, f(x))
    plt.show()
    print(np.size(x))