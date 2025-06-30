import string
input_text = input("Введіть рядок для перетворення на hashtag: ")
text_no_punct = ''.join(c if c not in string.punctuation else ' ' for c in input_text)
words = text_no_punct.split()
capitalized = [word.capitalize() for word in words]
hashtag = '#' + ''.join(capitalized)
if len(hashtag) > 140:
    hashtag = hashtag[:140]
print(hashtag)