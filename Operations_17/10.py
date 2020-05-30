""" a fast way to make a shallow copy of a list """
a = [5, 4, 3, 2, 1]
a = a[::-1]
b = a
b[0] = 10
""" both a and b will be [10, 2, 3, 4, 5] """

b = a[:]
b[0] = 10
""" only b will change to [10, 2, 3, 4, 5] """

""" copy list by typecasting method """

a = [1, 2, 3, 4, 5]
print(list(a))

""" using the list.copy() method (python3 only) """
a = [1, 2, 3, 4, 5]

print(a.copy())

""" copy nested lists using copy.deepcopy """
from copy import deepcopy

l = [[1, 2], [3, 4]]
l2 = deepcopy(l)
print(l2)

