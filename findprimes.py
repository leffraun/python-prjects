"""
to find number of primes between 2 and num (inputter number)
"""
import math

def collect_primes(num):
    primes=[]
    for i in range(2, num+1):
        flag=True
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                flag=False
                break
        if flag:
            primes.append(i)

    return primes
try:
    num=int(input("enter the N:"))
    if num>1:
        primes=collect_primes(num)
        if primes:
            print("the numbers from 2 to",num," are:",collect_primes(num))
        else:
            print("no primes found")
    else:
        print("only positive numbers from two allowed")
except ValueError:
    print("positive")
