"""
Write a function to check whether a given string is "smashable", 
meaning that it’s a word in a predefined dictionary and can be reduced 
to a single character, one character at a time, and every intermediate 
word during the reduction is also in the dictionary of words. (Assume you 
have a file or list of valid dictionary words, like /usr/share/dict/words)
Example: Given the word SPRINT as input, it should return the following:
SPRINT → PRINT → PINT → PIT → IT → I
"""

def is_smashable(str, dictionary):
    # base case
    # pull out all one letter words from the dictionoary
    # if the input string doesnt contain any of those letters
    # return false

    # if the input containts any of the letter
    # try to build back from that
    # example input has I >>
    # I
    # IT
    # PIT
    # PINT
    # PRINT
    # SPRINT
    # do this process until length of input str is reached
    pass