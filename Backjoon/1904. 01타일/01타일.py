n = int(input())

if n == 0:  # n이 0일 때 예외 처리
    print(0)
elif n == 1:  # n이 1일 때 처리
    print(1)
elif n == 2:  # n이 2일 때 처리
    print(2)
else:
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

    print(dp[n])
