UNVISITED = 0
VISITED = 1
VISITING = -1


def construct_graph(vertices, edges):
    graph = [[] for _ in range(len(vertices))]
    for u, v in edges:
        graph[u].append(v)
    return graph


def dfs(node, s, graph, visited, max_paths):
    if visited[node] == VISITED:
        return False
    if visited[node] == VISITING:
        return True
    visited[node] = VISITING
    for neighbor in graph[node]:
        if dfs(neighbor, s, graph, visited, max_paths):
            return True
    for neighbor in graph[node]:
        for c in range(26):
            max_paths[node][c] = max(max_paths[node][c], max_paths[neighbor][c])
    max_paths[node][ord(s[node]) - 65] += 1
    visited[node] = VISITED
    return False


def solution(s, edges):
    graph = construct_graph(s, edges)
    visited = [UNVISITED for _ in range(len(s))]
    max_paths = [[0 for _ in range(26)] for _ in range(len(s))]
    for node in range(len(s)):
        if visited[node] == UNVISITED and dfs(node, s, graph, visited, max_paths):
            return None
    res = 0
    for i in range(len(s)):
        for j in range(26):
            res = max(res, max_paths[i][j])
    return res
