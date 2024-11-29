import sys
# 테스트 케이스의 개수
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    # 테스트 케이스 입력 받기
    n = int(sys.stdin.readline().rstrip())

    # dp 배열 초기화
    dp = [0] * (n + 1)

    # 1, 2, 3일 경우 값 선언
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    else:
        # 초기값 설정
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4

        # 점화식 사용
        for i in range(4, n + 1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        # 결과 출력
        print(dp[n])
