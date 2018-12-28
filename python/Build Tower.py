# !/usr/bin/python3
# -*- coding:utf-8 -*-

'''
Build Tower
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

Python: return a list;
JavaScript: returns an Array;
C#: returns a string[];
PHP: returns an array;
C++: returns a vector<string>;
Haskell: returns a [String];
Ruby: returns an Array;
Have fun!

for example, a tower of 3 floors looks like below

[
  '  *  ', 
  ' *** ', 
  '*****'
]
and a tower of 6 floors looks like below

[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
]
'''

def tower_builder(n_floors):
    return [('*'*i).center(n_floors*2-1) for i in range(1,n_floors*2,2)]


# print(tower_builder(1))
# print(tower_builder(2))
# print(tower_builder(3))
print(tower_builder(6))
