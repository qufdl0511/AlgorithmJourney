# 방법1. for문 사용하기
import sys

n = int(sys.stdin.readline())
result = sum(i for i in range(n + 1))

# 1부터 N까지의 합
print(result)

#방법2. 수학 공식 사용하기
import sys

n = int(sys.stdin.readline())
result = n * (n + 1) // 2

# 1부터 N까지의 합
print(result)

# 시간복잡도의 차이
# for문은 0부터 n+1까지 n번 순회하기 때문에 시간복잡도는 O(n)
# 수학 공식은 단순히 1번의 연산으로 n의 크기와 상관없으므로 시간복잡도는 O(1)