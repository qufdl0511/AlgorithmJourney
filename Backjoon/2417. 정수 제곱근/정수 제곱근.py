import sys

# 제곱근을 구하고자 하는 숫자 n
n = int(sys.stdin.readline())

# 이진 탐색 범위 초기화
start = 0
end = n

while start <= end:
    mid = (start + end) // 2
    if mid ** 2 < n:
        start = mid + 1
    else:
        end = mid - 1

print(start)