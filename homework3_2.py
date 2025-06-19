lst = [9, "focus", [8,6,4]]

if len(lst) > 1:
    lst_revert = [lst[-1]] + lst[:-1]
else:
    lst_revert = lst
print(lst_revert)