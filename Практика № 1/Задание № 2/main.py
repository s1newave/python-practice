a = [10, -7, 8, -100, -50, 32, 87, 117, -210]

print(min(a, key=abs))
print(max(a, key=abs))
print(sorted(a, key=abs))
