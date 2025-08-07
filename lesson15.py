# Приклад створення класу, що ітерується, і ітератора

class Goods:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Goods [name = {self.name}, price = {self.price}]"

class BasketIterator:
    """ Клас ітератор, який знає як обробляти наповнення Кошика,
    щоб віддавати по одному елементу при кожному запиті
    """

    def __init__(self, goods_list):
        """При ініціалізації отримує список товарів
        і встановлює значення індексу 0"""
        self.goods_list = goods_list
        self.index = 0

    def __next__(self):
        """ Якщо значення індексу не виходить за межі розміру
        списку, надаємо елемент Кошика.
        В іншому випадку - викликаємо виняток"""
        if self.index < len(self.goods_list):
            res = self.goods_list[self.index]
            self.index = self.index + 1
            return res
        else:
            raise StopIteration

    def __iter__(self):
        return self

class Basket:
    def __init__(self, user):
        self.user = user
        self.goods_list = list()

    def add_good(self, good):
        self.goods_list.append(good)

    def __str__(self):
        result = f"User: {self.user}\n"
        for good in self.goods_list:
            result += str(good)+"\n"
        return result

    def __iter__(self):
        """Повертаємо екземпляр класу Ітератора"""
        return BasketIterator(self.goods_list)

basket = Basket("Alexander_Ts")

a = Goods("Apple", 35)
b = Goods("Milk", 50)

basket.add_good(a)
basket.add_good(b)

# Пройдемося циклом по елементах кошика
for good in basket:
    print(good)
# Додамо ще одну позицію товару до кошику
c = Goods("Oil", 100)
basket.add_good(c)

# І знову пройдемося циклом по елементах кошика
for good in basket:
    print(good)


basket = Basket("Alexander_Ts")

a = Goods("Apple", 35)
b = Goods("Milk", 50)

basket.add_good(a)
basket.add_good(b)
# Побачимо, що в кошику є товар
print(basket)
# User: Alexander_Ts
# Goods [name = Apple, price = 35]
# Goods [name = Milk, price = 50]

# Спроба передати об'єкт кошика в цикл, спричинить помилку
# TypeError: 'Basket' object is not iterable
for good in basket:
    print(good)




