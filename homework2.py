number = int(input("Введіть чотиризначне число: "))


if 1000 <= number <= 9999:
    digit1, remainder = divmod(number, 1000)
    digit2, remainder = divmod(remainder, 100)
    digit3, digit4 = divmod(remainder, 10)

    print(digit1)
    print(digit2)
    print(digit3)
    print(digit4)
else:
    print("Це не чотиризначне число!")
