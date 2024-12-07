count = 0
i = 300000000
while count < 5:
    new_i = i // 2
    k = 0
    for j in range(2, new_i + 1):
        if i % j == 0:
            if k == 5:
                print(i // j)
                count += 1
                break
    i += 1
