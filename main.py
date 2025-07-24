from stats import count_words, count_each_char, sort_dict, sort_on

def main():
    print("============ BOOKBOT ============")
    book="./books/frankenstein.txt"
    text = get_book_text(book)
    print("Analyzing book found at " + book)
    
    print("----------- Word Count ----------")
    word_count = count_words(text)
    print(f"Found {word_count} total words")
    
    print("--------- Character Count -------")
    char_count = count_each_char(text)
    sorted_char_count = sort_dict(char_count) 
    for i in sorted_char_count:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as path:
        file_contents = path.read()
    return file_contents

main()