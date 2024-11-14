import sys

# 입력 받을 숫자의 개수, 임의의 수 입력 받기
N, M = map(int, sys.stdin.readline().split())
# 리스트 입력
arr = list(map(int, sys.stdin.readline().split()))

# 결과 변수 초기화
result = 0

# i, j, k의 모든 조합을 확인
for i in range(N):
    for j in range(i + 1, N):  # i 다음 인덱스부터 시작하여 중복 제거
        for k in range(j + 1, N):  # j 다음 인덱스부터 시작하여 중복 제거
            # 세 숫자의 합 계산
            data = arr[i] + arr[j] + arr[k]
            # 합이 M 이하이고, 최대 합을 찾는 경우 result를 업데이트
            if data <= M and data > result:
                result = data

print(result)