#!/usr/bin/python
# Filename : raw_input.py

def input(q):
  return raw_input(q)

name = input('your name is ?')
age = int(input('your age is ?'))

if age > 18 :
  print 'SO OLD!!!!' ,name
else:
  print 'young boy!!!',name