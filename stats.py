
def get_num_words(book_contents):    
    return len(book_contents.split())

def count_characters(book_contents):
    char_count = {}
    for char in book_contents:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    return char_count


def sort_on(items):
    return items["num"]



def sort_char(char_count):
    char_list = []
    for chars in char_count:
        char_list.append({"char": chars, "num": char_count[chars]})

    
    char_list.sort(reverse=True, key=sort_on)
    return char_list