# ! /usr/bin/python3
# -*- coding:utf-8 -*-
'''
Your job is to create a calculator which evaluates expressions in Reverse Polish notation.

For example expression 5 1 2 + 4 * + 3 - (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation) should evaluate to 14.

For your convenience, the input is formatted such that a space is provided between every token.

Empty expression should evaluate to 0.

Valid operations are +, -, *, /.

You may assume that there won't be exceptional situations (like stack underflow or division by zero).
'''

def calc(expr):

    l = expr.split()

    while len(l)>1:
        polish = []
        for i in range(0,len(l)):
            if l[i] in '+-*/':
                s = str(int(eval(l[i-2]+l[i]+l[i-1])))
                polish.pop()
                polish.pop()
                polish.append(s)
                polish.extend(l[i+1:])
                break
            else:
                polish.append(l[i])
        
        l = polish
    else:
        c = l[0] if len(l) else '0'
    
    return int(c) if isinstance(eval(c),int) else float(c)

# print(calc("5 1 2 + 4 * + 3 -"))
# print(calc("4 2 /"))
print(calc(""))