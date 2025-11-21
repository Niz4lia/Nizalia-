a=1
try:
    b=int(input("Enter a number: "))
    a=a/b
    
except ZeroDivisionError:
    print("You provided number to be divided by 0")
except ValueError:
    print('You did not provide a number')
except:
    print("Something went wrong")
else:
    print("success: ",a)
finally:
    print('processing complete')