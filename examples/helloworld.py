# -*- coding: UTF-8 –*-
#!/usr/bin/python
# Filename : helloworld.py

# 声明一个 hellotext 变量，并赋值一个字符串给它，备用
hellotext = 'world again and again !'

# 简单打印 helloworld 
print 'hello world!' # => 'hello world'

# 使用 printf 进行标准化输出
# 使用方法：
# 字符串中的 %s 标识了一个 placeholder（占位符）
# 在字符串结束后 以 % 分割，%之后的代表占位符的内容，以此替代占位符，占位符内容可以是变量或者常量
# 多个占位内容，以 , 分割，被 () 包围
print 'hello %s' % 'world again !' # => 'hello world again'
print 'hello %s' % hellotext # => 'hello world again and again'
print 'hello %s %s' % ('world',' again and again and again !') # => 'hello world again and again and again'