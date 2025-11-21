#creating a function(non-return type)
def fun():
    print('Welcome to QBHS')
#calling function
fun()

#(return type)
def add(num1:int,num2:int):
    num=num1+num2
    return num

num1,num2=5,15
ans=add(num1,num2)
print(f'The addition of {num1} and {num2} results: {ans}')

#evenodd
def evenodd(x):
    if (x%2==0):
        print(f'The entered number {x} is even')
    else:
        print(f'The entered number {x} is odd')
evenodd(8)
#default argument
def myfun(x,y=50):
    print("x=",x)
    print('y=',y)
myfun(10)

#keyword argument
def student(firname,lasname):
    print(firname,lasname)

student(firname='Nizalia',lasname='Fatima')

#positional function
def nameage(name, age):
    print("Hi,I'm",name)
    print("My age is",age)

print('case-I')
nameage('Nizalia',16)

#square function
def square(num):
    return num**2
result=square(5)
print(result)

def multiply(x,y):
    return x*y

def f1():
    x="Hello,World"

    def f2():
        print(x)
    f2()

f1()


#Recursive function
#factorial
def factorial(n):
    if n <0:
        return "error:factorial on negative no."
    elif n==0:
        return 1
    else:
        return n*factorial(n-1)
    
result=factorial(1)
print(result)

#fibonacci series


def fibonacci(n):
    if n <= 0:
        return "Error:cannot be negative"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = fibonacci(n - 1)
        fib.append(fib[-1] + fib[-2])
        return fib

print(fibonacci(10))