import sys

# 정수의 개수를 입력 받기
N = int(sys.stdin.readline().strip())
# 한 줄에 공백으로 구분된 정수를 입력 받고, N개의 정수만 리스트에 추가
data = list(map(int, sys.stdin.readline().split()))

datalist = []
for i in range(N):
    datalist.append(data[i])

# 최대값, 최소값 출력
print(min(datalist), max(datalist))