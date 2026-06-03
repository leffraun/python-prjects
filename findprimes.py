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
num=int(input("enter the N:"))
print("the numbers from 2 to",num," are:",collect_primes(num))
