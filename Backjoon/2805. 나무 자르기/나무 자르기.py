import sys

# 나무의 수 M, 가져가려는 나무의 길이 N
N, M = map(int, sys.stdin.readline().split())

# 나무의 길이 리스트
tree_arr = list(map(int, sys.stdin.readline().split()))

# 이진 탐색 초기값
start, end = 0, max(tree_arr)
result = 0

while start <= end:
    mid = (start + end) // 2  # 중간값
    # mid보다 긴 나무만 자른 나무 길이 합 계산
    tree_len = sum(tree - mid for tree in tree_arr if tree > mid)

    if tree_len >= M:  # 필요한 나무 길이를 충족
        result = mid  # 현재 높이를 저장
        start = mid + 1  # 높이를 더 높게 설정
    else:
        end = mid - 1  # 높이를 더 낮게 설정

# 절단기 높이의 최대값 출력
print(result)