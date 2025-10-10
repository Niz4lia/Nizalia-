def add(a,b):
    c=a+b
    print(f"Your answer: ",c)
    return (c)
def multi(a,b):
    c=a*b
    print(f"Your answer: ",c)
    return (c)
def sub(a,b):
    c=a-b
    print(f"Your answer: ",c)
    return (c)

def div(a,b):
    c=a/b
    print(f"Your answer: ",c)
    return (c)

a=int(input("Enter the First Number: "))
b=int(input("Enter the Second number: "))
oper=str(input("Enter the operater"))
if oper=='+':
    result =add(a,b)
    
elif oper=='-':
    result=sub(a,b)

elif oper=='*':
    result=multi(a,b)
    
elif oper=='/':
    result=div(a,b)
    
else:
    print("Error")
