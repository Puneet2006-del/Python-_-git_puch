from functools import reduce

l = [ 45,556,47,556,72,56,23,65,779,741,567,8]

def greater(a,b):
    if a>b:
        return a
    return b

print(reduce(greater, l))