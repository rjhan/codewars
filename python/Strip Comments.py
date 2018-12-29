# !/usr/bin/python3
# -*- coding:utf-8 -*-

'''
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
'''

def solution(string,markers):
    l = []
    
    for s in string.split("\n"):   
        for m in markers:
            if m in s:
                s = s[:s.find(m)]   
        l.append(s.rstrip())
  
    return '\n'.join(l)

def solution1(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)



print(solution1("apples, pears # and bananas\ngrapes\nbananas !!apples", ["#", "!"]))
print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
print(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")