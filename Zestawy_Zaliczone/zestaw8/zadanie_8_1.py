def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if a == 0 and b == 0 and c == 0:
        print("x dowolne, y dowolne")
    elif a == 0 and b == 0:
        print("rownanie sprzeczne")
    elif a == 0:
        print("x dowolne, y =", -c / b)
    elif b == 0:
        print("x = ", -c / a, " y dowolne")
    else:
        print("y = (", -a, " * x - ", c, ") /", b)


#      ax+by+c
solve1(0, 0, 0)  # x dowolne, y dowolne
solve1(0, 0, 1)  # rownanie sprzeczne
solve1(0, 1, 1)  # x dowolne, y = -1.0
solve1(1, 1, 1)  # y = ( -1  * x -  1 ) / 1
