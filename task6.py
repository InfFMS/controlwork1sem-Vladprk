def F(n):
    if n == 1:
        return 1
    elif n > 1:
        return F(n-1) + 2**(n-1)
    else:
        return "error"


print(F(12))
