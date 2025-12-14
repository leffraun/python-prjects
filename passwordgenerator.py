import random
attempts=0
def makepassword(attempts):
    passwordlength=random.randint(12,18)

    chc=["!","@","#","$","%"]
    a=random.randint(97,122)
    A=random.randint(65,90)
    password=''
    for i in range(passwordlength):
        choice=random.randint(0,2)
        if(choice==0) :
            password+=random.choice(chc)
            #print(random.choice(chc),end='')
        elif(choice==1):
            password+=random.choice(chr(a))
            #print(chr(a),end='')
        elif(choice==2):
            password+=random.choice(chr(A))
            #print(chr(A),end='')
    lowercase=any( c.islower() for c in password)
    uppercase=any(c.isupper() for c in password)
    specialcase=any(c in chc for c in password)
    if lowercase and uppercase and specialcase:
        return password
    else:
        attempts+=1


password=makepassword(attempts)
print("password generated",password)
print("number of attempts:",attempts) #attempts= number of tries used to create the password to ensure it follows the rules







