
# O(n) it loops for n times for n items in input
def print_items(n):
    for i in range(n):
        print(i)
# print_items(10)


# O(2n) drop constants any operations with n+n loops it will be of order o(n) not o(n+n)=o(2n) it will be o(n)
def print_items2n(n):
    for i in range(n):
        print(i)
    for i in range(n):
        print(i)
# print_items2n(10)


# O(n**2) 
def print_itemsnsquare(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
# print_itemsnsquare(10)


# drop non-dominants 
# O(n**2+n) is equal to o(n**2) because when we increase the size of the input the square term will 
# be more dominant  when compared to n
def print_items_non_dominants(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

    for k in range(n):
        print(k)
# print_items_non_dominants(10)


# O(1) this is a constant operation, number of operations is independent of input size
def add_num(n):
    return n+n+n
# print(add_num(2))


# O(logn) this order will be occuring for sorting algos

# diffferent terms as input for a functions for this function order will be O(a+b)
def print_itemsaaddb(a,b):
    for i in range(a):
        print(i)
    for i in range(b):
        print(i)

# diffferent terms as input for a functions for this function order will be O(a*b)
def print_itemsamulb(a,b):
    for i in range(a):
        for j in range(b):
            print(i,j)
 