a=[0,1,2,3,4,5,6,7,8,9]
#给列表里的每个数字加一

# a=map(lambda x:x+1,a)
# for i in a:
#     print(i)

a=[i+1 for i in range(10)]#列表生成式
print(a)
#也可以结合三元运算值
