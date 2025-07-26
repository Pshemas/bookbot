import sys
from stats import count_words, count_chars, create_char_stats


def get_book_text(filepath_relative: str) -> str:
    with open(filepath_relative) as bookfile:
        bookfile_contents = bookfile.read()
    return bookfile_contents


def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = args[1]
    book = get_book_text(filepath)
    words_cnt = count_words(book)
    # print(f"{words_cnt} words found in the document")
    char_cnt = count_chars(book)
    # print(char_cnt)
    print(
        f"""============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {words_cnt} total words
--------- Character Count -------"""
    )
    char_stats = create_char_stats(char_cnt)
    for item in char_stats:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')
    print("============= END ===============")


if __name__ == "__main__":
    main()
