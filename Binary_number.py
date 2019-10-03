#Given a base-10 integer n , convert it to binary (base-2). 
#Then find and print the base-10 integer denoting the maximum number of consecutive 1s in n's binary representation.

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    reml=[]
    n = int(input())
    while(n>0):
        rem=n%2
        reml.append(rem)
        n=int(n/2)
    nl=len(reml)
    count=1
    c=nl-1
    k=[]
    while(c>0):
        
        if reml[c]==reml[c-1] and reml[c]==1:
            count+=1
        if (reml[c]==1 and reml[c-1]==0) or c==1:
            k.append(count)
            count=1
        c-=1
k.sort()
print(k[-1]) #max no of consecutive 1s
