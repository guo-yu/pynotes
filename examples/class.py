#!/usr/bin/python
# Filename : class.py

class Article:
    def read(self):
        title = 'watch this title'
        author = 'me'
        content = 'this is a kind of novel'
        print self.name, 'is' , author
    def __init__(self,name):
        self.name = name

newpost = Article(name='turing')
newpost.read()