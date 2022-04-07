#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 21:48:12 2022

@author: vipul.chawla
"""

def find_string(s):
    newstr = ''
    for i in s:
        if s.count(i) == 1 and i != " ":
            newstr = newstr + i
    return newstr

print(find_string('something else'))


def find_dupe(s):
    dup_list = []
    for i in s:
        if s.count(i) > 1 and i != '' and i not in dup_list:
            dup_list.append(i)
    return dup_list

print(find_dupe('something else'))

def find_first_dupe(s):
    result = ''
    for i in s:
        if i in result:
            break
        result = result+i
    return i
        
print(find_first_dupe('something else'))


def power(x,y):
    if x == 0:
        return 0
    result = 1
    temp = 0
    if y < 0:
        temp = y * -1
    else:
        temp = y
    for i in range(temp):
        result = result * x
    if y < 0:
        return 1/result
    else:
        return result

print(power(0,5))
print(power(2,-5))


# reverse string
def rev_str(s):
    print(s)
    n = len(s)
#   print(n)
    res=''
#    return s[::-1]
    for i in range(n):
        res = res+s[n-1-i]
    return res
    
print(rev_str('Hello World'))
    