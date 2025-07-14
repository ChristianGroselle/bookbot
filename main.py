# Christian Groselle Boot dev BookBot

from stats import get_book_text
from stats import count_words
from stats import count_chars

def main():
    book_content = get_book_text("books/frankenstein.txt")

    word_count = count_words(book_content)

    char_count = count_chars(book_content)

    print(f'{word_count} words found in the document')

    print(char_count)
main()

    