#%% LIST | RO'YHAT | СПИСОК
# Ordered - Tartiblangan
# Mutable - O'zgaruvchan
# Allow duplication

# %% 
a = []
b = list()
print(type(a), type(b))

# %%
# int a[] = {1, 2, 3, 4, 5};
a = [1, 2, 3, "Hello", "h", 56.9]
print(a.__sizeof__())

# %%
lst = [11,22,33,44,55,66,77, 88, 99]

print(lst[2])
print(lst[2:])
print(lst[2:6])
print(lst[2:6:2])
print(lst[-1])

lst[2] = "Salom"
lst[2] = "K" + lst[2][1:]
lst[4:6] = ["Good", "Boy"]
lst[7:11] = [123,234,345,456,567]
print(lst)

# %%
lst = [11, 22, 33]
lst.append("Hello")
lst.insert(2, 9000)
print(lst)

# %%
lst = [11, 22, "Hello", 33, 44, 55]
lst.pop()
lst.pop(1)
lst.remove("Hello")
print(lst)

# %%
lst = [11, 22, "Hello", 33, 44, 55, "Hello"]

print(lst.count("Hello"))
print(lst.index("Hello"))
print(lst.index("Hello", 3))


# %%
a = [11,22,"hello",33,44,55,66,77,88,99,100]

for i in a:
    print(i)

for i in range(len(a)):
    print(a[i])

# %%
