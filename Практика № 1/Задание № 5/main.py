from random import randint


def printMatrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print("{:^5}".format(mat[i][j]), end="")
        print()


N, M = 3, 5

mat = []
for i in range(N):
    mat.append([])
    for j in range(M):
        mat[i].append(randint(20, 80))

printMatrix(mat)
