import sys
# 테스트 케이스의 개수
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    # 테스트 케이스 입력 받기
    n = int(sys.stdin.readline().rstrip())

    # dp 배열 초기화
    dp = [0] * (n + 1)

    # 작은 입력값 처리
    if n < 4:
        print(1)
    elif n == 4:
        print(2)
    else:
        # 초기값 설정
        dp[1] = 1
        dp[2] = 1
        dp[3] = 1
        dp[4] = 2

        # 점화식 사용
        for i in range(5, n + 1):
            dp[i] = dp[i-1] + dp[i-5]

        # 결과 출력
        print(dp[n])
