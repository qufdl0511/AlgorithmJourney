import sys

# 출입 기록의 수 입력
n = int(sys.stdin.readline().strip())

login = []  # 들어온 사람
logout = []  # 나간 사람

for _ in range(n):
    log = sys.stdin.readline().strip().split()

    if log[1] == "enter":
        login.append(log[0])  # 들어온 사람 기록
    elif log[1] == "leave":
        logout.append(log[0])  # 나간 사람 기록

# 로그아웃에 없는 사람만 남기는 함수 정의
def filter_remaining(person):
    if person not in logout:
        return person
    return None

# map을 사용해 필터링
remaining = map(filter_remaining, login)

# 결과를 정렬하고 None을 제외한 이름 출력
for name in sorted(filter(None, remaining), reverse=True):
    print(name)
