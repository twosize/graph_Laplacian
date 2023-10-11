import random


N = 100  
w = 10  
total_nodes = N 


A = [[0 for _ in range(total_nodes)] for _ in range(total_nodes)]


for i in range(1, N ):
    A[i][0] = 1
    A[0][i] = 1


edges_added = 0
while edges_added < w:
    i, j = random.randint(1, N), random.randint(1, N)
    

    if i != j and A[i][j] == 0:
        A[i][j] = 1
        A[j][i] = 1
        edges_added += 1


D = [[0 for _ in range(total_nodes)] for _ in range(total_nodes)]
for i in range(total_nodes):
    D[i][i] = sum(A[i])

# Compute Laplacian Matrix L (L = D - A)
L = [[0 for _ in range(total_nodes)] for _ in range(total_nodes)]

for i in range(total_nodes):
    for j in range(total_nodes):
        L[i][j] = D[i][j] - A[i][j]

#Print matrices (This part is optional, useful for verification)
print("Adjacency Matrix A:")
for row in A:
    print(row)

print("\nDegree Matrix D:")
for row in D:
    print(row)

print("\nLaplacian Matrix L:")
for row in L:
    print(row)