letters = ["a", "b", "c"]
nums = [1, 2, 3]

dict_ = dict(zip(letters, nums))

key = input("Введите ключ: ")

if key in dict_:
    print(f"Значение: {dict_.get(key)}")
else:
    value = input("Введите значение: ")
    dict_[key] = value

file = open("ex2-1.txt", "w")
file.write(dict_.__str__())
file.close()
