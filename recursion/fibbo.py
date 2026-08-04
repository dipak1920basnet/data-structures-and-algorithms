def check_fibbo(array):
    def recur_fibo(array, left, right):

        if len(array)<3:
            return False
        
        if right == len(array) -1:
            return True

        if (array[left]+array[right]) != array[right+1]:
            return False

        return recur_fibo(array, left+1, right+1)


    def while_fibbo(array):

        if len(array)<3:
            return False

        left = 0
        right = left + 1

        while right < len(array) - 1:
            if (array[left]+array[right]) != array[right+1]:
                return False
            left += 1
            right += 1
        else:
            return True
        
    print(recur_fibo(array,0,1))
    print(while_fibbo(array))

array = [1,2,3,5,8]
check_fibbo(array)