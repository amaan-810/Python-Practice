n=5

num1=0
num2=1
temp=0
print(num1,end=", ")
print(num2,end=", ")
for i in range(2,n):
    print(num1+num2,end=", ")
    num1,num2=num2,num1+num2


