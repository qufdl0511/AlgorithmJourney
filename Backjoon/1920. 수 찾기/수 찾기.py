import sys

# 입력 받기
N = int(sys.stdin.readline())
N_arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_arr = list(map(int, sys.stdin.readline().split()))

# 이진 탐색 함수 정의
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 원하는 값 찾은 경우 인덱스 반환
        if arr[mid] == target:
            return mid
        # 원하는 값이 중간점의 값보다 작은 경우 왼쪽 부분 탐색
        elif arr[mid] > target:
            end = mid - 1
        # 원하는 값이 중간점의 값보다 큰 경우 오른쪽 부분 탐색
        else:
            start = mid + 1

    return None

# N_arr 정렬
N_arr.sort()

# M_arr의 각 원소를 N_arr에서 탐색
for i in range(M):
    result = binary_search(N_arr, M_arr[i], 0, len(N_arr) - 1)
    if result is not None:  # 값이 존재하는 경우
        print(1)
    else:  # 값이 존재하지 않는 경우
        print(0)
