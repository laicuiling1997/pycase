#global 关键字使用


def global_test():
    count = 10
    return count

print(global_test())  #10


def global_test():
    global count #使用global关键字后，相当于直接在全局定义了一个count变量
    count = 10
    return count

print(global_test())  #10
print(count) #10
