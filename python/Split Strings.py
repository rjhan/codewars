# !/usr/bin/python3
# -*- coding:utf-8 -*-

""" 
Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then 
it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef'] 
"""

import re

#常规解法
def solution1(s):
    #也可以选择不判断字符串个数的奇偶，每次循环的时候在后面直接加‘_’，但这样效率不高，不推荐
    # return [(s + "_")[i:i + 2] for i in range(0, len(s), 2)]
    s = s if len(s)%2==0 else s+'_'
    return [s[x:x+2] for x in range(0,len(s),2) ]



#利用正则表达式
def solution2(s):
    return re.findall('.{2}',s+'_')


print(solution1('abc'))
print(solution1('abcdef'))

print(solution2('abc'))
print(solution2('abcdef'))
