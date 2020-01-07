from sys import stdout
from multiprocessing import Pool, cpu_count
comp = 0

def Pow(m):
    print('comp\tz\ty\tm\tifif')
    comp = 0
    z = 3
    y = 1
    ifif =False
    print(comp, z, y, m, 'None', sep='\t')
    while m != 0:
        comp = comp +1
        if m % 2 == 1:
            ifif = True
            y = y*z
        m = int(m/2)
        z = z*z
        print(comp, z, y, m, ifif, sep='\t')
        ifif = False
    return comp

def avrage(lis):
    x = 0
    for z in lis:
        x += z
    x / len(lis)
    return x

def handleStuff(n):
    p = Pool(cpu_count())
    res = avrage(p.map(Pow, range(2**n - 1)))
    return res / len(range(2**n - 1))

if __name__ == "__main__":
    n = 1
    while True:
        Pow(n)
        n += 1
        input()
