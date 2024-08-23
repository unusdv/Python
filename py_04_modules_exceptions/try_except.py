# %% Syntax Error
# a = 5 
# b = 10

# if a > b
#     print(a)

# %% Semantic Error
# def factorial (a):
#     f = 0
#     for i in range(1, a):
#         f *= i
    
#     return f


# print(factorial(5))

# # QA | Quality Assurance
# def factorial_test ():
#     a = factorial(5)
#     if a == 120:
#         print("PASSED")
#     else:
#         print("factorial() ERROR: Expected 120, got", a)

# factorial_test()


# %% Exceptions
# while True:
#     try:
#         a = int(input("a = "))
#         b = int(input("b = "))

#         print(a + b)
#         print(a - b)
#         print(a * b)
#         print(a / b)

#         break

#     except:
#         print("Oka, Son kiritinde!")


# %%
# while True:
#     try:
#         a = int(input("a = "))
#         b = int(input("b = "))

#         print(a + b)
#         print(a - b)
#         print(a * b)
#         print(a / b)

#         break

#     except ValueError:
#         print("Oka, Son kiritinde!")

#     except ZeroDivisionError:
#         print("Eeeee, matematikani bismasmidiz, oka? 0 ga bo'lish mumkunmas")

#     except KeyboardInterrupt:
#         print("Endi oka, erkalanvordiz!")
    
#     finally:
#         print("Ishlar tugadi")


# %% Custom Exceptions
class LoginError (Exception):
    pass


while True:
    try:
        login = input("Enter login: ")

        if len(login) < 6:
            raise LoginError
        
        if login == "userlogin":
            print("Entered")
            break
        else:
            print("Incorrect")

    except ValueError:
        print("HH")

    except LoginError:
        print("Login should be at least 6 characters")


# %%

def get_list(lst1, lst2, lst3):
    d = {
        lst1[0]: {lst2[0]: lst3[0]},
        lst1[1]: {lst2[1]: lst3[1]}
    }

    print(d)


# get_list(5)
# get_list([1,2,3,4,5,6,7])
# get_list("Hello")
d = [1,2]
f = [3,4]
g = [5,6]
get_list(d, f, g)


def getL(*g):
    print(g)


getL(1,2,3,4,5,6)


# %%
def str_splitter(s):
    print(s)
    print(s.split())
    print(s.split("."))


str_splitter("Salom Yoz. Olam juda ham go'zal. Imtihon bo'lyapti.")


# %%
