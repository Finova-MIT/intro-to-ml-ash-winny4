a=int(input("Enter an integer:"))
def prime(x):
 p=1
 for i in range(2,(x//2)+1):
    if(x%i==0):
        p=0
        break
 if(p==1):
    print("It is a prime number")
 else:
    print("It is not a prime number")
prime(a)