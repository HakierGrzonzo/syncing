import itertools
def f1(a, b, c):
    a = 10
    b += 5
    c += a
    return a, b, c

def f2(a, b, c):
    b += c
    a += b
    return a, b, c

def f3(a, b, c):
    c = b + 10
    a *= 2
    b += a
    return a, b, c

threadies = [f1, f2, f3]
for possibility in itertools.permutations(threadies):
    print(list([x.__qualname__ for x in possibility]))
    a, b, c = 0, 0, 3
    for f in possibility:
        a, b, c = f(a, b, c)
        print(a, b, c)
    print(a + b + c)
