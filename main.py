# Christian Groselle Boot dev BookBot

import sys

from stats import get_book_text, count_words, count_chars, format_chars

def main():
    print("============ BOOKBOT ============")

    # Get path from args
    args = sys.argv

    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_content = get_book_text(sys.argv[1])
    word_count = count_words(book_content)

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    char_count = count_chars(book_content)

    sorted_chars = format_chars(char_count)

    print("--------- Character Count -------")
    for i in sorted_chars:
        print(f"{i["char"]}: {i["num"]}")

    print("============= END ===============")

main()

    