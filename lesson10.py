def decorator_with_args(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix}: Something is happening before the function is called.")
            result = func(*args, **kwargs)
            print(f"{prefix}: Something is happening after the function is called.")
            return result
        return wrapper
    return decorator

@decorator_with_args("LOG")
def say_hello():
    print("Hello!")


# Виклик функції з декоратором із аргументами
say_hello()

"""
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Виклик функції з декоратором
say_hello()



def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
print(closure)
print(closure(15))
result = closure(5)
print(result)  # Вивід: 15

"""