#creating a function
def add(a,b):
    c=a+b
    print(f"Your answer: ",c)
    return (c)
#recalling the function
num1=int(input("Enter the First Number: "))
num2=int(input("Enter the Second number: "))
add(num1,num2)