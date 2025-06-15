#!/bin/python3

import math
import os
import random
import re
import sys


def multiples_3(n):
    a = 3 
    n_total = (n-1)//a 
    l = a * n_total
    sum_3 = int((n_total/2)*(a + l))
    return sum_3
    
    
def multiples_5(n):
    a = 5
    n_total = (n-1)//a 
    l = a * n_total
    sum_5 = int((n_total/2)*(a + l))
    return sum_5
        
def multiples_15(n):
    a = 15
    n_total = n//a 
    l = a * n_total
    sum_15 = int((n_total/2)*(a + l))
    return sum_15

def sum_all(sum_3, sum_5, sum_15): 
    total_sum = sum_3 + sum_5 - sum_15
    return total_sum
    
        
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        sum_3 = multiples_3(n)
        sum_5 = multiples_5(n)
        sum_15 = multiples_15(n)
    
        print(sum_all(sum_3, sum_5, sum_15))
    
