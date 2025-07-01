


student = {"name": "Alexander", "lastname": "Tsin", "age": 36, "group": "PN121"}
for key in student:
    print(f'key: {key}')



# for key, val in student.items():
#     print("key:", key, "val:", val)

"""
# Помилка, якщо немає такого ключа
d2 = {"A1":{1: "one", 5: "five"}, "A2":"456"}
# d2[4] # KeyError: 4

#Помилки немає, для відсутнього ключа
print(d2.get(4)) # виведе: None

# Можна встановити значення за замовчуванням для ключа, який відсутній
print(d2.get('address', {}))
print(d2) # виведе: {}



my_new_dict = {key: [] for key in [1, 2, 3] }
#рівнозначний код:
my_dict = {}
for key, value in [1,2,3]:
    my_dict[key] = []

my_new_dict[1].append('add')
print(my_new_dict) # виведе: {1: ['add'], 2: [], 3: []}


import copy

d2 = {"A1":{1: "one", 5: "five"}, "A2":"456"}
d3 = copy.deepcopy(d2)

d3["A1"][1] = "789"
print('d2 ->', d2) # виведе: d2 -> {'A1': {1: 'one', 5: 'five'}, 'A2': '456'}
print('d3 ->', d3) # виведе: d3 -> {'A1': {1: '789', 5: 'five'}, 'A2': '456'}
print(id(d2["A1"]) == id(d3["A1"])) # виведе: False




human = {"name": "Alexander",
        "lastname": "Glock",
        "age": 36,
        "address": {"street": "Lisova", "house": 87, "flat": 705}
}

house = human["address"]["house"]
print(house) # виведе: 87

# Міняємо значення для квартири
human["address"]["flat"] = 700
print(human["address"]["flat"]) # виведе: 700




print(hash((1,5)))



# 1. Пустий словник
d1 = dict()
print(type(d1)) # виведе: <class 'dict'>

d2 = {}
print(type(d2)) # виведе: <class 'dict'>

# Створюємо словник з трьох елементів
d = {
    "name": "Alice",
    "age": 25,
    "hobbies": ["reading", "writing", "coding"]
}

# Виводимо тип та довжину словника
print(type(d)) # виведе: <class 'dict'>
print(len(d)) # виведе: 3

# Отримуємо доступ до елементів словника за ключем
print(d["name"]) # виведе: Alice
print(d["age"]) # виведе: 25
print(d["hobbies"]) # виведе: ['reading', 'writing', 'coding']

# Змінюємо значення за ключем
d["age"] = 26
print(d["age"]) # виведе: 26

# Додаємо новий елемент до словника
d["city"] = "London"
print(d) # виведе: {'name': 'Alice', 'age': 26, 'hobbies': ['reading', 'writing', 'coding'], 'city': 'London'}


# Створення словника з допомогою конструктора dict
SEASONS = dict(Winter=1, Spring=2, Summer=3, Autumn=4)
print(SEASONS) # виведе: {'Winter': 1, 'Spring': 2, 'Summer': 3, 'Autumn': 4}

# Створення словника, із заздалегідь заданого набору ключ-значення
pairs = [('IBM', 125), ('ACME', 50), ('PHP', 40)]
d = dict(pairs)
print(d) # виведе: {'IBM': 125, 'ACME': 50, 'PHP': 40}


my_dict = {
    1:"hello",
    2:"hello2",
    31:"hello3"
}

print(my_dict[31])


lst = ['a', 'b']
my_tuple = (1, 2, lst, 4, 5)
print(my_tuple) # виведе: (1, 2, ['a', 'b'], 4, 5)

my_tuple[2][1] = 999 # змінюємо елемент списка
print(my_tuple) # виведе: (1, 2, ['a', 999], 4, 5




t1 = (42,)
t2 = [10, 20, 30]
t3 = tuple(t2)
tpl = t1 + t3
print(tpl) # виведе: (42, 10, 20, 30)



# Створюємо кортеж з трьох елементів
t = (1, "hello", [3, 4, 5])

# Виводимо тип та довжину кортежу
print(type(t)) # виведе: <class 'tuple'>
print(len(t)) # виведе: 3

# Отримуємо доступ до елементів кортежу за індексом
print(t[0]) # виведе: 1
print(t[1]) # виведе: hello
print(t[2]) # виведе: [3, 4, 5]

# Спробуємо змінити елемент кортежу
#t[0] = 2 # викине виняток TypeError: 'tuple' object does not support item assignment


# Створюємо кортеж з одного елементу
t = (42,) # необхідна кома, інакше буде ціле число
print(type(t)) # виведе: <class 'tuple'>

t = (6) # без коми буде ціле число
print(type(t)) # виведе: <class 'int'>

# Створюємо кортеж без дужок
t = 1, 2, 3
print(type(t)) # виведе: <class 'tuple'>

# Створюємо кортеж з іншого ітерованого об'єкта
t = tuple("hello")
print(t) # виведе: ('h', 'e', 'l', 'l', 'o')

# Змінюємо значення двох змінних за допомогою кортежу
a = 10
b = 20
a, b = b, a # еквівалентно (a, b) = (b, a)
print(a) # виведе: 20
print(b) # виведе: 10


# Створюємо рядок з українськими символами
s = "Привіт, світ!"

# Виводимо тип та довжину рядка
print(type(s)) # виведе: <class 'str'>
print(len(s)) # виведе: 11


# Кодуємо рядок в байти за допомогою кодування UTF-8
b = s.encode("utf-8")

# Виводимо тип та довжину байтів
print(type(b)) # виведе: <class 'bytes'>
print(len(b)) # виведе: 19
print(b) # виведе: b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd1\x96\xd1\x82, \xd1\x81\xd0\xb2\xd1\x96\xd1\x82!'

# Декодуємо байти назад в рядок за допомогою кодування UTF-8
s = b.decode("utf-8")

# Виводимо тип та довжину рядка
print(type(s)) # виведе: <class 'str'>
print(len(s)) # виведе: 11
print(s) # виведе: Привіт, світ!

# Якщо вказати неправильне кодування, то отримаємо кракозябри
print(b.decode('windows-1251'))  # виведе: РџСЂРёРІС–С‚, СЃРІС–С‚!
"""