import sys

# 출입 기록의 수 입력
n = int(sys.stdin.readline().strip())

human = set()  # 출입 인원을 관리할 집합

for _ in range(n):
    log = sys.stdin.readline().strip().split()  # 한 줄을 읽고 공백 기준으로 나눔

    if log[1] == "enter":
        human.add(log[0])  # 사람이 들어오면 집합에 추가
    elif log[1] == "leave":
        human.remove(log[0])  # 사람이 나가면 집합에서 제거

# 집합을 내림차순 정렬
li = sorted(human, reverse=True)

# 정렬된 이름 출력
for name in li:
    print(name)
