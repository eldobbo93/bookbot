from stats import count_words, count_each_char, sort_dict, sort_on
import sys

def main():
    #Check correct number of args given
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    book=sys.argv[1]
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