my_graph = {
    4: [2,3],
    2: [19,8],
    19: [2,6],
    6: [19,8],
    8: [2,3],
    3: [9],
    9: [3]
}

def traverse_graph(graph, node):
    visited = set()
    traversal_order = []
    traversal_order = dfs(graph, node, visited, traversal_order)

    print(traversal_order)

def dfs(graph, node, visited, traversal_order):
    if node not in visited:
        traversal_order.append(node)
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(graph, neighbor, visited, traversal_order)
    return traversal_order

if __name__ == "__main__":

    traverse_graph(my_graph, 4) 