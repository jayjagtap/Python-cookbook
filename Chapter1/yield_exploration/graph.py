
from collections import defaultdict, deque
undirected_graph_edges = [
    [4,9], [17,11], [11,19], [9,11], [4,17], [13,14],[17,20]
]

directed_graph_edges = [
    [4,9], [17,11], [11,19], [9,11], [4,17], [13,14],[17,20]
]
# *********************************************************************************************************************************************
def make_undirected_graph(undirected_graph_edges):
    graph = defaultdict(set)

    for edge in undirected_graph_edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])
    
    return graph

def make_directed_graph(directed_graph):
    graph = defaultdict(set)
    indegree = defaultdict(int)
    for edge in directed_graph:
        graph[edge[0]].add(edge[1])
        indegree[edge[1]]+=1
        # Initialize defaults
        graph[edge[1]]
        indegree[edge[0]]

    return graph, indegree

def dfs_graph(graph):
    """
    Covers disconnected graphs
    """
    visited = set()
    dfs_order = []
    for node in graph.keys():
        if node not in visited:
            # print("Node: ", node, "dfs_order: ", dfs_order)
            dfs(node, graph, visited, dfs_order)

    return dfs_order

def bfs_graph(graph):
    """
    Given a graph, prints bfs order for all nodes including disconnected graphs.
    """
    visited = set()
    bfs_order = []
    for node in graph.keys():
        if node not in visited:
            # print("Node: ", node, "visited: ", visited)
            bfs(node, graph, visited, bfs_order)
    
    return bfs_order
# *********************************************************************************************************************************************


def dfs(node, graph, visited, dfs_order):
    """
    Given a node return dfs_order for all connected components
    """
    visited.add(node)
    dfs_order.append(node)

    for nbor in graph[node]:
        if nbor not in visited:
            dfs(nbor, graph, visited, dfs_order)
    
    return dfs_order



def bfs(node, graph, visited={}, bfs_order=[]):
    Q = deque()
    Q.append(node)
    visited.add(node)

    while Q:
        front = Q.popleft()
        bfs_order.append(front)

        for nbor in graph[front]:
            if nbor not in visited:
                Q.append(nbor)
                visited.add(nbor)

    return bfs_order
    
def topological_sort(graph, indegree):
    
    Q = deque(node for node in indegree if indegree[node] == 0)
    sorted_order = []
    
    if not Q:  # if there are no source nodes, the graph is a loop and dependencies cannot be resolved.
        return None   
    
    while Q:
        front = Q.popleft()
        sorted_order.append(front)
        for nbor in graph[front]:
            indegree[nbor]-=1
            if indegree[nbor] == 0: # New source created, this node has no dependencies, we can add this to the list
                Q.append(nbor)
            
    if len(sorted_order) != len(graph): return None  # Smaller loops in graph

    return sorted_order

if __name__ == "__main__":
    
# *********************************************************************************************************************************************
    print("*********************************************************************************************************************************************")
    graph = make_undirected_graph(undirected_graph_edges)
    print(graph)
    
    # Print DFS traversal 
    print("DFS order for above graph: ", dfs_graph(graph))

    # Print BFS Traversal
    print("BFS order for above graph: ", bfs_graph(graph))
# *********************************************************************************************************************************************
    print("*********************************************************************************************************************************************")
    # Directed Graph
    graph, indegree = make_directed_graph(directed_graph_edges)
    print(graph)
    print(indegree)

    # Print DFS traversal 
    print("DFS order for above graph: ", dfs_graph(graph))

    # Print BFS Traversal
    print("BFS order for above graph: ", bfs_graph(graph))
# *********************************************************************************************************************************************
    print("*********************************************************************************************************************************************")
    # toplogical sort.
    edges = [
        [4,9], [4,13], [4,10], [10,13], [10,15], [18,15]
    ]

    graph, indegree = make_directed_graph(edges)
    print("Toplogical Sort")
    print("Graph: ", graph)
    print("indegree: ", indegree)
    print("Sorted order: ", topological_sort(graph, indegree))
