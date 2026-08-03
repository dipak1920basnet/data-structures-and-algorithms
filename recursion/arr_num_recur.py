def recur_arr(arr, left, right):
    if left >= right:
        return arr
    # temp_left = arr[left]
    # arr[left] = arr[right]
    # arr[right] = temp_left
    # left += 1
    # right -= 1

    arr[left], arr[right] = arr[right], arr[left]
    return recur_arr(arr, left+1, right-1)

arr = [0,1,2,3,4,5,6,7,8,9]




# reverse an arry using while loop

array = [0,1,2,3,4,5,6,7,8,9]

def while_reverse(arr):
    # totally reverse a array
    left = 0
    right = len(arr) - 1

    while left<=  right:
        arr[left], arr[right] = arr[right], arr[left]
        left +=1
        right -= 1
    return arr



def while_reverse_parameter(arr, left, right):
    while left<=  right:
        arr[left], arr[right] = arr[right], arr[left]
        left +=1
        right -= 1
    return arr

print(recur_arr(array.copy(), 2, 6))
print(while_reverse_parameter(array.copy(), 2, 6))
print(while_reverse(array.copy()))
