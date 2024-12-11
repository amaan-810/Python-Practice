def checkPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

a,b=input("Enter two Numbers : ").split()
a=int(a)
b=int(b)

print("Prime Numbers are : ")

for i in range(a,b+1):
    if checkPrime(i):
        print(i,end=" ")

