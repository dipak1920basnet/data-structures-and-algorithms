count = 0
def head_func():
    global count
    if count == 4:
        return
    print("Head recursion")
    count += 1
    head_func()
head_func()
print()


new_count = 0

def tail_func():
    global new_count
    if new_count == 4:
        return
    new_count += 1
    tail_func()
    print("Tail recursion")

tail_func()