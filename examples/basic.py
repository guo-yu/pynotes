# -*- coding: UTF-8 –*-
#!/usr/bin/python
# Filename : basic.py

# 声明变量 apple ，并赋值一个字符串给它
apple = 'im a apple'

# 打印出来看看
print apple # => 'im a apple'

# 修改变量的内容
apple = 'im a banana'

# 再打印出来看看
print apple

# 进行逻辑判断
if apple == 'im a apple':
    print 'yep! it\'s a apple !'
else:
    print 'Nop! it\'s NOT a f***ing apple!'

# 声明一个变量，赋值一个数字给它
apple_number = 10

# 打印出来看看
# 注意：不同的变量类型（这里是字符串 + 数字 + 字符串）相连接时，
# 在 python 中，需要转换成同一个类型。
print 'I have ' + str(apple_number) + ' apples, wow!'

# 修改一个数字变量
# 熟悉这几种不同的运算符号组合
# abc += 3 相当于 abc = abc + 3
apple_number = apple_number + 1 #=> 11
apple_number += 1 # => 12
apple_number += 3 # => 15

# 再打印出来看看
# 这回我们使用 helloworld.py 里提到的标准输出方法打印
# 与那个例子不同的是，这里 %d 标识输出数字，而非 %s 输出字符串
print 'I have %d apples, wow !!' % apple_number

# 让我们大胆一点，看看其他的变量类型
# 声明一个数组
apples = [10,12,13,20,30]

# 打印出来看看 
print apples # => [10,12,13,20,30]

# 数组有什么用？
# 数组标识一个一维度序列
# 我们可以访问到数组中元素，使用他们的下标访问，下标从0开始计算
print apples[0] # => 10
print apples[3] # => 20
print len(apples) # 打印数组的长度 => 5

# 让我们更大胆一点，迎接新世界
# 声明一个 apples_factory 变量，并赋值给他一个对象（字典）
# 什么是对象（字典）？
# 对象有一个键(key)，一个值(value)，值可以是一个字符串，一个数字，一个列表（数组），甚至另一个对象。
apples_factory = {
    'name': 'apples factory',
    'store': apple_number,
    'list': apples,
    'worker': [
        {
            "name": "john",
            "age": 20
        },
        {
            "name": "steve",
            "age": 22
        }
    ]
}

# 打印这个对象出来
print apples_factory

# 访问这个对象中的属性
print apples_factory['name'] # => 'apples factory'
print apples_factory['store'] # => 15
print apples_factory['list'][0] # => 10
print apples_factory['worker'][0]['name'] # => john
