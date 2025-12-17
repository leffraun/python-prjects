#calculator
# given n as number1 and m as number 2 and op is operator . n1 and m1 are n and m's string version
try:
    n1,op,m1=input("enter your number, operator and number to operate it with\"eg: 5+3\":\n").split()
except ValueError:
 print("you gave the wrong type.")


n=int(n1)
m=int(m1)
#print(n,op,m)
result=0
if(op=="/"):
    result=n/m
elif (op=="+"):
    result=n+m
elif (op=="-"):
    result=n-m
elif (op=="*"):
    result=n*m
else:
    print("wut the heck..")
r=round(result)
print(f"{n} {op} {m} = {r}")
