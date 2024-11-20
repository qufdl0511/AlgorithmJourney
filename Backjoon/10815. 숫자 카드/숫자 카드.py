import sys

# 가지고 있는 숫자 카드 개수
N = int(sys.stdin.readline())
# 숫자 카드를 dict의 key로 저장
cards = {}
num = list(map(int, sys.stdin.readline().split()))
for i in range(N):  # N을 명시적으로 사용
    cards[num[i]] = 1  # 카드 존재 여부를 나타내기 위해 1 저장

# 확인 해야 할 숫자 카드 개수
M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 결과 출력
for i in range(M):  # M을 명시적으로 사용
    if arr[i] in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')
