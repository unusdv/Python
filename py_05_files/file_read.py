f = open("1.txt", "r")

# txt = f.read(12)
# print(txt)
# txt = f.readline()
# print(txt)
# txt = f.readline()
# print(txt)

txt = f.readlines()
print(txt)

f.close()
