# -*- coding: UTF-8 –*-
#!/usr/bin/python
# Filename : if_else.py

# 使用 if else 语句书写判断逻辑
# 代码逻辑中，判断语句几乎无处不在
# 判断逻辑区分着不同的代码快，根据判断条件的真假，来判断执行哪一处代码块
# 特殊地来说，判断语句也可以用在一行中，比如三元运算符（python中没有三元运算符）

a = 13

if a == 12:
    print 'a = 12 is true'
else:
    print 'a != 12 !'

# 我们尝试做了一个简单的判断，根据 a 是否等于 12，程序执行了不同的代码块。

# 如果我们只执行简单的代码判断，比如根据 a 是否等于 12 的真假来对另外一个变量进行赋值，可以写在一行中：

b = 'a is equal to 12' if a == 12 else 'a is NOT equal to 12, a is ' + a

# 试着自己写写看吧
