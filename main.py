def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_num_words(text)
    num_charecter = get_num_character_dict(text)

    #print report
    print_report(words, num_charecter, book_path)


def print_report(nb_words, nb_chars_dict, b_path):
    print(f"--- Begin report of {b_path} ---")
    print(f"{nb_words} words found in the document")
    print()

    for key in sorted(nb_chars_dict.items(), key=lambda x : x[1], reverse=True):
        print(f"the '{key[0]}' character was found {key[1]} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        lecture = f.read()
    return lecture


def get_num_words(string):
    words = string.split()
    return len(words)


#get a dict of {"char": appear n time in text}
def get_num_character_dict(string):
    char_num ={}
    for item in string:
        lower = item.lower()
        if 'a' <= lower <= 'z':
            if lower in char_num:
                char_num[lower] += 1 
            else:
                char_num[lower] = 1     
    return char_num


if __name__ == "__main__":
    main()