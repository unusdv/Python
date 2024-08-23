from os import system
# system("clear") # cls

# list  - Ordered   | Mutable   | Allow duplicates
# tuple - Ordered   | Immutable | Allow duplicates
# set   - Unordered | Immutable | Doesn't allow duplicates
# dict  - Unordered | Mutable   | Doesn't allow duplicates*

# d = {
# #   KEY : VALUE
#     "model": "Damas",
#     "horse_power": 450,
#     "max_speed": 260,
#     "color": ["Red", "Yellow"]
# }

# d["max_speed"] = 300
# d["engine"] = "V12"

# print(d["model"])
# print(d["max_speed"])
# print(d["color"])
# print(d["engine"])

# user = {
#     "login": "johndoe",
#     "pswd": "qwerty"
# }

# user1 = {
#     "login": "qwerty",
#     "pswd": "asdfgh"
# }

# lst = [user, user1]

# for i in range(2):
#     lg = input()
#     ps = input()
#     u = {
#         "login": lg,
#         "pswd": ps
#     }
#     lst.append(u)


student = {
    "name": "Sam",
    "age": 18,
    "university": "MIT"
}

# for i in student.items():
#     print(i)

print(student.items())
print(student.keys())
print(student.values())

student.update({"grade": 2})
print(student)