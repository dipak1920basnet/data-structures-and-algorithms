def Quick(n:list)->list:
    if len(n) == 0 or len(n) == 1:
        return n 

    pivot_index = 0
    pivot = n[pivot_index]

    for i in range(pivot_index+1,len(n)):
        if n[i] < pivot:
            for j in range(i,pivot_index,-1):
                n[j], n[j-1] = n[j-1],n[j]
            pivot_index += 1

    left = Quick(n[:pivot_index+1])
    right = Quick(n[pivot_index+1:])

    return left + right


num = [4,1,7,6,3,2,8]

num = [5,7,8,4,1,6,8,2]

num = [3,1,2,4,1,5,2,6,4]

num = [2,1]

print(Quick(num))
