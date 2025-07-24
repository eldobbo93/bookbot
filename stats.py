def count_words(text):
    return len(text.split())

def count_each_char(text):
    res = {}
    for char in text.lower():
        if char in res:
            res[char] += 1
        else:
            res[char] = 1
    return res