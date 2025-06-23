lst = [0, 1, 7, 2, 4, 8]
if lst:
    index = 0
    for i in range(0, len(lst), 2):
        index += lst[i]
    result = index * lst[-1]
else:
    result = 0
print(result)