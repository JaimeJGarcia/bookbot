def char_count(book):
    chars_dict = {}

    for char in book:
        lower_char = char.lower()

        if lower_char in chars_dict:
            chars_dict[lower_char] += 1
        else:
            chars_dict[lower_char] = 1

    return chars_dict

def sort_on(dict):
    return dict["num"]
    
def extend_dictionary(alpha_dict):
    print(dict(sorted(alpha_dict.items(), key=lambda x: x[1], reverse = True)))
    


def remove_non_alpha(dict):
    for char in list(dict):
        if char.isalpha() == False:
           del dict[char]

    return dict
    

def print_report(file_path, word_count, char_dict):
    # header
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")

    #space
    print("\n\n")

    # while char in 
    #char_dict.sort(reverse = True, key = sort_on)
    #print(char_dict)

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
    char_dict = char_count(book)
    print(f"character count:\n {char_dict}")
    alpha_dict = remove_non_alpha(char_dict)
    print(alpha_dict)
    extend_dictionary(alpha_dict)


if __name__ == "__main__":
    main()
