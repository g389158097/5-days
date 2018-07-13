#装饰器
user_status = False

# #认证程序在此
# def login():
#     _username = 'cbc'
#     _password = 'goudan'
#     global user_status
#     if user_status==False:
#         user=input('user:')
#         word=input('password:')
#         if user==_username and word==_password:
#             print('验证通过')
#             user_status=True
#         else:
#             print('输入错误')
#     else:
#         print('欢迎登陆会员')



#版块


# def home():
#     print('------shouye----')
# def cc():
#     print('cc')
# def bb():
#     print('bb')
# def cc2():
#     print('cc2')

#假设bb与cc 要收费
#那么就需要用户认证
#此时认证的程序就可以单独写出来

#此时需要验证的在前面加入验证程序
#@login3(cc)
# def home():
#     print('------shouye----')
# def cc():
#     print('cc')
# def bb():
#     print('bb')
# def cc2():
#     print('cc2')

#但是这段验证程序违反了开放-封闭原则：不允许被修改，但是可以被拓展
#简单来说，要对原代码进行修改
#如何在不改变原有编码的情况下加上认证功能呢？
#高阶函数：把一个函数当成返回值或者返回
#所以，每次在一个板块需要认证的时候，将整个板块的函数作为一个参数传入认证模块内




# #修改后的代码
# def login2(func):
#     _username = 'cbc'
#     _password = 'goudan'
#     global user_status
#     if user_status==False:
#         user=input('user:')
#         word=input('password:')
#         if user==_username and word==_password:
#             print('验证通过')
#             user_status=True
#             func()#验证成功后在调用
#         else:
#             print('输入错误')
#     else:
#         print('欢迎登陆会员')
#         func()#验证成功后在调用
#没有改板块的源代码
#符合开放-封闭原则


# login2(bb)
#但是此时每登陆一个版块就要调用一次，改变了调用方式
#还是很麻烦

#匿名函数 不需要写名字
#匿名函数也可以有名字

#直接修改函数名
# bb=login2(bb)
# cc=login2(cc)
#此时又出现了一个问题 调用顺序的问题
#但是在上面修改函数名的过程中，就已经调用了一次函数，所以要让它在你想执行的时候在执行
#
# def login3(func):
#     def inner():#闭包
#         _username = 'cbc'
#         _password = 'goudan'
#         global user_status
#         if user_status==False:
#             user=input('user:')
#             word=input('password:')
#             if user==_username and word==_password:
#                 print('验证通过')
#                 user_status=True
#                 func()#验证成功后在调用
#             else:
#                 print('输入错误')
#         else:
#             print('欢迎登陆会员')
#             func()#验证成功后在调用
#     return inner#不加括号



# cc=login3(cc)
# print(cc)
# cc()

#最后就多了一行代码   cc=login3(cc)
#这就叫做装饰器
#符合开放封闭原则的情况下，给代码加新功能

#更简单的写法@login



# @login3
# def home():
#     print('------shouye----')
# @login3
# def cc():
#     print('cc')
# def bb():
#     print('bb')
# def cc2():
#     print('cc2')
#
#
# cc('33')#cc带参数的话就会报错
#*args **kwargs  非固定参数
#
def login3(func):
    def inner(*args,**kwargs):#闭包
        _username = 'cbc'
        _password = 'goudan'
        global user_status
        if user_status==False:
            user=input('user:')
            word=input('password:')
            if user==_username and word==_password:
                print('验证通过')
                user_status=True
                func(*args,**kwargs)#验证成功后在调用
            else:
                print('输入错误')
        else:
            print('欢迎登陆会员')
            func(*args,**kwargs)#验证成功后在调用
    return inner#不加括号
@login3
def home():
    print('------shouye----')
@login3
def cc(style):
    print('cc',style)
def bb():
    print('bb')
def cc2():
    print('cc2')

cc('33')



#此时又出现了问题，假设传入参数的时候还要加入一个参数
#login若要继续添加函数就可以继续闭包
