from collections import deque, defaultdict

def bfs(sor, des):
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E'],
    }

    visited = []
    level = 1
    level_map = defaultdict(list)
    q = deque([(sor, level)])
    visited.append(sor)

    while q:
        current_node, level = q.popleft()
        level_map[level].append(current_node) 

        for child in graph[current_node]:
            if child not in visited:
                visited.append(child)
                q.append((child, level+1))

    res = level_map
    return res

if __name__ == "__main__":
    bfs('A', 'F')
            
    
