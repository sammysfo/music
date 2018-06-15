#!/usr/bin/env python3
"""Module for turning a command line prompted text-string into a series of
musical notes.

Usage:

    python3 simple.py
"""

import re


notes = ['C','C#','Db','D','D#','Eb','F','F#',
         'Gb','G','G#','Ab','A','A#','Bb','B']
stops_affricates_fricatives = list('bcdfghjkpqsstvzz')
alphas_to_notes = dict(zip(stops_affricates_fricatives, notes))

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
split the phrase into consonants and vowels and stops, affricates, and
fricatives.

    Args:
        Phrase to be processed.

    Returns:
        Tuple of vowels and consonants and safs for unpacking.
    """
    cleaned = re.sub(r'[^A-Za-z]', '', phrase).lower()

    vowels = []
    consonants = []
    safs = []
    for x in list(cleaned):
        if re.search(r'[aeiou]', x):
            vowels.append(x)
        else:
            consonants.append(x)

        if x in stops_affricates_fricatives:
            safs.append(x)

    return vowels, consonants, safs


def print_parts(phrase):
    """Prints the vowels and consonants and SAF's of a phrase.

    Args:
        Phrase to be printed
    """
    vowels, consonants, safs = process_phrase(phrase)
    print("vowels are: {}".format(vowels))
    print("consonants are: {}".format(consonants))
    print("saf's are: {}".format(safs))

def safs_to_notes(safs):
    pass

def main():
    """Take a string and transorm it into a series of musical notes.

    """
    phrase = get_phrase()
    print_parts(phrase)


if __name__ == '__main__':
    main()
