n = int(input("Введите количество элементов: "))
print("Введите элементы:")
a = [int(input()) for _ in range(n)]

print(a)

a[0], a[-1] = a[-1], a[0]

print(a)
