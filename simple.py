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


def process_phrase(phrase):
    """Remove all characters that aren't [A-Za-z] from a phrase, lc that,
split the phrase into a list of characters for assignement to notes.

    Args:
        Phrase to be processed.

    Returns:
        List of characters derived from the phrase.
    """
    cleaned = re.sub(r'[^a-zA-Z]', '', phrase).lower()
    return list(cleaned)


def print_phrase(phrase):
    """Prints whatever phrase is passed to it to STDOUT.

    Args:
        Phrase (string)
    """
    print(phrase)


def main():
    """Take a string and transorm it into a series of musical notes.

    """
    processed = process_phrase(get_phrase())
    print_phrase(processed)


if __name__ == '__main__':
    main()
