# def to_float(value):
#     try:
#         return float(value)
#     except ValueError:
#         return None


# def calcMissing(readings):
#     # [{'index': 0, 'value': 289.71}, {'index': 1, 'value': 291.71}, {'index': 2, 'value': 292.46}, 
#     #  {'index': 3, 'value': None}, {'index': 4, 'value': None}, {'index': 5, 'value': 305.11}, {'index': 6, 'value': None}]
#     data = [{'index': i, 'value': to_float(r.split(' ')[1])} for i, r in enumerate(readings)]
#     print(data)

#     for row in data:
#         if row['value'] is None:
#             left_not_none = next((r for r in data[:row['index']][::-1] if r['value'] is not None), None)
#             right_not_none = next((r for r in data[row['index'] + 1:] if r['value'] is not None), None)
#             if left_not_none is None:
#                 print(right_not_none['value'])
#             elif right_not_none is None:
#                 print(left_not_none['value'])
#             else:
#                 diff_index = right_not_none['index'] - left_not_none['index']
#                 diff_value = right_not_none['value'] - left_not_none['value']
#                 print(left_not_none['value'] + diff_value / diff_index
from collections import deque

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
visited = []
q = deque()

def bfs_1(graph, visited, node):
    visited.append(node)
    q.append(node)

    while q:
        cur_res = q.popleft()
        neighbors = graph[cur_res]
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.append(neighbor)

                q.append(node)

def dfs(graph, visited, node):
    visited = []
    if node not in visited:
        visited.append(node)

        for neighbor in graph[node]:
            dfs(graph, visited, neighbor)

def bfs(adj_lst, node, visited):
    res = []
    q = deque()
    q.append(node)

    visited[node] = True

    while q:
        cur_node = q.popleft()
        res.append(cur_node)

        for i in adj_lst[cur_node]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
            

#          0
#     1          2
#    3              4
def node_node_rel(adj_lst, n1, n2):
    adj_lst[n1].append(n2)
    adj_lst[n2].append(n1)

def dfs(graph, visited, node):
    if node not in visited:
        visited.append(node)

        for neighbor in graph[node]:
            dfs(graph, visited, neighbor)

if __name__ == "__main__":
    graph = {
                '5' : ['3','7'],
                '3' : ['2', '4'],
                '7' : ['8'],
                '2' : [],
                '4' : ['8'],
                '8' : []
            }
    visited = []
    
    dfs(graph, visited, '5')
    # V = 5 

    # adj_lst = [[] for _ in range(V)]

    # visited = [False] * V

    # node_node_rel(adj_lst, 0, 1)
    # node_node_rel(adj_lst, 0, 2)
    # node_node_rel(adj_lst, 1, 3)
    # node_node_rel(adj_lst, 1, 4)
    # node_node_rel(adj_lst, 2, 4)

    # bfs(adj_lst, 0, visited)



    
