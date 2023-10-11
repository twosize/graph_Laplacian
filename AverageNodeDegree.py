import random

total_nodes = 100 
additional_edges = 10 


adj_matrix = [[0] * total_nodes for _ in range(total_nodes)]

for i in range(1, total_nodes):
    adj_matrix[i][0] = 1
    adj_matrix[0][i] = 1

edges_added = 0
while edges_added < additional_edges:
    node1, node2 = random.randint(1, total_nodes-1), random.randint(1, total_nodes-1)
    

    if node1 != node2 and adj_matrix[node1][node2] == 0:
        adj_matrix[node1][node2] = 1
        adj_matrix[node2][node1] = 1
        edges_added += 1


node_degrees = [sum(row) for row in adj_matrix]


average_degree = sum(node_degrees) / total_nodes

print(f"Node Degrees: {node_degrees}")
print(f"Average Node Degree: {average_degree}")
