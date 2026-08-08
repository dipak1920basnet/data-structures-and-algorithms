def Merge_Array(left:list, right:list)->list:
    i,j = 0,0
    left_n = len(left)
    right_n = len(right)
    array = []
    while i < left_n and j < right_n:
        if left[i] < right[j]:
            array.append(left[i])
            i += 1
        else:
            array.append(right[j])
            j+=1
    if i< left_n:
        array.extend(left[i:])
    if j < right_n:
        array.extend(right[j:])

    return array

def Merge_sort(n:list)->list:
    if len(n) == 0 or len(n) == 1:
        return n 
    half_point = (len(n)//2)
    left_half = Merge_sort(n[:half_point])
    right_half = Merge_sort(n[half_point:])
    return Merge_Array(left_half, right_half)

n = [3,1,2,4,1,5,2,6,4]
print(Merge_sort(n))