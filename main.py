# Christian Groselle Boot dev BookBot

def get_book_text(filepath):
    """
    Reads the content of a book file and returns it as a string.
    Args:
        filepath (str): The path to the book file.

    Returns:
        str: The content of the book file.
    """

    # Read the file and return the contents as a string
    with open(filepath) as f:
        return f.read()

def main():
    print(get_book_text("books/frankenstein.txt"))

main()

    