# 포도주 잔의 수 입력
N = int(input())

# dp 배열과 각 포도주의 양을 저장할 배열 선언
dp = [0] * (N + 1)
glass = [0] * (N + 1)

# 포도주 양 입력
for i in range(1, N + 1):
    glass[i] = int(input())

# 예외 처리: 포도주 잔이 1개 또는 2개인 경우
if N == 1:
    print(glass[1])
    exit()
elif N == 2:
    print(glass[1] + glass[2])
    exit()

# 초기값 설정
dp[1] = glass[1]
dp[2] = glass[1] + glass[2]
dp[3] = max(glass[1] + glass[2], glass[1] + glass[3], glass[2] + glass[3])

# 점화식 적용
for i in range(4, N + 1):
    dp[i] = max(dp[i-1], dp[i-2] + glass[i], dp[i-3] + glass[i-1] + glass[i])

# 결과 출력
print(dp[N])