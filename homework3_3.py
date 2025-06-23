lst = [9, "focus", [8,6,4], 98, 56]

if len(lst) == 0:
    result = [[], []] #lst
elif len(lst) % 2 == 0:
    half = len(lst) // 2
    result = [lst[:half], lst[half:]]
else:
    half = len(lst) // 2 + 1
    result = [lst[:half], lst[half:]]

print(result)