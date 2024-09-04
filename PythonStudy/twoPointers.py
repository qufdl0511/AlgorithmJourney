n = 5
m = 5
data = [1, 2, 3, 4, 5]
count = 0
interval_sum = 0
end = 0

for start in range(n):
    while end < n and interval_sum < m:
        interval_sum += data[end]
        end += 1

    if interval_sum == m:
        count += 1

    interval_sum -= data[start]

    # 디버깅 출력
    print(f"Start: {start}, End: {end}, Interval Sum: {interval_sum}, Count: {count}")

print(count)
