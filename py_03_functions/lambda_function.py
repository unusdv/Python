# %%
def f (a, b):
    return lambda a, b: a + b

# def g (a, b, c):
#     g(a,b,c)
g = f(5, 6)
print(g(5, 6))

# %%
# Lambda
# Arrow function
# Anonimous function
z = lambda x, y: x * y

print(z(5, 6))


# %%
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

print(myfunc)
print(mydoubler)


# %%
def a():
    def g():
        print("Hey")
    g()
    

a()
# %%
