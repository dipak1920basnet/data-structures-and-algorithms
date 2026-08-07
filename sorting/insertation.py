def Insertation(n):
    m = len(n)
    if m == 0 or m== 1:
        # return n 
        print(n)
        return
    for i in range(1, m):
        if n[i] < n[i-1]:
            temp = n[i]
            n[i] = n[i-1]
            for j in range(0,i):
                if temp < n[j]:
                    n[j], temp = temp, n[j]             
    print(n)

n =  [5,8,1,6,9,2,4]

# new_n = [34, 12, 78, 56, 23, 89, 1, 45, 67, 10, 99, 2, 31, 54, 76, 8, 14, 90, 5, 38]
# Insertation(new_n)
# print(new_n==[1, 2, 5, 8, 10, 12, 14, 23, 31, 34, 38, 45, 54, 56, 67, 76, 78, 89, 90, 99])

# # Empty list
# Insertation([])

# # Single element
# Insertation([5])

# # Already sorted
# Insertation([1, 2, 3, 4, 5])
            


def insertation_sort(n):
    for i in range(1,len(n)):
        if n[i] < n[i-1]:
            temp = n[i]
            n[i] = n[i-1]
            for j in range(i-1, -1,-1):
                if j == 0:
                    n[j] = temp
                    break
                elif n[j-1] > temp:
                    n[j] = n[j-1]
                else:
                    n[j] = temp
                    break

    print(n)

insertation_sort([1, 2, 3, 4, 5])
insertation_sort([5])
insertation_sort([])
insertation_sort([34, 12, 78, 56, 23, 89, 1, 45, 67, 10, 99, 2, 31, 54, 76, 8, 14, 90, 5, 38])

