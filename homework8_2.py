import string

def is_palindrome(text):
    allowed = string.ascii_lowercase + string.digits
    text = text.lower()

    cleaned = ""
    for char in text:
        if char in allowed:
            cleaned += char

    return cleaned == cleaned[::-1]