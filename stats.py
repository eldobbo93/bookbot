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

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    list=[]
    for i in dict:
        char_dict = {}
        char_dict["char"] = i
        char_dict["num"] = dict[i]
        list.append(char_dict)
    list.sort(reverse=True, key=sort_on)
    return list