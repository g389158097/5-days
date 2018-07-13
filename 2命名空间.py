#name space  存放变量名字的地方
#共有三种：locals 函数内的名称空间 保函局部变量与形参
#globals：全局变量，函数定义所在模块的名字空间
#builtins 内置模块的名字空间
# x=1
# print(globals())
#不同变量的作用域就是由于变量所在的命名空间决定的
#有了命名空间才有了作用域
n=10
def func():
    n=20
    print('func',n)
    def func2():
        n=30
        print('func2',n)
        def func3():
            print('func3',n)
        func3()
    func2()


func()
#嵌套函数 会沿用上一层函数的命名空间也就是作用域
#作用域的查找顺序LEGB
#L:LOCAL
#E:enclosing 相邻的上一级就像上面的例子 外部嵌套函数的命名空间
#G：global 全局变量
#B：builtin 内置模块的命名空间

