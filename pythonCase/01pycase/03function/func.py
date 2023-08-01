#函数
    #1.形参和实参
    #2.关键字参数
    #3.默认参数
    #4.收集参数：*params




# 1.形参和实参
# def firstTest(name):
#     '函数定义过程中的name叫形参'
#     print(name + ',very happy!')

# firstTest('Jennifer') #Jennifer,very happy!

# print(firstTest.__doc__) #函数定义过程中的name叫形参




#嵌套函数
# def func1():
#     print('func1正在被调用中。。。')
#     def func2():
#         print('func2正在被调用中。。。')
#     func2()

# func1()


#闭包
# def FuncX():
#     x = 5
#     def FuncY():
#         x *= x
#         return x 
#     return FuncY

#创建函数对象
# print(FuncX()())  # UnboundLocalError: cannot access local variable 'x' where it is not associated with a value


# Q: 以上代码为什么会报错呢？
# A: 由于FuncX中的x变量为数字，数字，字符串，元组都是不可变类型，所以不能被FuncY函数所用，
#    解决方法：在FuncY函数中写入 nonlocal x

# A: nonlocal关键字只能用于访问外部/修改函数的变量

#修改后的代码
# def FuncX():
#     x = 5
#     def FuncY():
#         nonlocal x
#         x *= x
#         return x 
#     return FuncY
# print(FuncX()())




# # lambda匿名函数

# # 语法 ：lambda [arg1 [,arg2,.....argn]]:expression

# # filter用法1：
# print(list(filter(lambda x: x % 2,range(10)))) #[1, 3, 5, 7, 9]


# # map用法2
# print(list(map(lambda x: x * 2,range(10)))) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# #用法3
# sum = lambda arg1, arg2: arg1 + arg2
# # 调用sum函数
# print ("相加后的值为 : ", sum( 10, 20 )) #相加后的值为 :  30
# print ("相加后的值为 : ", sum( 20, 20 )) #相加后的值为 :  40





def x(n):
    reslut = n
    for i in range(1,n):
        reslut *= i
    return reslut

number= int(input("请输入一个正整数："))
res = x(number)
print("%d 的乘阶是：%d"%(number,res))


# 递归
# 函数调用自身的技术

def y(n):
    if n==1:
        return 1
    else:
        return n * y(n-1)

number= int(input("请输入一个正整数："))
res = y(number)
print("%d 的乘阶是：%d"%(number,res))






