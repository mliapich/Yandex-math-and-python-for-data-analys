from math import *
import numpy
from scipy.optimize import minimize, differential_evolution
from matplotlib import pyplot as plt

def f(x):
    return sin(x / 5.0) * exp(x / 10.0) + 5 * exp(-x / 2.0)

def h(x):
    return(int(f(x)))

def main():
    x = numpy.linspace(1,30,1000)
    y = [f(i) for i in x]
    z = [h(i) for i in x]
    plt.plot(x,y)
    plt.plot(x,z)
    plt.show()
    print 'BFGS\n',minimize(h,[30],method='BFGS')
    print 'DE\n',differential_evolution(h,[(1,30)])

if __name__ == '__main__':
    main()
