def is_even(number: int) -> bool:
    s = str(number)
    if s == '0':
        return False
    last_digit = s[-1]

    return last_digit in {'0', '2', '4', '6', '8'}