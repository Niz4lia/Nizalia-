a=int(input("Enter the First Number: "))
b=int(input("Enter the Second number: "))
oper=str(input("Enter the operater"))
if oper=='+':
    result =(a+b)
    
elif oper=='-':
    result=(a-b)

elif oper=='*':
    result=(a*b)
    
elif oper=='/':
    result=(a/b)
    
else:
    print("Error")
