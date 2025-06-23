lst = [1, 0, 13, 0, 0, 0, 5]
result = []
zero_count = 0
for num in lst:
    if num != 0:
        result.append(num)
    else:
        zero_count += 1
for _ in range(zero_count):
    result.append(0)
print(result)