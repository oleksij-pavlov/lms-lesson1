

my_string1 = "😍"
print(my_string1.isalpha())

my_string2 = "😍"
print(my_string2.isdigit())



"""

my_string = "Beautiful is better than ugly"

# є символи, які не є літерами (пробіл)
print(my_string.isalpha()) # виведе:  False

my_string1 = "😍"
print(my_string1.isalpha())

my_string2 = "😍"
print(my_string2.isdigit())

print(my_string2)



lst = [2, 3, 5] # join працює тільки з типом даних "рядок"
print("".join(lst)) # TypeError: sequence item 0: expected str instance, int found

# варіант того, як можна "на льоту" перевести число в рядок
x = "".join([str(y) for y in lst])
print(x) # виведе: 235
print(type(x)) # виведе: <class 'str'>

my_lst = ['I', 'like', 'Python']
# пробіл, як символ для з'єднання елементів зі списку
_string = " ".join(my_lst)
print(_string) # виведе: I like Python

# рядок, це також об'єкт, що ітерується.
my_str = "I like Python"
_string = "_".join(my_str)
print(_string) # виведе: I_ _l_i_k_e_ _P_y_t_h_o_n

my_str = "I like Python"
_string1 = "".join(my_str)
print(_string1)


my_string = "I like   Python"
lst = my_string.split()
print(lst) # виведе: ['I', 'like', 'Python']


my_string = "i like python"
my_string = my_string.title()
print(my_string)  # виведе: I Like Python


my_string = "I like Python"
my_string1 = my_string.upper() # Результат зберігаємо в іншій змінній
my_string2 = my_string.lower()
print(my_string1) # виведе: I LIKE PYTHON
# Початковий рядок залишився незмінним
print(my_string) # виведе: I like Python
print(my_string2)



variable1 :str = "1"
variable2 = str(1)
variable3 :str = 1
print(variable1, variable2)
print(type(variable1))
print(type(variable2))
print(type(variable3))



string1 = ("Python"+ "fsefsf"+ "ffdsf", )
print(string1, sep='->')

"""