# my approach to solution
def check_palindrome(n):
    def helper(n):
        k = 0
        while n > 0:
            if k == 0:
                k = n % 10
            else:
                k = k * 10 + n % 10
            n = n // 10

        return k
    if helper(n) == n:
        print("palindrome")
    else:
        print("not palidrome")
n = 1234321
check_palindrome(n)