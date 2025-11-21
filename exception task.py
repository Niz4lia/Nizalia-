def safe_divide():
    
    try:
        denominator=int(input("Enter a number you want to divide with: : "))
        numerator=int(input("Enter The Number you want to divide: "))
        answer= numerator/denominator
        
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except ValueError:
        print('You did not provide a number')
    except:
        print("Something went wrong")
    else:
        print("success: ",answer)
    finally:
        print('processing complete')

safe_divide()