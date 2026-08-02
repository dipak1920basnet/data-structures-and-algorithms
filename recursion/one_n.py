# print 1 to n using recursion 

def recur(i,n):
    if i > n:
        return
    print(i)
    recur(i+1,n)

recur(1,5)