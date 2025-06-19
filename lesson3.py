first_list = [2, 4, 7, 11, 0, -2, 8]
my_list = first_list[3:6]

print(my_list) # [11, 0, -2]

# від початку та до 5 го індексу
print(first_list[:5]) # [2, 4, 7, 11, 0]

# починаючи з 3-го індексу і до кінця
print(first_list[3:]) # [11, 0, -2, 8]

# від початку та до кінця (копія)
print(first_list[:]) # [2, 4, 7, 11, 0, -2, 8]

# від початку і до кінця з кроком 2
print(first_list [::2]) # [2, 7, 0, 8]

# У зрізах можна використати і негативні значення індексів
print(first_list[-5: -1: 2])  # [7, 0]

#  Копія списку з елементами у зворотному напрямку
a = first_list[::-1]
print(a) # [8, -2, 0, 11, 7, 4, 2]







"""
l = [[]] * 3
print(l)

# Всі три елементи новоствореного списку - це один і той же список
print(id(l[0]))
print(id(l[1]))
print(id(l[2]))


first_list = [2, 4, 7]
my_list = first_list * 3
print(my_list) # [2, 4, 7, 2, 4, 7, 2, 4, 7]


lst_lst = [[1, 2, 545], [4, 5, 1223311, "fast"]]
print(len(lst_lst)) # виведе 2
print(len(lst_lst[0])) # виведе 3
print(len(lst_lst[1])) # виведе 4



lst = [3, 1, 4, 1, 5]
size = len(lst) # size буде рівне 5
print(size) # виведе 5 на екран


lst = [3, 1, 4, 1, 5, 9, 2, 6, 5]
if 2 not in lst:
	print("2 не входить до списку lst")
else:
	print("2 входить до списку lst")



lst = [3, 1, 4, 1, 5, 9, 2, 6, 5]
if 2 in lst:
	print("2 входить до списку lst")
else:
	print("2 не входить до списку lst")



lst = [3, 1, 4, 1, 5, 9, 2, 6, 5]
lst.pop() # Останній елемент списку
lst.pop(-1) # Останній елемент списку
print(lst)



lst = [3, 1, 4, 1, 5, 9, 2, 6, 5]
x = lst.pop(0) # повертає значення 3 і видаляє його зі списку і присвоює його змінній
print(lst) 
print(x)




lst = [3, 2, 4, 1, 5, 9, 2, 6, 1, 5]
lst.remove(1) # видаляє перше входження 1 зі списку
print(lst) # 





empty_lst = []

empty_lst.insert(2, "left")
print(empty_lst) # [5]

empty_lst.insert(2, 66)
print(empty_lst) # [5, 66]

empty_lst.insert(1, 7)
print(empty_lst) # [5, 7, 66]




lst = []
lst.append(2)
lst.append(3.1)
lst.append(['42', 1])
lst.append('ffff')
print(lst)
lst[1] = 765
print(lst)
lst.insert(1,264)
print(lst)


lst_lst = [
    [9, 12, 3],
    [4, [22,7], 46],
    [9, 10, 84],
]

print(lst_lst[0]) # Перший "рядок" [9, 12, 3]
print(lst_lst[1]) # Другий "рядок" [4, 5, 46]

print(lst_lst[1][2]) # Останній елемент другого рядка 46 (lst_lst[1][-1])
print(lst_lst[2][1]) # Другий елемент (1) третього списку (2)
print(lst_lst[1][1][0])




lst1 = [1, 3.6, 9, "Hello", [2, "o"]]
lst2 = list('Hello world')

print(lst1[-1]) # Останній елемент списку (lst1[5])

lst = []
list3 = list()


a = 1123 #None
b = None #1123
c = b or a #Що перше повернуло true
print(c)



number_b = 2
# Ці 2 коди однакові
if number_b < 5:
	number_a = 10
else:
	number_a = 20
# Ці 2 коди однакові
nuber_a = 10 if number_b < 5 else 20



number_a = 17

if not number_a > 20:
    print("Yes")
else:
    print("No")


orange_price = 15.5
my_money = 11
tea_price = 12
banana = 10

if my_money > orange_price:
    print("I buy orange")
elif my_money > tea_price:
    print ("Not orange, just tea")
elif my_money > banana:
    print("Not orange, not tea, just banana")
else:
    print("I buy apple")
print('OK')



number1 = int(input("Введіть перше число "))
action = input("Введіть дію (+,-,*,/)")
number2 = int(input("Введіть друге число "))

if action == "+"
    result = number1 + number2
elif action == "-"
    result = number1 + number2
elif action == "*"
    result = number1 * number2
elif action == "/"
    result = number1 / number2
elif action == "/" and number2 == 0:
    result = "не можна длити на нуль"
print("result")
    
    

orange_price = 17.5
my_money = 20
tea_price = 14

if my_money > orange_price:
    print("I buy orange")
else:
    # Вкладений умовний оператор if зі своїм блоком else
    if my_money > tea_price:
        print("Not orange, just tea")
    else:
        print("I buy apple")
print("The end")




# В данному випадку завжди буде виконано лише один блок коду - або той,
# що знаходиться в if, або той, що в else
orange_price = 7.5
my_money = 7.5

if my_money >= orange_price:
	print("I buy orange")
else:
	print("I buy apple")
print("The end")



orange_price = 17.5
my_money = 20

if my_money > orange_price:

	# Цей набір команд буде виконано лише в тому випадку,
	# коли my_money буде більшим, ніж orange_price
    my_money -= orange_price
    # my_money = my_money - orange_price
    print("I buy orange")
    print(my_money)
print("The end")
"""