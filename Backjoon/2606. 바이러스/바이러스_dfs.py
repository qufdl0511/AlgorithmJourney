import sys
sys.setrecursionlimit(10000)

# 입력 처리
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
net = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    net[a].append(b)
    net[b].append(a)

visited = [False] * (N + 1)

def dfs(node):
    visited[node] = True
    for neighbor in net[node]:
        if not visited[neighbor]:
            dfs(neighbor)

dfs(1)
print(visited.count(True) - 1)  # 1번 제외한 감염된 컴퓨터 수 출력

