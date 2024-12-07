count = 0
for x in range(1, 2097153):
    if 2097152 % x == 0:
        count += 1
print(count)
