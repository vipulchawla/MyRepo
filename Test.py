#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 15:37:48 2022

@author: vipul.chawla
"""
# test

#print('code for testing yo yo')


def newAllocation(coachAllocation):
    totalpc = 0
    totalgc = 0
    totalman = 0
    numberOfDays = len(coachAllocation)
    print(numberOfDays)
    if numberOfDays > 0:
        try:
            for allocation in coachAllocation:
                totalpc = totalpc + allocation[0]
                totalgc = totalgc + allocation[1]
                totalman = totalman + allocation[2]
            print('Personal Coaching Allocation %: ', totalpc/numberOfDays)
            print('General Coaching Allocation %: ', totalgc/numberOfDays)
            print('Management Allocation %: ', totalman/numberOfDays)
        except:
            print('Invalid argument - Pass the allocation in list format')
    else:
        print('No Allocation Found')
        
        
        
        
