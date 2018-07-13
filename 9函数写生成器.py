#生成器的写法 1.列表生成式  2.函数


def range2(n):
    count=0
    while count<n:
        print(count)
        count+=1
        sign=yield count#变成了生成器
        print('---sign',sign)
        if sign=='stop':
            break
    #return 333

#yield 返回数据并冻结当前执行过程
#启动必须next一下
#yield生成器只要有return会报错
#return在生成器里代表生成器的中止，会报错
n=range2(3)
n1=next(n)
n.send('stop')
#1.唤醒并继续执行
#2.发送一个信息到生成器内部




