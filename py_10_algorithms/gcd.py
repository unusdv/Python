def gcd(a,b):
    if b != 0:
        t = a
        a = b
        b = t % b
    return a

if __name__ == "__main__":
    print(gcd(50,20))
    print(gcd(30,10))
    