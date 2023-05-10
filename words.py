""" Retrieve and print words from a URL.

Usage:
    python3 words.py <URL>
"""
import sys
from urllib.request import urlopen

def fetch_words(url):
    """ Fetch a list of words from a url.

    Args:
        url: The url of a UTF-8 text document.

    Returns:
    A list of strings containing the words from the document.
    
    """
    story = urlopen(url)
    story_words = []

    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    """ Print items one per line

    Args:
       An iterable serie of printable items.   
    """
    for item in items:
        print(item)


def main(url):
    """ Print each word from a text document from at a utl

    Args:
       url: The URL of a UFT-8 text document.
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])


"""
# Run it from the REPL:

PS D:\2\github\core-python> python
Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from words import *
>>> main("http://sixty-north.com/c/t.txt")


# Access the help on the REPL - It will display your comments

>>> from words import *
>>> help(fetch_words)

"""