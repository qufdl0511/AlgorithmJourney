import sys
# 행렬의 크기 N과 M
N, M = map(int, sys.stdin.readline().split())

# 행렬 A와 B 선언
A, B = [], []

# 행렬 A값 입력
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    A.append(a)

# 행렬 B값 입력
for i in range(N):
    b = list(map(int, sys.stdin.readline().split()))
    B.append(b)

# 행렬 A와 B의 합 출력
for i in range(N):
    for j in range(M):
        result = A[i][j] + B[i][j]
        print(result, end=' ')
    print()