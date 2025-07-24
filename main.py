def main():
    print(get_book_text("./books/frankenstein.txt")) 

def get_book_text(path):
    with open(path) as path:
        file_contents = path.read()
    return file_contents

main()