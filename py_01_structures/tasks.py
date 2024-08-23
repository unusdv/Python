# %% Initiate Random
from random import randint as rd

# %% Task 1. Get 10 elements from user
print([int(input()) for _ in range(10)])

# %% Task 2.

a = [i for i in range(10)]
print(a)

# %% TASK 3.
lst = list()

i = 0
while i < 10:
    lst.insert(0, input())
    i += 1


lst.clear()
for _ in range(10):
    lst.insert(0, input())

# %%


lst = [rd(1,100) for _ in range(30)]

s = 0
for item in lst:
    s += item

print(sum([rd(1,100) for _ in range(30)])/30)

# %% 

lst = [rd(1, 100) for _ in range(30)]
print(lst, min(lst), max(lst))

# %%

lst = [rd(1, 100) for _ in range(30)]
print(lst)

mini = lst.index(min(lst))
maxi = lst.index(max(lst))

lst[mini], lst[maxi] = lst[maxi], lst[mini]
print(lst)

# %%
lst = [rd(1, 10) for _ in range(15)]
print(lst)
lst.sort()
print(lst)

i = 0
while i < len(lst) - 1:
    if lst[i] == lst[i + 1]:
        lst.pop(i+1)
        continue

    i+=1

print(lst)

# %%
lst = [rd(1, 10) for _ in range(15)]
print(lst)

i = 0
while i < len(lst):
    j = i + 1
    while j < len(lst):
        if lst[i] == lst[j]:
            lst.pop(j)
            j -= 1
        j += 1
    
    i += 1

print(lst)

# %%
lst = [rd(1, 10) for _ in range(15)]
print(lst)

cycle = int(input())

while cycle > 0:
    lst.insert(0, lst.pop())
    cycle -= 1

print(lst)
# %%
