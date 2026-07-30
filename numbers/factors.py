def brute_force(n):
    factorial_list = []
    for i in range(1,n+1):
        if n % i == 0:
            factorial_list.append(i)
    return factorial_list

n = 10
print(brute_force(n))