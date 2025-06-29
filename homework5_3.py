import string
input_text = input("Введіть рядок для перетворення на hashtag: ")
clean_text = ''.join(c for c in input_text if c not in string.punctuation and not c.isspace())
words = input_text.split()
hashtag = '#' + ''.join(word.capitalize() for word in words)
if len(hashtag) > 140:
    hashtag = hashtag[:140]
print(hashtag)