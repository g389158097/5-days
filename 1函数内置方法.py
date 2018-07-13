# abs 取绝对值
# dict 把一个数据转换为字典
# help 帮助
# min 在一个列表里取最小的值
a=[1,2,3,4,5]
print(min(a))
#max 取最大的
#all 对一个列表所有元素进行bool  空列表是true
#bool 判断一个值是不是true 0是false 其他数字是true 空列表是false
print(all(a))
a.append(0)
print(all(a))
#any 只要有一个值是true，列表就是true
#dir 打印当前程序中存在的所有变量
#hex十六进制
# slices 定义好切片的规则
#divmod 除数与余数都给出
print(10//3)
print(divmod(10,3))
#sorted 排序 从小到大 reverse 反转排序
#items 将字典变成列表
d={}
for i in range(20):
    d[i]= i-50
d[0]=399
s=sorted(d.items(),key=lambda x:x[1],reverse=True)
print(s)
#ascii 转换ascii码
#enumerate 返回列表的索引
#oct 八进制
#bin 二进制
#eval 把字符串转换成代码运行
eval('print("hello world")')#只能处理单行代码 可以拿到返回值
#exec可以执行多行代码  但是并没有返回值
#sum 求和
#bytearray将字符串修改
#map 方法 列表内的每一个参数都交给map执行一遍
#filter 过滤
v=list(filter(lambda  x:x>3,[1,2,3,4,5]))
print(v)
#reduce 每个元素依次进行运算
#pow 求多少次方
#print sep两者之间的连接
#tuple 变成元组
#callable 看一个对象是否可以调用 函数可以调用 列表不可以
#format 字符串的格式化
#frozenset 将集合变为不可变的
#vars 打印变量名和它的值
#locals 在函数内部运行 打印函数的局部变量
#globals 打印全局变量
#repr 显示形式变为图片
#zip 将两个列表一一对应连接起来
a=[1,2,3,4]
b=[5,6,7,8]
c=list(zip(a,b))
print(c)
#reversed 反转
#complex 变为复数
#round 保留几位小数
#set 将列表变为集合








