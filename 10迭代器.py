#可以用制作for 循环的数据类型
#1.集合类型 如list tuple dict set str
#2.一类是生成器和带有yield的生成器函数
#可迭代对象统称为iterable
#可以使用isinstance（）判断一个对象是否为iterable
from collections import Iterable
print(isinstance([],Iterable))


#isinstance
#凡是可以用作for 循环的都是iterable函数

