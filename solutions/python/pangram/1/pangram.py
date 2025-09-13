import re
import string


def is_pangram(sentence: str):
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(set(sentence.lower()))
