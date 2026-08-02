count = 0
def func():
    global count
    if count == 4:
        return
    print("Hello world")
    count += 1
    func()
func()
print(count)