def approach_one(n):
    def count_num(n):
        count = 0
        while n > 0:
            n = n // 10
            count += 1
        return count

    count = count_num(n)

    def multiply(n):
        numbers = 0
        while n > 0:
            t = n % 10
            numbers += t ** count
            n = n // 10
        return numbers

    result = multiply(n)

    if n == multiply(n):
        check = True
    else:
        check = False
    
    return count, result, check

print(approach_one(153))
print(approach_one(1634))
