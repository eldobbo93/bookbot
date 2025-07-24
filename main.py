def main():
    text = get_book_text("./books/frankenstein.txt")
    word_count = count_words(text)
    print(f"{word_count} words found in the document") 

def get_book_text(path):
    with open(path) as path:
        file_contents = path.read()
    return file_contents

def count_words(text):
    return len(text.split())

main()