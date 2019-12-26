import numpy as np


N = 3
M = 4
A = np.array([[2, 7, 9, 3],
             [14, 4, 1, 9],
             [1, 5, 2, 5]])

B = np.zeros((N, M))
print(A)
i = 0
j = 0
# Подсчет первого столбца
B[0, 0] = A[0, 0]
for i in range(1, N):
    A[i, 0] = A[i - 1, 0] + A[i, 0]

# Подсчет первого строки
for j in range(1, M):
    A[0, j] = A[0, j - 1] + A[0, j]


steps = [(N - 1, M - 1)]

i = N - 1
j = M - 1
for _ in range(1 + j):
    top = A[i - 1, j]
    left = A[i, j - 1]

    if top < left:
        i -= 1
    else:
        j -= 1
    steps.append((i, j))


for i in range(1, N):
    for j in range(1, M):
        top = A[i - 1, j]
        left = A[i, j - 1]

        if top < left:
            A[i, j] += top
        else:
            A[i, j] += left
print(A)
print(steps)

# Подсчет первого столбца
# for _ in range(N):
#     for _ in range(M):
#         left = A[i, j - 1]
#         top = A[i - 1, j]
#         if left < top:
#             j += 1
#         else:
#             i += 1