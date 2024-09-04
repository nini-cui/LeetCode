from collections import deque

# def bfs_implementation(graph, visited, val):
#     q = deque()
#     q.append(val)
#     visited.append(val)

#     while q:
#         current_node = q.popleft()

#         neighbors = graph[current_node]
#         for neighbor in neighbors:
#             if neighbor not in visited:
#                 visited.append(neighbor)
#                 q.append(neighbor)
    
#     return visited

# def bfs_implementation(graph, visited, val):
#     q = deque()
#     q.append(val)
#     visited.append(val)
#     res = []
    
#     while q:
#         current_node = q.popleft()
#         adj_nodes = graph[current_node]
#         for adj_node in adj_nodes:
#             if adj_node not in visited:
#                 visited.append(adj_node)
#                 q.append(adj_node)

#     return res 

def bfs_implementation(graph, val):
    visited = set()
    
    q = deque([val])
    visited.append(val)

    while q:
        current_node = q.popleft()
        for adj_node in graph[current_node]:
            if adj_node not in visited:
                visited.append(adj_node)
                q.append(adj_node)

def bfs(val):
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E'],
    }

    result = bfs_implementation(graph, val)
    # visited = []

    # result = bfs_implementation(graph, visited, val)
    return result

if __name__ == "__main__":
    bfs('A')
            
    
