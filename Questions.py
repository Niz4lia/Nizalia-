
# #Datatype



# name="Nizalia Fatima"
# age="16"
# fav_prog="Python"
# print(f'My name is{name}. I am {age} years old. My favourite programming language is{fav_prog}')
# a=2
# b=2.5
# c="nice"
# d=["Hi","hello","Bye","Goodbye"]
# e=True
# f={"name":"Nizalia","age":16,"fav_prog":"Python"}
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# b=int(b)
# print(type(b))
# A=30
# B=10
# A=A+B-A
# B=A+A+A
# print(f"A={A}, B={B}")
# greet=input("What is your name? ")
# print(f"Hi,{greet}")

# #Expression and variables
# #Question1
# Width=4
# Lenght=4
# Area=Lenght*Width

# #Question2
# Math=24
# Eng=20
# Phy=19
# Comp=25
# sum=(Math+Eng+Phy+Comp)
# per=sum/100*100
# print(f"{per}%")

# #question3
# celsius=37
# fahrenheit=(celsius*9/5)+32
# print(fahrenheit)

# #Question4
# s=int(input('Enter a number:'))
# sq=s*s
# cu=s*s*s
# print(f'Square={sq}, Cube={cu}')

# #String

# #Question1

# wor= str(input("Enter a word: "))
# vowels = "a,e,i,o,u,A,E,I,O,U"
# consonents = "b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z,B,C,D,F,G,H,J,K,L,M,N,P,Q,R,S,T,V,W,X,Y,Z"
# quan = 0
# con=0
# for letter in wor:
#     if letter in vowels:
#         quan += 1
#         print(letter)
# for letter in wor:
#     if letter in consonents:
#         con += 1
#         print(letter)

# print("Number of vowels:", quan)
# print("Number of consonents:", con)

# #Question2
# sen="Hi I'm Nizalia"
# rev=sen[::-1]
# print(rev)


# #Question3
# wo=str(input("Enter a Word: "))
# reve=wo[::-1]

# if reve==wo:
#     print(f"{wo} is a Pallandrom")
# else:
#     print("This isn't a pallandrom")
# #Question4
# sen=sen.replace(" ","_")
# print(sen)

# #Question5
# tex="Hello everyone, have a good day. Hope you all are doing good."
# #fin=tex.split("good")
# fin=tex.count("good")
# print(fin)

# #Conditions If-Else
# #Question1
# n1=3
# if n1>0:
#     print(f"{n1} is a positive number")
# elif n1<0:
#     print(f"{n1} is a negative number")
# else:
#     print("The number is zero")

# #Question2
# us="Niz4li4"
# pas='5302'
# username=input("Enter your username: ")
# password=input("Enter your password: ")
# if us==username and pas==password:
#     print("You are logged in")
# else:
#     print("Incorrect username or password")

# #Question3
# year=int(input("Enter the year: "))
# if year % 4 == 0:
#     print("It is a Leap year")
# else:
#     print("It is not a Leap year")

# #Question4
# num1=int(input("Enter First Number: "))
# num2=int(input("Enter Second Number: "))
# num3=int(input("Enter Third Number: "))
# max_num = max(num1,num2,num3)
# print(f"The largest number is {max_num}")
# #Question5
# M=20
# E=25
# P=24
# C=23
# total=M+E+P+C

# percentage=total/80*100

# if percentage>=90:
#     print("Grade A")
# elif percentage>=80:
#     print("Grade B")
# elif percentage>=70:
#     print("Grade C")
# elif percentage>=60:
#     print("Grade D")
# else:
#     print("Grade F")

# #Loops
# #Question1
# for i in range(1,11):
#     print(i)

# #Question2
# num=2
# for i in range(1,11):
#     mul=num*i
#     print(f"{num} x {i} = {mul}")

# #Question3
# dig=0
# nu=3322
# sumo=0
# for dig in str(nu):
#     sumo+=int(dig)
# print(f"Sum of digits is {sumo}")
# #Question4
# for i in range(1,51):
#     if i%2==0:
#         print(f"The even numbers are {i}")
#     if i%2==1:
#         print(f"The odd numbers are {i}")
#Question5
# def fibonacci(x):
#     a=0
#     b=1
#     for _ in range(x):
#         print(a, end=" ")
#         a, b = b, a + b

# fibonacci(10)
#Functions
def summ(a,b):
    return a+b
#Question2
def prime(numm):
    if numm > 1:
        for i in range(2, numm):
            if numm % i == 0:
                print("It is not a Prime number")
        else:
            print("It is a Prime number")
   
#Question3
def fact(factn):
    for i in range(1,factn):
        factn=factn*i
    return factn

#Question4
def max_min(num_list):
    maximum=max(num_list)
    minimum=min(num_list)
    return maximum,minimum

l=[3,5,1,9,6,2]
maxi,mini=max_min(l)
print(f"Maximum={maxi}, Minimum={mini}")

#Question5
r=9
for i in range(r):
    for j in range(r):
        if i == j or i + j == r - 1:
            print("*", end=" ")
        else:
            print(" ", end="*")
    print()
