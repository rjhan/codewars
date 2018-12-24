# ! /usr/bin/python3
# -*- coding:utf-8 -*-

'''
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and 
numeric digits that occur more than once in the input string. 
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
'''
from collections import Counter

#常规解法，遍历每个字符串
def duplicate_count1(text):
    s = text.lower()
    return len([x for x in set(s) if s.count(x)>1])

#利用Counter,Counter可以进行集合的增减
def duplicate_count(text):
    s= text.lower()
    return len(Counter(s)-Counter(set(s)))



print(duplicate_count("abcde"),'=>0')
print(duplicate_count("aabbcde"),'=>2') 
print(duplicate_count("aabBcde"),'=>2')
print(duplicate_count("abcdea"),'=>1')
print(duplicate_count("indivisibility"),'=>1')
print(duplicate_count("Indivisibilities"),'=>2')
print(duplicate_count("aA11"),'=>2')
print(duplicate_count("ABBA"),'=>2')