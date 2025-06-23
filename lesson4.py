r = range(1, 11, 2) # r є об'єктом range
for i in r: # i приймає значення 1, 3, 5, 7, 9
    print(i) # виводить на екран кожне значення

"""
lst = [4, 6, 8, 7]
for i, el in enumerate(lst):
    print(i,"->", el)


# Варіант обходу списку списків за допомогою циклу for
first_list = [[1, 2, 3], [4, 5, 6]]
for lst in first_list:
    for j in lst:
        print(j)

for i in range(1, 11):
    if i < 10:
        end = "-"
    else:
        end = "\n"
    print(i, end=end)

# Це виведе на екран: 1-2-3-4-5-6-7-8-9-10


# Варіант обходу списку списків за допомогою циклу while
first_list = [[1, 2, 3], [4, 5, 6]]
i = 0
while i < len(first_list):
    j = 0
    lst = first_list[i]
    while j < len(lst):
        print(lst[j])
        j += 1
    i += 1


# виведе на екран прямокутник із символів «*».
a = int(input("Input a "))
b = int(input("Input b "))
i = 0
while i < a: # Висота
    j = 0
    while j < b: # ширина
        print("*", end='') # end='' рядок не буде переведено за замовчуванням - нова строка
        j += 1
    print()
    i += 1




# Перевірка того, що число є простим, за допомогою циклу
number = int(input("input positive number "))
i = 2
while i < number:
    if number % i == 0:
        print("It is not a prime number") # Якщо число ділиться без залишку на інше число, то це число не є простим
        break
    i = i + 1
else: # виконається тільки якщо break в циклі не буде викликаний.
    print("It is a prime number")





# Виведе на екран числа від 1 до 4
number = 0

while number <= 10:
    number = number + 1
    if number == 5:
				# Цикл завершить свою роботу тоді, коли значення number дорівнюватиме 5
        break
    print(number)
print('End')


number = 0
while number < 10:
    number = number + 1 # До continue !!!!
    if number == 5:
        continue
    print(number)


n = 1 # присвоюємо початкове значення змінній n
while n <= 10: # запускаємо цикл при умові n <= 10
	print(n) # друкуємо значення n
	n = n + 1 # збільшуємо значення n на 1
print('End')




first_list = [3, 4, 5, 4, 5, 34, 5, 35, -2]
print(first_list.index(4)) # 0 - тому, що 3 стоїть на першому місці та її індекс дорівнює 0
# ValueError якщо такого елемента у списку немає
print(first_list.index(9))

first_list = [3, 4, 5, 4, 5, 34, 5, 35, -2]
print(first_list.count(5))  # 3
first_list.count(9) # 0

first_list = [3, 4, 5, 4, 5, 34, 5, 35, -2]
print(first_list.index(3)) # 0 - тому, що 3 стоїть на першому місці та її індекс дорівнює 0
# ValueError якщо такого елемента у списку немає
print(first_list.index(9))

# кількість елементів збігається
first_list = [2, 4, 7, 11, 0, 999, 8]
first_list[1:4] = [12, 13, 14]
print(first_list) # [2, 12, 13, 14, 0, 999, 8]

# кількість елементів, які змінюємо, більше
first_list = [2, 4, 7, 11, 0, 999, 8]
first_list[1:4] = [23]
print(first_list)

# кількість елементів, які змінюємо, менша
first_list = [2, 4, 7, 11, 0, 999, 8]
first_list[1:3] = [33, 34, 35]
print(first_list) # [2, 33, 34, 35, 11, 0, 999, 8]

"""