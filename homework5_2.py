while True:
    number_a = int(input("Введіть перше число: "))
    number_b = int(input("Введіть друге число: "))
    action = input("Введіть дію (+, -, *, /): ")
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
        print(f"Результат: {result}")
    continue_calc = input("Бажаєте продовжити? (y/yes для продовження): ").lower()
    if continue_calc not in ["y", "yes"]:
        print("Роботу завершено.")
        break