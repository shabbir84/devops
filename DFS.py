graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(graph,node,visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end= " ")
        visited.add(node)
    for neighbour in graph.get(node, []):
        dfs(graph, neighbour, visited)
dfs(graph,"A")