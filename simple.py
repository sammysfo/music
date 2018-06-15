#!/usr/bin/env python3
"""Module for turning a command line prompted text-string into a series of
musical notes.

Usage:

    python3 simple.py
"""

import re
import string


notes = ['C','C#','Db','D','D#','Eb','F','F#','Gb','G','G#','Ab','A','A#','Bb','B']
alphas_to_notes = dict(zip(notes, string.ascii_lowercase))


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
split the phrase into consonants and vowels.

    Args:
        Phrase to be processed.

    Returns:
        Tuple of vowels and consonants for unpacking.
    """
    cleaned = re.sub(r'[^A-Za-z]', '', phrase).lower()

    vowels = []
    consonants = []
    for x in list(cleaned):
        if re.search(r'[aeiouy]', x):
            vowels.append(x)
        else:
            consonants.append(x)

    return vowels, consonants


def print_phrase(phrase):
    """Prints the vowels and consonants of a phrase to STDOUT.

    Args:
        Phrase to be printed
    """
    vowels, consonants = process_phrase(phrase)
    print("vowels are: {}".format(vowels))
    print("consonants are: {}".format(consonants))

def main():
    """Take a string and transorm it into a series of musical notes.

    """
    phrase = get_phrase()
    print_phrase(phrase)


if __name__ == '__main__':
    main()
