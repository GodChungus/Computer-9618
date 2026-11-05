def undirected_matrix(V, E):
    matrix = [[0]*V for _ in range(V)]
    for edge in E:
        u, v = edge
        matrix[u][v] = 1
        matrix[v][u] = 1
    return matrix

def directed_matrix(V, E):
    matrix = [[0]*V for _ in range(V)]
    for edge in E:
        u, v = edge
        matrix[u][v] = 1
    return matrix


V = 6
E = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5]]
for row in undirected_matrix(V, E):
    print(row)
print()
