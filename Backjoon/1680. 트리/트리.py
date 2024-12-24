import sys

n = int(sys.stdin.readline())
graph = list(map(int, sys.stdin.readline().split()))  # [-1, 0, 0, 1, 1]
erase = int(sys.stdin.readline())

def dfs(v):
    graph[v] = -2 # 노드를 없앤다는 뜻으로 -2 값을 임의로 둠
    for i in range(n):  # 전체 트리 반복
        if v == graph[i]:  # 지우려는 노드 v가  graph[i]에 들어 있으면 graph[i]는 v의 자식
            dfs(i)  # i의 자식도 지움

dfs(erase)
cnt = 0

for i in range(n):
    if graph[i] != -2 and i not in graph:  # -2는 지운 노드, i노드의 자식이 트리 안에 없으면 리프노드
        cnt += 1

print(cnt)