# using for loop 

def for_loop(n):
    factorial = 1
    for i in range(1,n+1):
        factorial *= i

    return factorial
print(for_loop(5))


# factorial using functional recursion 

def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

print(factorial(5))


# factorial with paremeter recursion
def para_factorial(n, total = 1):
    if n == 0:
        print(total)
        return 
    para_factorial(n-1, total*n)
para_factorial(5)