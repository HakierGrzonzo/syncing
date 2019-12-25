from sys import stdout
from multiprocessing import Pool
comp = 0

def Pow(k):
    comp = 0
    a = 2
    z = a
    y = 1
    m = k
    while m != 0:
        comp = comp +1
        if m % 2 == 1:
            y = y*z
        m = int(m/2)
        z = z*z
    return comp

def handleStuff(n):
    p = Pool(10)
    res = p.map(Pow, range(2**n))
    return max(res)

if __name__ == "__main__":
    for n in range(2,129):
        toMake = 2**n -1
        print(str(n) + "\t" +str(handleStuff(n)))
        comp = 0
