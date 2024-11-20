import sys
# 1. 출입 기록의 개수를 입력 받습니다.
N = int(sys.stdin.readline())
# 2. dict를 정의합니다.
my_dict = {}

for _ in range(N):
    # 3. 주어지는 출입 기록을 사람 이름과 출입 상태로 구분합니다.
    name, state = sys.stdin.readline().split()
    # 4. 출입 상태에 따라 dict에 add & remove를 합니다.
    if state == "enter":
        my_dict[name] = True
    else:
        del my_dict[name]

# 5. dict 내부의 key들을 사전 역순으로 정렬합니다.
sorted_dict = sorted(my_dict.keys(), reverse=True)
# 6. 원소를 출력합니다.
for x in sorted_dict:
    print(x)