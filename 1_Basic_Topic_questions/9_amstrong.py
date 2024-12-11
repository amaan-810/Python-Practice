
n=input("Enter a number : ")

pw=len(n)
n=int(n)
temp=n
sum=0
while(temp>0):
    ld=temp%10
    sum=sum+(ld**pw)
    temp=temp//10

# print(sum,pw)
if sum== n:
    print("is Armstrong")
else:
    print("not armstrong")