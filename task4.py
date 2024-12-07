for x in range(2030):
    arifm_v = 3**100 - x
    count = 0
    while arifm_v != 0:
        if arifm_v % 3 == 0:
            count += 1
        arifm_v = arifm_v//3
    if count == 2:
        print(x)
        break