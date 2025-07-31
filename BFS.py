graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(graph)
from collections import deque

def bfs(start_node):
    visited = set()
    queue = deque(start_node)
    while queue:
        node=queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph.get(node,[]))
bfs("A")




