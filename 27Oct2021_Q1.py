# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 15:54:28 2021

@author: jyoti
"""

'''
The carshare dilemma:
    Suppose we have selected a group of people to take a survey. 
    35% of the group like Uber, 20% like both Lyft and Uber,
    and 25% like neither Lyft nor Uber. 
    Given this information, what percentage of the sample likes Lyft?
    
    Hint: You can use basic probability theory to solve this problem.
    '''
'''
Solution
    P{Uber} = 0.35
    P{Uber and Lyft} = 0.20
    P{Not uber nor Lyft}= 0.25
    P{uber or Lyft} = 1-0.25 = 0.75
    0.75 = 0.35 + P{Lyft} - 0.20
    P{Lyft} = 0.60
    
    60% people likes Lyft
    '''

def carshare(p_u,p_both,p_none):
    
    return 1-p_none-(p_u - p_both)

    