def char_count(book):
    return len(book)

def read_content(book_path):
    with open(book_path) as file:
        return file.read()

def word_count(book):
    words = book.split()
    return len(words)
    
def main():
    book_path = "books/frankenstein.txt"
    book = read_content(book_path)
    print(book) 
    print(f"The word count is {word_count(book)}")
    print(f"The character count is {char_count(book)}")

if __name__ == "__main__":
    main()
