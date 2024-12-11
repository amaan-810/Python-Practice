a,b=input("Enter two numbers : ").split()
a=int(a)
b=int(b)
op_code=input("Enter a valid opcode : ")

print("Result : ")

if(op_code == "+"):
    print(a+b)
elif (op_code == "-"):
    print(a-b)
elif(op_code == "*"):
    print(a*b)
elif(op_code == "/"):
    print(a/b)
else : 
    print("Enter a valid op_code!")