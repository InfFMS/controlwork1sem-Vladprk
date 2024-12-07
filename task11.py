for x in range(174457, 174506):
    k = 0
    mas = []
    for i in range(2, x//2 + 1):
        if x % i == 0:
            k += 1
            mas.append(i)
            if k > 2:
                break
    if k == 2:
        print(mas)
