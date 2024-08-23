from os import system
# system("clear") # cls

# list  - Ordered   | Mutable   | Allow duplicates
# tuple - Ordered   | Immutable | Allow duplicates
# set   - Unordered | Immutable | Doesn't allow duplicates
# dict


# s = {}
# d = set()
# a = {"Apple", "Google", "Meta", "Microsoft", "Meta", "Amazon"}
# print(len(a))

# a1 = {11,22,33,44,55}
# a2 = {33,44,55,66,77}

# print(a1.difference(a2))    # Farq
# print(a1.union(a2))         # Yig'indi
# print(a1.intersection(a2))  # Umumiy qism

# for i in a1:
#     print(i)

# a1.add(1234)
# print(a1)

a = [1,2,3,4,5,6,3,4,3,2,3,4,3,2,1,3,4,5]
a = list(set(a))

print(a)
