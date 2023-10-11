
"""d) Use your favorite programming language and write a code to compute the graph Laplacian based
on your answer of part b. [Hint: yes, this is about matrix subtraction. Do not use any software
package that will directly generate the Laplacian for you.
"""
n = 7

A = [[0 for _ in range(n)] for _ in range(n)]


for i in range(1, n):
    A[i][0] = 1
    A[0][i] = 1

print("Adjacency Matrix A:")
for row in A:
    print(row)

D = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    D[i][i] = sum(A[i])

print("\nDegree Matrix D:")
for row in D:
    print(row)


L = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        L[i][j] = D[i][j] - A[i][j]

print("\nLaplacian Matrix L:")
for row in L:
    print(row)