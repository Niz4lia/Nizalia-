import math
def calculate_square_root():
    try:
        num = float(input("Enter a number to find its square root: "))
        if num < 0:
            raise ValueError("Cannot compute square root of a negative number.")
        result = math.sqrt(num)
    except ValueError:
        print(f"Error")
    else:
        print(f"The square root of {num} is {result}")
    finally:
        print("Operation complete.")
calculate_square_root()