# reverse an array 
# pythonic 
def reverse(arr):
    return arr[::-1]

array = [1,2,3,4,5]
print(reverse(array))

# for loop 

def reverse_for(arr):
    reversed_arr = []
    for i in range(len(arr)-1,-1,-1):
        reversed_arr.append(arr[i])
    return reversed_arr

print(reverse_for(array))

# a direct method pythonic
def direct(arr):
    # return list(reversed(arr))
    arr.reverse()
    return arr 

print(direct(array))



new_array = [1,2,3,4,5]
# Reverse an array using recursion 
def recur_arr(arr):
    if len(arr)==1:
        return arr
    # print(arr)
    return [arr[-1]]+recur_arr(arr[:-1])

print(recur_arr(new_array))