def functhree():
    print('Three')


def functwo():
    functhree()
    print('Two')


def funcone():
    functwo()
    print('one')
    

# funcone()

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(4))