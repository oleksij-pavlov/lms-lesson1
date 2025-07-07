def say_hi(name: str, age: int) -> str:
    return f"Hi. My name is {name} and I'm {age} years old"

assert say_hi("Oleksii", 18) == "Hi. My name is Oleksii and I'm 18 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')
