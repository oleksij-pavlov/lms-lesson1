def is_even(number: int) -> bool:
    s = str(number)
    last_digit = s[-1]
    return last_digit in {'0', '2', '4', '6', '8'}

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')