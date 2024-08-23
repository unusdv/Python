from os import system
system("clear") # cls

# list  - Ordered   | Mutable   | Allow duplicates
# tuple - Ordered   | Immutabe  | Allow duplicates
# set   - Unordered | Immutable | Doesn't allow duplicates
# dict


# lst = [11,22,33,11,22,33]
# print(lst)

# lst[2] = "Hello"
# print(lst)

# TUPLE
# tpl = tuple()
# print(type(tpl))

# t = (1,2,3,4,5,1,2,3,4,5)

# print(t)

# # t[2] = 9000 # TypeError: 'tuple' object does not support item assignment
# print(t[3])
# print(t[3:])
# print(t[3:6])
# print(t.count(5))
# print(t.index(5))


# y = 11, 22, 33, 44, 55
# print(type(y), y)
# y = list(y)
# y[2] = 9000
# y = tuple(y)
# print(y)

t = (1,2,3,4,5,6,7,8,9)
# Unpacking
a, b, *c, d, e = t

user = (123, "johndoe", "passsword123", "Male", 34)

id, *credentials, gender, age = user

print(id)
print(credentials)
print(gender)
print(age)

b = id, gender, age, credentials
print(b)