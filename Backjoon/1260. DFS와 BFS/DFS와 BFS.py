from collections import deque

# 입력 받기
N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호가 작은 것을 먼저 방문하기 위해 정렬
for i in graph:
    i.sort()

# DFS 함수
visited_dfs = [False] * (N + 1)
dfs_result = []

def dfs(V):
    visited_dfs[V] = True
    dfs_result.append(V)
    for i in graph[V]:
        if not visited_dfs[i]:
            dfs(i)

# BFS 함수
visited_bfs = [False] * (N + 1)
bfs_result = []

def bfs(V):
    queue = deque([V])
    visited_bfs[V] = True
    while queue:
        v = queue.popleft()
        bfs_result.append(v)
        for i in graph[v]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                queue.append(i)

# 함수 호출
dfs(V)
bfs(V)

# 결과 출력
print(" ".join(map(str, dfs_result)))
print(" ".join(map(str, bfs_result)))
