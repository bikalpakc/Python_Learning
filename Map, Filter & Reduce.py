#MAP

# l1=[1,5,7,3,2]
# l2= list(map(lambda x: x*x, l1))
# print(l2)

#FILTER

# def filterpreset(a):
#     return a>6

# l1=[1,5,7,3,2]
# l2=list(filter(filterpreset, l1))
# print (l2)

#REDUCE
from functools import reduce

def sum(x,y):
    return (x+y)
l1=[1,5,7,3,2]
l2=reduce(sum, l1)
print(l2)