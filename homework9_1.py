def popular_words (text:str, words:str):
    clean_text = text.lower().split()
    vocabulary = {word: clean_text.count(word) for word in words}

    return vocabulary

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')