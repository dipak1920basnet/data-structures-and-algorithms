def recur_palin(string):
    left = 0
    right = len(string)-1
    # with recursion 
    def recur(string, left, right):
        if left >= right:
            return True
        if string[left] != string[right]:
            return False
        return recur(string, left+1, right-1)
    print(recur(string, left, right))

    # using while_loop 
    def while_loop(string):
        left = 0
        right = len(string) - 1
        while left<= right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        else:
            return True

    print(while_loop(string))

name="Dipak"
# name="mom"
# name = "nitins"
recur_palin(name)