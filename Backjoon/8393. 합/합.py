import sys

n = int(sys.stdin.readline())
result = sum(i for i in range(n + 1))

# 1부터 N까지의 합
print(result)