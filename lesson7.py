name = str(input('Enter your name: '))
age = int(input('Enter your age: '))

def say_hi(fc_name, fc_age):
    return f"Hi. My name is {fc_name} and I'm {fc_age} years old"

print(say_hi(name, age))


"""



name = str(input('Enter your name: '))
age = int(input('Enter your age: '))

def say_hi(name, age):
    print(f"Hi. My name is "+str(name)+" and I'm "+str(age)+" years old")
say_hi(name, age)




def greet(name, greeting):
    print(f"{greeting}, {name}!")

greet("Alice", "Hello")
print(greet)



def add_numbers(a, b):
    return a + b

result = add_numbers(3, 4)
result2 = add_numbers(4, 5)

print(result)
print(result2)

print(result+result2)


frozen_set = frozenset([1, 2, 3, 3])
my_dict = {frozen_set: "Hello"}
print(frozen_set)
print(my_dict)



my_set = {1, 2, 3}
my_set.add(4)

print(my_set)

my_set.remove(2)
print(my_set)

my_set = {1, 2, 3}
my_set.discard(2)
my_set.discard('fwsdfwfd')
print(my_set)

my_set = {1, 2, 3}
popped_element = my_set.pop()
print(popped_element)
print(my_set)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2) # union_set = set1|set2
print(union_set)
print("union 1 "+ str(union_set))

set1 = {1, 2, 3, 'fff'}
set2 = {3, 4, 5, 'ddd'}
union_set = set1|set2
print(union_set)
print("union 2 "+ str(union_set))

set1 = {1, 2, 3, 'fff'}
set2 = {3, 4, 5, 'ddd'}
set1.update(set2)
union_set = set1
print(union_set)
print("union 3 "+ str(union_set))

set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2) # intersection_set = set1&set2
print(intersection_set)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)  # difference_set = set1`set2
print(difference_set)





from collections import namedtuple

# Створення іменованого кортежу з іменованими полями 'name' та 'age'

Person = namedtuple('Person', ['name', 'age'])

person = Person(name='John', age=25)
person2 = Person(name='Ivan', age=40)

print(person.name)
print(person.age)

print(person2.name)
print(person2.age)

# Створення нового екземпляру зі зміненим значенням 'age'
updated_person = person._replace(age=30)
print(updated_person)  # Виведе Person(name='John', age=30)





from collections import OrderedDict

ordered_dict = OrderedDict()

ordered_dict['a'] = 1
ordered_dict['b'] = 2
print(ordered_dict)

value_of_a = ordered_dict['a']
print(value_of_a)

ordered_dict['a'] = 100
print(ordered_dict)  # Виведе OrderedDict([('a', 100), ('b', 2)])

if 'a' in ordered_dict:
    print("Key 'a' is present.")
else:
    print("Key 'a' is not present.")

del ordered_dict['a']
print(ordered_dict)  # Виведе OrderedDict([('b', 2)])

if 'a' in ordered_dict:
    print("Key 'a' is present.")
else:
    print("Key 'a' is not present.")

ordered_dict['c'] = 3
# ordered_dict['d'] = 4

print(ordered_dict)  # Виведе OrderedDict([('b', 2), ('c', 3)])
"""