def find_circuit(vertices, edges):

    path = []
    is_first = True

    for vertex in vertices:
        temp = vertex
        visited_edges = []

        if is_first:
            path.append(temp)
            is_first = False

        for edge in edges:
            if edge in visited_edges:
                continue

            visited_edges.append(edge)

            if edge[0] == temp:
                path.append(edge[1])

                if edge[1] == vertex:
                    path.append(vertex)
                    return

                temp = edge[1]
                break

    if len(path) == 0:
        print("No circuit found")
    else:
        print(" -> ".join(path))

# Example
vertices = ['A', 'B', 'C', 'D']
edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')]

find_circuit(vertices, edges)