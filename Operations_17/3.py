""" most frequent element in a list """

a = [1, 2, 3, 1, 2, 3, 2, 2, 4, 5, 1]
print(max(set(a),key = a.count))

""" using Counter from collections """

from collections import Counter

cnt = Counter(a)
print(cnt.most_common(3))