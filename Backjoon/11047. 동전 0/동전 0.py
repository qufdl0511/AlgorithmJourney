import sys
# 돈의 종류 N, 동전 가치의 합 K
N, K = map(int, sys.stdin.readline().split())
# 돈의 종류 리스트
money_arr = []
# 돈의 수 초기화
count = 0

# 돈의 가치 저장
for _ in range(N):
    money_arr.append(int(sys.stdin.readline()))

# 큰 돈부터 사용하기 위해 내림차순 정렬
money_arr.sort(reverse=True)

# 필요한 돈의 수 최솟값 구하기
for money in money_arr:
     if K >= money:
         count += K // money
         K = K % money
print(count)