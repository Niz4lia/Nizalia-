num1=float(input("Enter the First Number: "))
num2=float(input("Enter the Second number: "))
oper=(input("Enter the operater(+, - , *, /): "))
if oper=='+':
    result =(f'{num1}+{num2} = {num1+num2}')
    print(result)
    
elif oper=='-':
    result=(f'{num1}-{num2} = {num1-num2}')
    print(result)

elif oper=='*':
    result=(f'{num1}*{num2} = {num1*num2}')
    print(result)
    
elif oper=='/':
        while num2==0:
            print('Not possible')
            num2=float(input('Enter a non zero number: '))
        
        result=(f'{num1}/{num2} = {num1/num2}')
        print(result)
    
else:
    print("Error")