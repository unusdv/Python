login = input("Enter login: ")
pswd = input("Enter password: ")

with open("data.txt", "a") as file:
    file.write(f"login:{login},")
    file.write(f"password:{pswd}\n")

# login:johndoe,password:qwerty
# login:sarah,password:asdfgh

print("Menga %s %2d marta %s dedi." % (c, b, a))
print(f"text {a.^#} {b} text")
