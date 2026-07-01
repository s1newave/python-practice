def calc(expr):
    a, op, b = expr.split()

    if op == "*":
        return int(a) * int(b)
    elif op == "**":
        return int(a) ** int(b)

print(f"{calc("3 * 7") = }")
print(f"{calc("4 ** 2") = }")
