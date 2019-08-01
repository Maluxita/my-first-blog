#!/usr/bin/python
# -*- coding: UTF-8 -*-

print ('hello, django girls')

def hi (name):
    print ('hi ' + name + '!')



def main ():
    print ('¿cual es tu nombre')
    name2 = str(input())
    hi(name=name2)

if __name__ == '__main__':
    main()

