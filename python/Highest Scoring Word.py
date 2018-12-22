# !/usr/bin/python3
# -*- coding : utf-8 -*-

""" 
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to it's position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid. 
"""


def high(x):
    return max(x.split(" "),key=lambda k:sum(ord(i)-96 for i in k))


print(high('man i need a taxi up to ubud'))
print(high('what time are we climbing up the volcano'))
print(high('take me to semynak'))