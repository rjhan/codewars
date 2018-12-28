# !/usr/bin/python3
# -*- coding:utf-8 -*-

'''
Build Tower Advanced
Build Tower by the following given arguments:
number of floors (integer and always greater than 0)
block size (width, height) (integer pair and always greater than (0, 0))

Tower block unit is represented as *

Python: return a list;
JavaScript: returns an Array;
Have fun!

for example, a tower of 3 floors with block size = (2, 3) looks like below

[
  '    **    ',
  '    **    ',
  '    **    ',
  '  ******  ',
  '  ******  ',
  '  ******  ',
  '**********',
  '**********',
  '**********'
]
and a tower of 6 floors with block size = (2, 1) looks like below

[
  '          **          ', 
  '        ******        ', 
  '      **********      ', 
  '    **************    ', 
  '  ******************  ', 
  '**********************'
]
Go take a look at Build Tower which is a more basic version :)
'''
#最开始没有读懂题意，这道题与基础班的差别就是给定了block_size,block_size包含了(w,h)
#每行中元素的个数要乘w，每行要重复 h遍

def tower_builder(n_floors, block_size):
    w, h = block_size
    return [('*'*i*w).center((n_floors*2-1)*w) for i in sorted(list(range(1,n_floors*2,2))*h)]


print(tower_builder(3,(2,3)))