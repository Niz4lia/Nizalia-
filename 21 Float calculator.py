n1=float(input("Enter First Number: "))
n2=float(input("Enter second Number: "))
oper=str(input("Enter the operator: "))
match oper:
    case '+': 
        print(float(n1+n2))
    case '-':
        print(float(n1-n2))
    case '*':
        print(float(n1*n2) ) 
    case '/' :
        print (float(n1/n2))
    case _:
        print("error") 