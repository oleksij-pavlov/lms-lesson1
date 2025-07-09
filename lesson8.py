def example_function(arg1, *args, arg2=2, **kwargs):
    print(arg1)
    print(args)
    print(arg2)
    print(kwargs)

example_function(1, 3, 5, arg2=4, arg3=6, arg4=8)


"""
def example_function(arg1, arg2, arg3):
    print(arg1, arg2, arg3)

kwargs = {'arg1': 1, 'arg2': 2, 'arg3': 3}
example_function(**kwargs)




def example_function(arg1, arg2, arg3):
    print(arg1, arg2, arg3)

args = (1, 2, 3)
example_function(*args)



def example_function(positional_arg, positional_arg2, *args, **kwargs):
    print("Positional Arg:", positional_arg, positional_arg2)
    print("Additional Positional Args:", args)
    print("Additional Named Args:", kwargs)

def example_function_with_named_arg(named_arg):
    print("Named Arg:", named_arg)

# Виклик функції з використанням різних видів аргументів
example_function(1, *range(3, 6), keyword_arg="value")

# Виклик функції з використанням іменованих аргументів
example_function_with_named_arg(named_arg=2)
example_function(1, 3, 4, 5, keyword_arg="value")


def example_function(**kwargs):
    print(kwargs.get("param1", 123))
    for key, value in kwargs.items():
        print(key, value)

# Виклик функції з різною кількістю іменованих аргументів
example_function(
    param1=1,
    param2=2,
    param3=3,
    param31=31,
    param32=32
)




def example_function(param1, param2, **kwargs):
    print(param1, param2)
    for value in kwargs:
        print(value)

# Виклик функції з різною кількістю іменованих аргументів
example_function(1, 2, 3, 4, "fwefw", True)

example_function(param1=1, param2=2)


def example_function(param1, param2, *args):
    print(param1, param2)
    for value in args:
        print(value)

# Виклик функції з різною кількістю іменованих аргументів
example_function(1, 2, 3, 4, "fwefw", True)
example_function(param1=1, param2=2)



def example_function(*args):
    for arg in args:
        print(arg)

# Виклик функції з різною кількістю позиційних аргументів
example_function(1, 2, 3, 4, 5)




def example_function(param1, param2=2, param3=3):
    print(param1, param2, param3)

# Виклик без вказання параметрів за замовчуванням
example_function(1)  # Використовуються значення за замовчуванням для param2 і param3

# Зміна значення одного з параметрів
example_function(1, param3=4)  # Вказуємо значення для param3, інші залишаються за замовчуванням


global_variable = 10

def outer_function():
    outer_variable = 5

    def inner_function():
        inner_variable = 3
        print(inner_variable)  # Local (локальна)
        print(outer_variable)  # Enclosing (обхоплююча)
        print(global_variable) # Global (глобальна)

    inner_function()

outer_function()

"""