import sys
sys.setrecursionlimit(10**6)

# DFS 재귀함수를 사용하여 가장 먼 거리를 찾기 위한 함수
def find(start, now):
    # a는 연결된 노드 번호, b는 간선의 거리
    for a, b in tree[start]:
        if visited[a] == -1:
            visited[a] = b + now
            find(a, visited[a])

# 노드의 개수
n = int(sys.stdin.readline())

# 트리 생성
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c, w = map(int, sys.stdin.readline().split())
    tree[p].append([c, w])
    tree[c].append([p, w])

# 방문 여부 : 방문을 안했으면 -1, 했으면 find함수를 통해 거리를 입력
visited = [-1]*(n+1)
# 노드 1에서 시작하므로 거리를 0으로 설정
visited[1] = 0
# 루트노드 1에서 시작
find(1,0)

# 가장 먼 노드의 번호 찾기 (1번 노드에서 가장 먼 노드)
start = visited.index(max(visited))
visited = [-1]*(n+1)
# start노드에서 시작하므로 거리를 0으로 설정
visited[start] = 0
# 가장 먼 노드(start)에서 다시 가장 먼 노드를 찾기
find(start,0)

# 트리의 지름 출력
print(max(visited))