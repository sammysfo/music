#!/usr/bin/env python3
"""Module for turning a command line prompted text-string into a series of
musical notes.

Usage:

    python3 simple.py
"""


import re

def get_phrase():
    """Prompt the user to enter a phrase

    Args:
        None.

    Returns:
        The string captured from command line input.
    """
    phrase = input("Enter a phrase: ")
    return phrase


def clean_phrase(phrase):
    """Remove all characters that aren't [A-Za-z] from a phrase, lc the result.

    Args:
        Phrase to be cleaned up.

    Returns:
        The cleaned up phrase.
    """
    cleaned = re.sub(r'[^a-zA-Z]', '', phrase).lower()
    return cleaned


def print_phrase(phrase):
    """Prints whatever phrase is passed to it to STDOUT.

    Args:
        Phrase (string)
    """
    print(phrase)


def main():
    """Take a string and transorm it into a series of musical notes.

    """
    print_phrase(clean_phrase(get_phrase()))


if __name__ == '__main__':
    main()
