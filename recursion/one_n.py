# print 1 to n using recursion 

def recur(i,n):
    if i > n:
        return
    print(i)
    recur(i+1,n)

recur(1,5)

print()
print()

#print 1 to n using single parameter 
def n_(n):
    if n == 0:
        return 
    n_(n-1)
    print(n)

n_(5)