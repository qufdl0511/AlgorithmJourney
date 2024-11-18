from collections import deque
import sys

# 명령의 수 입력
N = int(sys.stdin.readline())

# deque 초기화
queue = deque()

for _ in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "1":
        queue.appendleft(cmd[1]) # 데크의 왼쪽에 삽입
    elif cmd[0] == "2":
        queue.append(cmd[1]) # 데크의 오른쪽에 삽입
    elif cmd[0] == "3":
        if queue:
            print(queue.popleft()) # 데크의 왼쪽 끝 요소를 빼고 출력
        else:
            print(-1)
    elif cmd[0] == "4":
        if queue:
            print(queue.pop()) # 데크의 오른쪽 끝 요소를 빼고 출력
        else:
            print(-1)
    elif cmd[0] == "5":
        print(len(queue)) # 데크에 들어있는 정수의 개수를 출력
    elif cmd[0] == "6":
        print(1 if not queue else 0) # 데크가 비어있는지 확인
    elif cmd[0] == "7":
        if queue:
            print(queue[0]) # 데크에 정수가 있다면 맨 앞의 정수를 출력
        else:
            print(-1)
    elif cmd[0] == "8":
        if queue:
            print(queue[-1]) # 데크에 정수가 있다면 맨 뒤의 정수를 출력
        else:
            print(-1)