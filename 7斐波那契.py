#如果生成器的推算过程比较复杂，还可以用函数来代替
#比如斐波那契数列
#除第一个数个第二个数字以外，任意一个数字都可以由前两个数字相加得到
#1 1 2 3 5 8 13 21 34.......
# def fib(max):
#     n,a,b=0,0,1
#     while n<max:
#         print(b)
#         a,b=b,a+b
#         #上面的代码 相当于
#         #t=a+b
#         #a=b
#         #b=t
#         n=n+1
#     return 'done'
#
# fib(15)
#正常函数

#生成器
#yield
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b#修改了一行代码就变成了生成器
        a,b=b,a+b
        #上面的代码 相当于
        #t=a+b
        #a=b
        #b=t
        n=n+1
    return 'done'

f=fib(15)

for i in f:
    print(i)
#yield把函数的执行过程冻结在这一步
#并把函数的值返回到next
#假设生成器每执行一步就要返回值可以用到yield