"""

a = "Hello"
# b = a.__iter__()
b = iter(a)
print(type(b)) # виведе  <class 'str_iterator'>
print(next(b))

a = (2, 4)
b = a.__iter__()
print(type(b)) # виведе <class 'tuple_iterator'>
print(next(b))
print(b)  #  виведе <tuple_iterator object at 0x7f09dc3db760>






# Ітератор Функція iter() приймає якийсь ітерабельний об'єкт,
# наприклад список, і повертає ітератор для цього об'єкта.
#
# Функція next() приймає якийсь ітератор і повертає наступний елемент з нього.
# Якщо елементів більше немає, то функція викликає виняток StopIteration.

lst = [1, 2, 3, 4, 5]
it = iter(lst)

# it - це ітератор для списку lst
print(type(it)) # <class 'list_iterator'>
print(next(it)) # виведе 1
print(next(it)) # виведе 2
print(next(it)) # виведе 3
print(next(it)) # виведе 4
print(next(it)) # виведе 5
# print(next(it)) # викличе виняток StopIteration







class UserSequence:
 # Реалізація послідовності квадратів чисел, що підтримує звернення за допомогою зрізів

    def __init__(self, number):
        self.number = number

    def __getitem__(self, index):
        # перевірка того, що індекс це об'єкт зрізу
        if isinstance(index, slice):
            # перевірка коректності значень об'єкт зрізу
            if index.start and index.start < 0:
                raise IndexError
            elif index.stop and index.stop > self.number:
                raise IndexError
            result = []
            # встановлення конкретних значень зрізу, якщо такі не були задані
            start = 0 if index.start is None else index.start
            stop = self.number if index.stop is None else index.stop
            reverse = False
            # якщо значення кроку від'ємне, значить буде перевернута послідовність
            if index.step and index.step < 0:
                reverse = True
                step = index.step * (-1)
            else:
                step = 1 if index.step is None else index.step
            # процес формування послідовності
            for i in range(start, stop, step):
                result.append(i ** 2)
            # перевертаємо послідовність, якщо reverse = True
            return list(reversed(result)) if reverse else result

        if isinstance(index, int):
            if index < self.number:
                return index ** 2
            else:
                raise IndexError
        raise TypeError

    def __len__(self):
        return self.number


seq = UserSequence(10)

print(seq[1:8])  # [1, 4, 9, 16, 25, 36, 49]
print(seq[:10:2])  # [0, 4, 16, 36, 64]
print(seq[:])  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(seq[::-1])  # [81, 64, 49, 36, 25, 16, 9, 4, 1, 0]








class UserSequence:
# Реалізація послідовності квадратів чисел

    def __init__(self, number):
        self.number = number

    def __getitem__(self, index):
        if index < self.number:
            return index ** 2 # поверне квадрат значення index
        else:
            raise IndexError

    def __len__(self):
        return self.number

seq = UserSequence(10)
# Отримуємо елементи послідовності у циклі
for i in range(len(seq)):
    print(seq[i], end=', ') # виведе 0, 1, 4, 9, 16, 25, 36, 49, 64, 81,

# Можемо отримати елемент послідовності за індексом
# print(seq[9]) # виведе 81

# Можемо отримати всі елементи послідовності у вигляді списку
print(list(seq))  # виведе [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Спроба отримати зріз, як у звичайному об'єкті, що ітерується, приведе до помилки
# print(seq[2: 4])




class PositiveValue:

    def __init__(self):
        self.val = None

    def __get__(self, instance_self, instance_class):
        return self.val

    def __set__(self, instance_self, value):
        if value < 0:
            raise ValueError('Value must be greater than zero')
        self.val = value


class Box:
    x = PositiveValue()
    y = PositiveValue()
    z = PositiveValue()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

box = Box(1, 2, 3)
print(box.x) # виведе 1

box.x = -1  # ValueError
box = Box(1, 2, -3)  # ValueError






class Coordinate:

    def __init__(self):
        self.value = None

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value

    def __delete__(self, instance):
        print("deleter")
        del self.value

class Point:
    x = Coordinate()
    y = Coordinate()

# Get
point1 = Point()

point1.x = 11
point1.y = 22

print(point1.x)  #  виведе 10
print(point1.y)  #  виведе 12

# Set
point2 = Point()
print(point2.x, point2.y) # виведе None None

point2.x = 22
point2.y = 33

print(point2.x, point2.y) # виведе 50 20

# Delete
point3 = Point()

point3.x = 33
point3.y = 44
print(point3.x, point3.y)  # виведе 50 20

del point3.x
print(point3.x) # AttributeError: 'Coordinate' object has no attribute 'value'
print(point3)







class Human:

    def __init__(self, last_name, first_name, patronymic, gender, age, height, weight):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight

    def show_inform(self):
        full_name = f'Full Name: {self.full_name}\n'
        gender_age = f'Gender: {self.gender}\nAge: {self.age}\n'
        height_weight = f'Height: {self.height} cm\nWeight: {self.weight} kg'
        all_info = full_name + gender_age + height_weight
        return all_info

    @property  #cashed_property
    def full_name(self):
        # Перетворення функції (методу) у звичайне поле
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    @property
    def short_full_name(self):
        return f'{self.last_name} {self.first_name[0].title()}.{self.patronymic[0].title()}.'

h = Human('Лучко', 'Петро', 'Петрович', 'male', 25, 185, 91)

print(h.full_name) # Лучко Петро Петрович
print(h.short_full_name) # Лучко П.П.
print(h.last_name) # Лучко

print(h.show_inform())  # звернення до методу
















class Cat:
    def __init__(self, _name, age):
        self.__name = _name
        self.age = age

    name = property() # Створення властивості name без методів контролю

    @name.getter
    def name(self):
        print("call get name")
        return self.__name

    @name.setter
    def name(self, name_value):
        print("call set name")
        self.__name = name_value

    @name.deleter
    def name(self):
        print("call remove name")
        del self.__name

cat = Cat('Barsik', 3)
print(cat.name)  # getter
cat.name =  "Devil" # setter
del cat.name  # deleter






class Cat:
    def __init__(self, _name, age):
        self.__name = _name
        self.age = age

    @property
    def name(self):
        return self.__name

cat = Cat('Barsik', 3)
cat.name =  "Devil" # AttributeError: can't set attribute
# del cat.name # AttributeError: can't delete attribute





class Cat:
    def __init__(self, _name, age):
        self.__name = _name   # захищене поле
        self.age = age

    def get_name(self): # Метод для читання
        print("call get name")
        return self.__name

    def set_name(self, name_value): # Метод для запису
        print("call set name")
        self.__name = name_value

    def del_name(self): # Метод видалення
        print("call remove name")
        del self.__name

    # Створення властивості name
    name = property(get_name, set_name, del_name, " Cat name")

    def __str__(self):
        msg = "Cat [ name = {}, age = {}]"
        return msg.format(self.name, self.age)

cat1 = Cat("Vaska", 6)
cat1.name = "Barsic"  # буде викликаний метод set_name
print(cat1.name)  # буде викликаний метод get_name
print(cat1)








class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        msg = "Cat [ name = {}, age = {}, color = {}]"
        return msg.format(self.name, self.age, self.color)

    def __getattr__(self, atr_name):
        if atr_name == "type":
                return "Home Cat"
        print(atr_name)
        return "11"

    def __getattribute__(self, atr_name):
        return object.__getattribute__(self, atr_name)

    def __setattr__(self, attr_name, attr_value):
        self.__dict__[attr_name] = attr_value

    def __setattr__(self, attr_name, attr_value):
        print("set field -> ", attr_name)
        self.__dict__[attr_name] = attr_value

    def __delattr__(self, attr_name):
        # Видаляємо поле з внутрішньої структури об'єкта
        print("remove field -> ", attr_name)
        del self.__dict__[attr_name]

cat = Cat('Barsik', 3, 'black')

setattr(cat, "name", "Bob") # змінює ім'я на Bob
# cat.name = "bob1"
setattr(cat, "age", 5) # змінює вік на 5
setattr(cat, "color", "red") # змінює колір на red

cat.type =  "Devil"
print(cat.type)   # виведе Devil
print(cat)


cat2 = Cat('Barsik', 3, 'black')
dct = {'name': "Voland", "age": 45, "color": "black"}

for key, val in dct.items():
    # Встановимо нові значення для полів об'єкта
    setattr(cat2, key, val)

print(cat2)  # виведе Cat [ name = Voland, age = 45, color = black]


cat3 = Cat('Barsik', 3, 'black')

# delattr(cat3, 'color')
del cat3.color
print(cat3)







import math

pow_math = getattr(math, 'pow')
print(pow_math(4, 2)) # виведе 16



class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        msg = "Cat [ name = {}, age = {}, color ={}]"
        return msg.format(self.name, self.age, self.color)

    def __getattr__(self, atr_name):
        return None # pass


cat = Cat('Barsik', 3, 'black')
print(cat.name)  # виведе Barsik

# Звернення до поля, якого немає
print(cat.type)  # виведе  None

print(getattr(cat, "name")) # виведе Barsik
print(getattr(cat, "age")) # виведе 3
print(getattr(cat, "color")) # виведе black


cat1 = Cat('Mursik', 4, 'white')
fields = ['age', 'name', 'color']
for field in fields:
    print(getattr(cat1, field))

"""