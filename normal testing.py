def start():
    print("Hello")
    second()
def second():
    i = input(": ")
    if i == "1":
        return second()
    else:
        return
    print("Hello")
start()