def Fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * Fact(n - 1)
<<<<<<< HEAD


def FiveDegree(x):
    if x == 1:
        return "Число є степенем п'ятірки"
    if x != int(x):
        return "Число не є степенем п'ятірки"
    else:
        return FiveDegree(x / 5)
=======
from math import ceil
def prost(n):
    i = 2
    while i <= ceil(n ** (1 / 2)):
        if n % i == 0:
            return "не просте"
        i = i + 1
    return "просте"
>>>>>>> 84849a36a4c7a8dc3273cbd5d038c2a719eb8b43
