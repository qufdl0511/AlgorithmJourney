# 계단의 수 입력
N = int(input())

# dp에 사용할 배열과 각 계단에 저장할 값을 선언
dp = [0] * (N+1)
stairs = [0] * (N+1)

# 계단에 해당되는 숫자 입력 받기
for i in range(1, N+1):
    stairs[i] = int(input())

# 첫번째, 두번째 계단 값 설정
if N == 1:
    print(stairs[1])
    exit()
elif N == 2:
    print(stairs[1] + stairs[2])
    exit()

# 세번째 계단부터 점화식 적용
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
for i in range(3, N+1):
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

# 최대값 출력
print(dp[N])
