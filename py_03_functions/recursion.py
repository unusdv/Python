# %%

def print_hello ():
    print("hello")
    print_hello()


print_hello()

# %%
def print_hello (a):
    if a == 10: return

    print("hello", a)
    print_hello(a + 1)
    print("hello", a)


print_hello(0)

# %%
def return_rec (a):
    if a == 10: return a
    return a + return_rec(a + 1)


print(return_rec(0))

# %%
