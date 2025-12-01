emp=input("Enter employee name(Alice, Bob, Charlie, David, Eve):\n")
rate=int(input("Enter employee rating(1-5): "))
if rate==5:
    print(f'{emp} has a rating of {rate}, and has received a bonus of $1000.')
elif rate==4:
    print(f'{emp} has a rating of {rate}, and has received a bonus of $750.')
elif rate==3:
    print(f'{emp} has a rating of {rate}, and has received a bonus of $500.')
else:
    print(f'{emp} has a rating of {rate}, and has received no bonus.')