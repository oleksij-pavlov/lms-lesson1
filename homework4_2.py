lst = [0, 1, 7, 2, 4, 8]
if lst:
    i = 0
    for index in range(0, len(lst), 2):
        i += lst[index]
    result = i * lst[-1]
else:
    result = 0
print(result)