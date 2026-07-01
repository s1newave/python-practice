m = [3.46871, 5.31916, 4.013449, 6.57686, 15.012678]

rounded = map(round, m, range(5, 5 - len(m), -1))

print(list(filter(lambda x: x > 5, rounded)))
