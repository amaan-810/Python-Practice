def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)

a=15
b=20
print("gcd : ",gcd(a,b))