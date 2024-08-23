# %%

d = dict()

for i in range(10):
    d.update({f"key{i}": f"value{i}"})

    d[f"key{i}"] = f"value{i}"

print(d)
print(f"Hello {1}")

# %%

s = input()
d = dict()

for i in s:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1

print(d)


# %%
d = dict()
d = {f"key{i}" : f"value{i}" for i in range(10)}

d1 = {value: key for key, value in list(d.items())[::-1]}

# d1 = dict()
# for key, value in d.items():
#     d1[value] = key

print(d)
print(d1)
# %%
