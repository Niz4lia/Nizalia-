def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1 ) 
num = int(input("Enter a number: "))
if num<0:
    print("factorial cannot be found for negative number")
elif num==0:
    print("factorial at 0 is 1") 
else:
    print ("factorial of",num,"is: ",factorial(num))