def sum_1(n):
    res = 0
    for i in range(1, n+1):
        res += 1 / i ** 2
    return res


def sum_2(n, m):
    res = 0
    for i in range(1, m+1):
        res += i ** n
    return res


def select_operation(x):
    if x == 1:
        return sum_1
    elif x == 2:
        return sum_2


print(select_operation(1) (3))
print(select_operation(2) (2, 3))
