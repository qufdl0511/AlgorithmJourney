import sys

# 총 금액 X를 입력 받기
X = int(sys.stdin.readline())

# 영수증에 적힌 구매한 물건의 종류의 수 N
N = int(sys.stdin.readline())

# 각 물건의 가격 저장값
result = 0

# 각 물건 값에 대해 처리
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    result += a*b

# 결과 반환
if X == result:
    print('Yes')
else:
    print('No')