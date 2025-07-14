def get_book_text(filepath):
    """
    Reads the content of a book file and returns it as a string.
    Args:
        filepath (str): The path to the book file.

    Returns:
        str: The content of the book file.
    """
    print(f"Analyzing book found at {filepath}...")
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

def count_chars(input_str):
    """
    Reads a string and returns the number of times that each char appears
    Args:
        input_str (str): The string to count

    Returns:
        dict(int): dict of ints containing the count for each char 
    """

    char_dict = {}

    for character in input_str.lower():
        if character not in char_dict.keys():
            char_dict[character] = 0    
        char_dict[character] += 1
    
    return char_dict

def format_chars(input_dict):
    """

    """
    def sort_on(items):
        return items["num"]
    
    formatted_list = []
    for key in input_dict:
        # Skip non alphanumric chars
        if not key.isalpha():
            continue
        formatted_list.append({"char": key, "num": input_dict[key]})

    formatted_list.sort(reverse=True, key=sort_on)
    return formatted_list
