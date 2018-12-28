# !/usr/bin/python3
# -*- coding:utf:8 -*-

'''
Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

Example:

solution('XXI') # should return 21
Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
'''
def solution(roman):
    dict = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
    x = 0

    while len(roman)>0:
        if roman[:2] in dict.keys():
            x += dict[roman[:2]]
            roman = roman.replace(roman[:2],"",1)
        else:
            x += dict[roman[:1]]
            roman = roman.replace(roman[:1],"",1)            

    return x

#这个思路暂时还没有实现，但现在的方法不能满足
# def solution1(roman):
#     from functools import reduce
#     d = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
#     return reduce(lambda x,y: x+y if x>=y else y-x , (d[c] for c in roman))


print(solution("XXI"))
print(solution("MCMXC"))
print(solution("XIV"))
print(solution("XIX"))
