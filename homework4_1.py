lst = [1, 0, 13, 0, 0, 0, 5]
result = []
i = 0
for num in lst:
    if num != 0:
        result.append(num)
    else:
        i += 1
for _ in range(i):
    result.append(0)
print(result)