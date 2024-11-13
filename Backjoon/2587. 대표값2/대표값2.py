import sys

# 다섯 개의 자연수를 리스트에 담기 위해 변수 선언
arr = []
# 다섯 개의 자연수를 합한 값을 담기 위해 변수 선언
arrSum = 0

# 다섯 개의 자연수를 입력 받고, 리스트와 합을 구함
for _ in range(5):
    data = int(sys.stdin.readline())
    arr.append(data)
    arrSum += data

# 리스트 오름차순으로 정렬
arr.sort()

# 리스트의 평균과 중앙값 출력
print(arrSum//len(arr))
print(arr[2])