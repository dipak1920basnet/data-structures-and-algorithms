# my approach to solution
def check_palindrome(n):
    def helper(n):
        k = 0
        while n > 0:
            t = n % 10
            if k == 0:
                k = t
            else:
                k = k * 10 + t
            n = n // 10

        return k
    if helper(n) == n:
        print("palindrome")
    else:
        print("not palidrome")
n = 123432
check_palindrome(n)