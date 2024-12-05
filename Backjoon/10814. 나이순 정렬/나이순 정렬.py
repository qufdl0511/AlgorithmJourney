import sys
# 온라인 저지 회원의 수 N
N = int(sys.stdin.readline().rstrip())

# 각 회원의 나이와 이름 입력 받기
arr = []
for i in range(N):
    arr.append(list(sys.stdin.readline().split()))

# arr[x, y]라고 할 때 arr[x]를 기준으로 정렬
arr.sort(key=lambda x: int(x[0]))

# 정렬된 값 출력
for i in range(N):
    print(*arr[i])