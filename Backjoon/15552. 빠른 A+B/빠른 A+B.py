import sys

# 입력 받을 개수를 첫 번째 줄에서 입력 받기
T = int(sys.stdin.readline().rstrip())

# 결과를 저장할 리스트 생성
result = []

# 각 테스트 케이스에 대해 처리
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    result.append(A + B)

# 결과 반환
for i in range(T):
    print(result[i])