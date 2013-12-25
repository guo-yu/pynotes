#!/usr/bin/python
# Filename : module_raw_input.py

version = '0.0.1'

def input(q):
  return raw_input(q)

name = input('your name is ?')
age = int(input('your age is ?'))

if age > 18 :
  print 'SO OLD!!!!' ,name
else:
  print 'young boy!!!',name