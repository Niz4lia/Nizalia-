def complex_calculation():
    try:
        num1=int(input("Enter a number: "))
        num=num1/(num1-5)
        print("Result: ",num)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except ValueError:
        print('You did not provide a number')
    finally:
        print('processing complete')
    
complex_calculation()