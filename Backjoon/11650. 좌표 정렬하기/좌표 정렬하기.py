import sys
# 점의 개수 N
N = int(sys.stdin.readline().rstrip())

# 점의 좌표 입력 받기
arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

# arr[x, y]라고 할 때 arr[x]를 기준으로 정렬 (arr[x]가 같으면, 그 다음 arr[y] 기준으로 정렬)
arr.sort(key=lambda x: (x[0], x[1]))

# 정렬된 값 출력
for i in range(N):
    print(*arr[i])