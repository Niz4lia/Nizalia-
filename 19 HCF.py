x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
def compute_hcf(x, y):
    while(y):
        x, y= y, x % y
    return x
hcf= compute_hcf(x, y)
print("The HCF is:", hcf)
