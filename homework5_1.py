import keyword
import string

input_text = input("Введіть ім'я змінної, ми перевіримо чи воно зарезервоване: ")
is_valid = True

if not input_text:
    is_valid = False
elif input_text in keyword.kwlist:
    is_valid = False
elif input_text[0].isdigit():
    is_valid = False
elif any(c.isupper() for c in input_text):
    is_valid = False
elif input_text == "_":
    is_valid = True
elif input_text.count("_") > 1:
    is_valid = False
else:
    allowed_chars = set(string.ascii_lowercase + string.digits + "_")
    for char in input_text:
        if char not in allowed_chars or char in string.punctuation.replace("_", "") or char.isspace():
            is_valid = False
            break
print(is_valid)
