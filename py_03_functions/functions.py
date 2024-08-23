# %%
"""
<type> func_name (<int> <var>, ...) {
    return 0
}
"""
# %%

def print_hello ():
    print("Hello")

print("Foundation")

print_hello()

# %% Function arguments
def add15 (a, b):
    print(a * b)


add15(5, 8)
add15(5, "Hello")
add15([1,2,3], [4,5,6])



# %%
def types (a: list, b: int):
    print(a + b)


types(5, 9)
types("Hello", "World")


# %%
def returning_object (a: int, b: int):
    return a + b


print(returning_object(5, 7))
print(type(returning_object(5, 7)))

print(returning_object(5, 7.6))
print(type(returning_object(5, 7.6)))

print(returning_object("H", "i"))
print(type(returning_object("H", "i")))


# %%
def none_type ():
    pass


print(none_type())

# %%
def print_details (model, brand, max_speed):
    print("Model:", model)
    print("Brand:", brand)
    print("Speed:", max_speed)


print_details("Damas", "Chevrolet", 430)
print_details(brand="BMW", max_speed=120, model="M5")


# %%
def get_sum (*vars):
    """Ekranga chop etish"""
    print(vars)


get_sum(1,2,3,4,5,6,7,8,9,0)
get_sum("hello", "World", "Foundation")

# %%
def user_details (**info):
    print(info["name"])


user_details(name="John", age=34)
user_details(name="BMW", age=34.67)

# %%
def auto (model, brand="Chevrolet"):
    print(model, brand)


auto("Q7", "Audi")
auto("Lacetti")

print("Hello", 1,2,3, sep=" = # = ")


# %%

def add15 (a: int) -> int:
    """Bu funksiya istalgan songa 15 qo'shib beradi."""
    return a + 15


print(add15(5))
