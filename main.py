def get_char_dict(book):
    chars_dict = {}

    for char in book:
        lower_char = char.lower()

        if lower_char in chars_dict:
            chars_dict[lower_char] += 1
        else:
            chars_dict[lower_char] = 1

    return chars_dict

def extend_dictionary(alpha_dict):
    return dict(sorted(alpha_dict.items(), key=lambda x: x[1], reverse = True))

def remove_non_alpha(dict):
    for char in list(dict):
        if char.isalpha() == False:
           del dict[char]
    return dict
    

def print_report(file_path, word_count, report_dict):
    # header
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")

    #space
    print("\n")

    # print char count descending order 
    for char in report_dict:
        print(f"The {char} character was found {report_dict[char]} times")

    print("--- End report ---")


def read_content(book_path):
    with open(book_path) as file:
        return file.read()

def get_word_count(book):
    words = book.split()
    return len(words)

def main():
    book_path = "books/frankenstein.txt"
    book = read_content(book_path)
    word_count = get_word_count(book)

    # create a dictionary with alphabetical character as keys and
    # their character count in the book as the value.
    # sorted in descending order
    char_dict = get_char_dict(book) # initial dictionary with char count
    alpha_dict = remove_non_alpha(char_dict) # removes non alphabetic chars
    report_dict = extend_dictionary(alpha_dict) # sorts chars on frequency
    
    # final CLI report
    print_report(book_path, word_count, report_dict)

if __name__ == "__main__":
    main()
