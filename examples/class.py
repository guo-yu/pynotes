# -*- coding: UTF-8 –*-
#!/usr/bin/python
# Filename : class.py

# 使用 class 关键词定义一个类
# 什么是类？
# 可以这样理解，class 罗列了一些属性和函数，这些属性和函数可以非常方便的创建一个自己的复制品
# 类的复制品叫做实例 （instance）
# 比如，person 是一个类，手，脚，其他器官是人的属性，学习，思考是人的方法。
# john 是 person 的一个实例。
# john 有所有 person 的属性和方法，意味着 john 有健全的器官，能学习也能正常思考。
# 以类为基础，对象作为类的实例，通常称为面向对象的编程（Object-oriented programming）

# 我们来试试创建一个类
# 类的名字可以随便起，但一些编程规范试图约束程序员用首字母大写的方式定义类的名字，以区分普通函数

# 我们定义一个 Article 类，很明显，这个类用以代表文章

class Article:
    
    # 我们在这个 class 中定义了一个方法，
    # 这个方法要做的事情是将 实例 本身的属性打印出来
    # 所有在类中定义的方法，都会被实例所继承
    def read(self):
        print '\n'
        print 'Title: \n %s \n' % self.title # \n 是换行符
        print 'Content: \n %s' % self.content
        print '\n'

    # 每一个定义类的过程中都会执行这个 「初始化」方法
    # 这个方法会在生成实例的过程中自动执行
    def __init__(self, title, content):

        # self 指代这个实例本身
        self.title = title
        self.content = content

# 现在我们来生成一个实例吧
# 我们把这个实例叫做 「我的第一篇文章」

my_first_blog = Article(
    title='我的第一篇文章',
    content='在这里写下你想说的话...'
)

# 我们试试打印这篇文章出来看看
my_first_blog.read()
