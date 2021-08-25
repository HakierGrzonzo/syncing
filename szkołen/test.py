import matplotlib.pyplot as plt
from multiprocessing import Pool
import numpy as np


a0 = 1 - (np.pi) / 2

def an(n):
    return (1 - ((-1)**n)) / (n*n*np.pi)


def bn(n):
    return -(1 - (1 + np.pi) * ((-1)**n)) /  (n * np.pi)

def Y(x):
    n = range(1, 1000)
    return (a0 / 2 + sum([an(n) * np.cos(n * x) + bn(n) * np.sin(n * x) for n in n]))
if __name__ == "__main__":
    X = np.linspace(-np.pi + 1 , np.pi - 1, 1000)
    pool = Pool(12)
    y = pool.map(Y, X, 100)

    plt.plot(X, y)
    plt.xlim(-np.pi, np.pi)
    plt.grid()
    plt.show()
