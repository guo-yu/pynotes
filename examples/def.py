# -*- coding: UTF-8 –*-
#!/usr/bin/python
# Filename : def.py

# 使用 def 关键词定义一个函数
# 什么是函数？
# 函数是一些代码片段的组合
# 你可以使用你希望使用的名字来定义函数，然后使用这个函数的名字来调用函数
# 我们来试试看将 helloworld 包装在一个函数中进行使用

def helloworld(text="hello world!"):
    print text

# 现在我们有了一个函数，函数有一些参数，参数在（）中声明，在 python 中，你可以用 a=b 的方式来定义参数的默认数值，也可以不定义，像下面这样：

def helloword_without_default_param(text):
    print text

# 如你所见，我可以使用任何我想使用的名字来定义函数，甚至带有下划线的函数名
# 现在我们如何执行他们呢？

helloworld() # => 'hello world!'
helloworld('good night!') # => 'good night!'
helloword_without_default_param(text='hello again!') # => 'hello again!'

# 现在你明白如何定义函数，以及执行函数了，自己写写看。
