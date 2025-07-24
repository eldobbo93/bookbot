from stats import count_words, count_each_char

def main():
    text = get_book_text("./books/frankenstein.txt")
    word_count = count_words(text)
    char_count = count_each_char(text)
    print(f"{word_count} words found in the document")
    print(char_count) 

def get_book_text(path):
    with open(path) as path:
        file_contents = path.read()
    return file_contents

main()