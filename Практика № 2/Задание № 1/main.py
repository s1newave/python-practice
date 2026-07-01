def is_palindrome(s):
    return s == s[::-1]


s = input("Введите строку: ")
print(
    "Строка",
    "является" if is_palindrome(s) else "не является",
    "палиндромом."
)
