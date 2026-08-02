# print by recursion n times 
# stop the recursion by parameter
def recursion(Value,n):
    if n == 0:
        return
    recursion(Value, n-1)
    print(f"n: {n}:",Value)
    
    
recursion(15,4)