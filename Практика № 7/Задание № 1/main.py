def disintegration(list_, val):
    if val not in list_:
        raise ValueError("value not found in the list")

    i = 0
    while i < len(list_):
        if list_[i] == val:
            del list_[i]
        else:
            i += 1

try:
    a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    print(a)

    disintegration(a, 4)
    print(a)

    disintegration(a, 5)
    print(a)
except ValueError:
    print("Значения нет в списке.")
