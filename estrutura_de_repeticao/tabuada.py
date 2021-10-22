def tabuada(targert: int, rangeNumber: int) -> str:
    for i in range(rangeNumber + 1):
        print("{0} * {1} = {2}".format(targert, i, targert * i))


tabuada(5, 10)
