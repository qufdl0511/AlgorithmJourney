import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

# 그래프 생성
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
print("graph", graph)
# 방문 여부, 방문 했으면 0 대신에 부모 노드 저장
visited = [0]*(N+1)
# 재귀함수로 구현
def DFS(L):
    for i in graph[L]:
        if visited[i] == 0:
            visited[i] = L
            DFS(i)
DFS(1)

# 각 인덱스에 저장된 부모 노드 가져오기
for i in range(2,N+1):
    print(visited[i])