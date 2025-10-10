n=int(input("Enter the Size of List: "))
lst=list(map(int,input("Enter The integer: ").strip().split()))[:n]
print("The list is:", lst)

lst.append(3)
print(lst)