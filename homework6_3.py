number = int(input("Введіть ціле число: "))

def multiply_digits(n):
    while n > 9:
        digits = tuple(int(d) for d in str(n))
        product = 1
        for digit in digits:
            product *= digit
        n = product
    return n

result = multiply_digits(number)
print("Результат:", result)