"""


VARIABLE = 123 # Глобальна змінна (великими)

variable1 :str = "1"
variable2 :int = 1
variable3 :float = 1.2

year_of_independence = 1991 # snake_case
_some_variable = 1 # Валідний код
myVariable = 2 # Невалідний код

print(id(variable3))

"""

"""
Блочний коментар
"""


"""

print(id(variable1))
print(id(variable2))
"""


"""
mutable
Списки, словники, сети - змінюються на льоту

immutable


l = [1, 2, "к"] # Це змінна типу list, який є змінюванним
print(l) # Виведе [1, 2, 3]
print(id(l)) # Виведе 4377070080. Для кожного запуску кода це значення – різне
l.append(4)
print(l) # Виведе [1, 2, 3, 4]
print(id(l)) # Виведе 4377070080. Таке ж саме значення


x = 1
print(x) # 1
print(type(x)) # <class 'int'>

print(2 ** 2) # Виведе 4
print(3 ** 2) # Виведе 9
print(2 ** 3) # Виведе 8



print(divmod(11, 2)) # Виведе (5, 1)
div, mod = divmod(11, 2)
print(div) # Виведе 5, тобто результат 11 // 2
print(mod) # Виведе 1, тобто результат 11 % 2


import math
print(math.sqrt(9)) # Виведе 3.0. sqrt від Square root – корінь квадратний.
"""


user_input = int(input("Please enter the integer number: ")) # Нехай користувач надрукував 4

print(type(user_input)) # <class 'str'>
print(int(user_input / 2)) # TypeError
number = int(user_input)
print(number / 2) # Виведе 2
print("hello", "world", sep="\n")

