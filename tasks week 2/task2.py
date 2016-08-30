from math import *
from scipy.linalg import solve
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial


def f(x):
    return sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)

def aproximate(points):

    pass

def main():
    A = np.array([[1, 1, 1, 1], [1, 4, 4**2, 4**3],[1, 10, 10**2,
                                                   10**3], [1, 15, 15**2, 15**3]], dtype='float')
    b = np.array([f(1.0), f(4.0), f(10.0), f(15.0)], dtype='float')
    fig, ax = plt.subplots()
    x = np.linspace(0, 15, 100)
    y = [f(i) for i in x]
    ax.plot(x, y)
    coef = solve(A, b)
    pol = Polynomial(coef)
    print coef
    file = open('result2.txt','w')
    file.write(str(coef))
    y = [pol(i) for i in x]
    ax.plot(x, y)
    plt.show()

if __name__ == '__main__':
    main()
