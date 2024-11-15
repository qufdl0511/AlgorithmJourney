import sys

N = int(sys.stdin.readline())
result = 0
num = 0

for i in range(N+1):
    # 각 자리 수를 리스트화
    num_list = list(map(int, str(i)))

    for j in range(len(num_list)):
        # 각 자리 수를 더하기
        num += num_list[j]
    # 각 자리 수를 더한 값에 현재 값 더하기
    num += i

    # 현재 수와 각 자리 수의 합이 N과 같은 수인지 확인
    if num == N:
        result = i
        break

    # 각 자리 수를 초기화
    num=0

print(result)