import sys
# 수의 개수 입력
n = int(sys.stdin.readline())
dataList = []
for i in range(n):
    data = int(sys.stdin.readline())
    dataList.append(data)

# 리스트 오름차순으로 정렬
dataList.sort()

# 결과를 한 줄에 하나씩 출력
for i in dataList:
    print(i)