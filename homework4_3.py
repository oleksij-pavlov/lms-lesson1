import random
length = random.randint(3, 10)
lst = [random.randint(0, 10) for _ in range(length)]
lst1 = [lst[0], lst[2], lst[-2]]
print(lst, lst1, sep='-->')