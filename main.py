import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1] 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    frankenstein = get_book_text(book)
    from stats import get_num_words
    num_words = get_num_words(frankenstein)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    from stats import count_characters
    char_count = count_characters(frankenstein)
    #print(f"{char_count}")
    from stats import sort_char
    sorted_char = sort_char(char_count)
    for keys in sorted_char:
        if keys["char"].isalpha():
            print(f"{keys["char"]}: {keys["num"]}")
    print("============= END ===============")
 

main()