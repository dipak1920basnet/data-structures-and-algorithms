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


def approach_two(n):
    t = str(n)
    power = len(t)
    total = 0
    for i in t:
        total += int(i)**power
    if n == total:
        check = True
    else: 
        check = False
    return power, total, check

print(approach_two(153))
print(approach_two(1634))
print(approach_two(169))