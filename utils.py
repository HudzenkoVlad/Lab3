def Fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * Fact(n - 1)


def FiveDegree(x):
    if x == 1:
        return "Число є степенем п'ятірки"
    if x != int(x):
        return "Число не є степенем п'ятірки"
    else:
        return FiveDegree(x / 5)
