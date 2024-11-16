import sys
# 주어 지는 명령의 수
N = int(sys.stdin.readline())
arr = []

for i in range(N):
    inputs = sys.stdin.readline().split()
    order = inputs[0]
    num = inputs[1] if len(inputs) > 1 else None

    if order == "push":
        arr.append(num)
    elif order == "pop":
        if arr:
            print(arr.pop())
        else:
            print(-1)
    elif order == "size":
        print(len(arr))
    elif order == "empty":
        if arr:
            print(0)
        else:
            print(1)
    elif order == "top":
        if arr:
            print(arr[-1])
        else:
            print(-1)