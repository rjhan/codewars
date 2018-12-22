# !/usr/bin/python3
# -*- coding:utf-8 -*-

'''
Implement the function unique_in_order which takes as argument a sequence and 
returns a list of items without any elements with the same value next to each other 
and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]

'''
def unique_in_order1(iterable):
    l = []

    for i in iterable:
        if len(l)==0 or i!=l[-1]:
            l.append(i)
    return l


def unique_in_order2(iterable):
    return [v for k,v in enumerate(iterable) if len(iterable)<=1 or v!=iterable[k-1]]

print(unique_in_order1('AAAABBBCCDAABBB'))
print(unique_in_order1('ABBCcAD'))
print(unique_in_order1([1,2,2,3,3]))
print(unique_in_order1(''))

print(unique_in_order2('AAAABBBCCDAABBB'))
print(unique_in_order2('ABBCcAD'))
print(unique_in_order2([1,2,2,3,3]))
print(unique_in_order2([]))

