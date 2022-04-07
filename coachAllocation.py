#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 21:03:23 2022

@author: vipul.chawla
"""

from  Test import *


pc = None
gc = None
managing = None
baseAllocation = [50,30,20]
coachAllocation = []
dailyAllocation = 0
tempAllocation = []
i = 1
while True:
    pc = input('enter pc allocation for day ' +str(i) +': ')
    if pc == 'done':
        break
    gc = input('enter gc allocation for day ' +str(i) +': ')
    if gc == 'done':
        break
    managing = input('enter management allocation for day ' +str(i) +': ')
    if managing == 'done':
        break
    try:
        pc = int(pc)
        gc = int(gc)
        managing = int(managing)
    except:
        print('Invalid Input - Enter only numerical numbers')
        continue
    dailyAllocation =  pc + gc + managing
    print(dailyAllocation)
    if dailyAllocation != 100:
        tempAllocation = baseAllocation
    else:
        tempAllocation = [pc,gc,managing]
    i = i + 1
    print(tempAllocation)    
    coachAllocation.append(tempAllocation)
    print(coachAllocation)
    
newAllocation(coachAllocation)