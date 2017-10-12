#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: commandDemo.py
@time: 17-10-10 下午6:10
"""
import os


def func():
    pass


if __name__ == '__main__':
    ls = 'ls -l \n'
    ls += 'df -h \n'
    print(ls)
    print(os.system(ls))