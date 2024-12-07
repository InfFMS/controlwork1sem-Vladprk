a = []
for i in range(100):
    for j in range(100):
        b = True
        for x in range(100):
            if not((not(i <= x <= j)) <= (((17 <= x <= 46) and (22 <= x <= 57)) <= (i <= x <= j))):
                b = False
                break
        if b == True:
            a += [j-i]
print(min(a))
