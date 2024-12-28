def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        words = get_num_words(file_contents)
        num_charecter = get_num_charecter_dict(file_contents)
        print_report(words, num_charecter, book_path)


def print_report(nb_words, nb_chars_dict, b_path):
    print(f"--- Bigin report of {b_path} ---")
    print(f"{nb_words} words found in the document")
    for key in nb_chars_dict:
        print(f"the '{key}' character was found {nb_chars_dict[key]} times")
    print("--- End report ---")


def get_num_charecter_dict(string):
    char_num ={}
    for item in string:
        lower = item.lower()
        if 'a' <= lower <= 'z':
            if lower in char_num:
                char_num[lower] += 1 
            else:
                char_num[lower] = 1     
    return char_num


def get_num_words(string):
    words = string.split()
    return len(words)


if __name__ == "__main__":
    main()