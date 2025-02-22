from collections import deque
import sys

# 명령의 수 입력
N = int(sys.stdin.readline())

# deque 초기화
queue = deque()

for _ in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        queue.append(cmd[1])
    elif cmd[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        print(1 if not queue else 0)
    elif cmd[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
