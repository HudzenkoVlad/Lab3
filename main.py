def Fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * Fact(n - 1)


a = int(input())
print(Fact(a))