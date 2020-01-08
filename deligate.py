def f(x):
    rez = x * 2
    print("")
    return rez


def start():
    n = int(input())
    l = {}
    i = int(0)
    ar = []
    while i < n:
        k = input()
        ar.append(k)
        i += 1
    for nb in ar:
        if l.get(nb) == None:
            l[nb] = f(int(nb))
        print(l[nb])
if __name__ == "__main__":
    start()
    pass


