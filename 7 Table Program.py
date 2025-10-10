#Table
num=int(input("Enter the table No.:"))
end=int(input("Enter where you want to finish"))
print(f"Table of{num}")
for i in range(1, end+1):
    
    val = num * i
    print(val)