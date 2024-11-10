import sys
# 단어 입력
word = sys.stdin.readline().rstrip()

# 팰린드롬 여부를 확인하는 조건
is_palindrome = True
length = len(word) // 2

# 맨 앞과 맨 뒤에서부터 비교하며 팰린드롬 확인
for i in range(length):
    if word[i] != word[-(i+1)]:
        is_palindrome = False
        break

# 결과 출력
if is_palindrome:
    print(1)
else:
    print(0)