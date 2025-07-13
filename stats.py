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

def count_words(input_str):
    """
    Reads a string and returns the number of words it contains
    Args:
        input_str (str): The string to count.

    Returns:
        int: The number of words in the string.
    """

    words = input_str.split()

    return len(words)