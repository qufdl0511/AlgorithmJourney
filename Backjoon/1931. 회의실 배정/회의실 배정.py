import sys
# 회의실 수 N
N = int(sys.stdin.readline())
# 회의실 리스트
arr = []
# 사용할 수 있는 회의실 수
count = 0
# 회의가 끝나는 시간
f_time = 0

# 회의 시간 저장
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

# 종료 시간을 기준으로 회의 시간 정렬 (종료 시간 우선, 종료 시간이 같으면 시작 시간으로 정렬)
arr.sort(key=lambda x: (x[1], x[0]))  # 종료 시간, 그 다음 시작 시간 기준으로 정렬

# 회의실을 사용할 수 있는지 확인
for i in range(N):
    s_time = arr[i][0]
    e_time = arr[i][1]

    if s_time >= f_time:  # 이전 회의 종료 시간이랑 겹치지 않으면 회의 가능
        count += 1
        f_time = e_time  # 회의 끝난 시간 업데이트

print(count)