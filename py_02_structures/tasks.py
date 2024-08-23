# %%
from random import randint as rd

# %% TASK 1.

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic1.update(dic2)
dic1.update(dic3)

print(dic1)


# %% TASK 3.
# INPUT: 5
# OUTPUT: {1: 5, 2: 10, 3:15,.. 10:50}

num = int(input())
d = dict()

for i in range(1, 11):
    d[i] = i * num

print(d)

# %% TASK 4.
# INPUT: 3
# OUTPUT: {23:45, 78:12, 76:46}
count = int(input())
d = dict()
for _ in range(count):
    d[rd(1,100)] = rd(1,100)

print(d)


# %% TASK 5.
# INPUT: 3
# OUTPUT: {23:45, 78:12, 76:46}
# print(student.items())
# print(student.keys())
# print(student.values())

# %% TASK 6.
# INPUT: 3
# OUTPUT: {23:45, 78:12, 76:46}
# -> 12, 78

count = int(input())
d = dict()
for _ in range(count):
    d[rd(1,100)] = rd(1,100)

print(d)
lst = list(d.keys()) + list(d.values())
print(max(lst), min(lst))

# %% TASK 7.
# *
# * *
# * * *
# * * * *
for i in range(10):
    for j in range(i):
        print("* ", end="")
    print()

# %% TASK 8.
lst = []
for i in range(10):
    l = []
    for j in range(i):
        l.append("*")
    lst.append(l)

print(*lst, sep="\n")


# %% TASK 9.
# Original list:
# [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After packing consecutive duplicates of the said list elements into sublists:
# [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]

lst = [rd(0,10) for _ in range(15)]

print(lst)
dct = dict()

for i in lst:
    if i not in dct.keys():
        dct[i] = [i]
    else:
        dct[i].append(i)

print(list(dct.values()))


# %% 
# INPUT: str.
