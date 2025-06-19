number_a = int(input("Введіть перше число: "))
action = input("Введіть дію (+, -, *, /): ")
number_b = int(input("Введіть друге число: "))

if action == "/" and number_b == 0:
    print("Помилка: не можна ділити на нуль.")
else:
    if action == "+":
        result = number_a + number_b
    elif action == "-":
        result = number_a - number_b
    elif action == "*":
        result = number_a * number_b
    elif action == "/":
        result = number_a / number_b
    else:
        result = "Невідома операція"
    print(result)