# without recursion 
def sums(n):
    total = 0
    for i in range(n+1):
        total += i
    # return total
    print(total)

# print(sums(3))

sums(3)


# print sum of natural number with recursion

def recur_sum(n,total=0):
    if n == 0:
        # print(total)
        return total
    return (total,recur_sum(n-1, total+n))
    

print(recur_sum(5))


# alternate method 

def new_recur_sum(n):
    if n == 0:
        return n
    return n + new_recur_sum(n-1)

print(new_recur_sum(5))