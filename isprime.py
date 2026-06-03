def is_prime (num):
    flag=1
    if num>2:
        for i in range(2,num):
            if num%i==0:
                 flag=0
        if(flag):
            print("it is a prime")
        else:
            print("it is not a prime ")
    elif num==2:
        print("it is a prime")
    else:
        raise ValueError

num=int(input("type a number to check if it is prime:"))
is_prime(num)
