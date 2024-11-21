import sys

n = int(sys.stdin.readline())
# 리스트 0으로 초기화
dp = [0] * (n + 1)

# 피보나치 수열 함수 정의
def fib(n):
    # 0일 때와 1일 때는 피보나치 수의 합이 적용되지 않으므로 값을 미리 할당
    dp[0] = 0
    dp[1] = 1

    # 두 번째부터 피보나치 수의 합 구하기
    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[n]

print(fib(n))
