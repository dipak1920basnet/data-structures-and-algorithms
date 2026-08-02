# print by recursion n times 
# stop the recursion by parameter
def recursion(Value,n):
    if n == 0:
        return
    print(Value)

    recursion(Value, n-1)

recursion(15,4)