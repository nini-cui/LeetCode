# def dfs_implementation(data, visited, key):
#     if key not in data:
#         return None
    
#     # for value in data[key]:
#     #     if value not in visited:
#     #         visited.append(value)
#     #         dfs_implementation(data, visited, value)

#     if key not in visited:
#         visited.append(key)
#         for neighbour in data[key]:
#             dfs_implementation(data, visited, neighbour)

#     return visited

def dfs_implementation(data, visited, key):
    if key not in data:
        return None
    
    if key not in visited:
        visited.append(key)
        for child in data[key]:
            dfs_implementation(data, visited, child)

def dfs(key):
    data = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E'],
    }

    visited = []
    result = dfs_implementation(data, visited, key)

    return result

if __name__ == "__main__":
    res = dfs('A')
    
