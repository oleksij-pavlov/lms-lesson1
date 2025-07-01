import string
inp = input("Введіть дві літери через дефіс (наприклад, a-c): ")
start, end = inp.split("-")
letters = string.ascii_letters
start_index = letters.index(start)
end_index = letters.index(end)
print(letters[start_index:end_index + 1])