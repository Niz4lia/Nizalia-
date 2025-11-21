acc= {}

n = int(input("How many accounts? "))

for i in range(n):
    acc = input(f"Enter account number {i+1}: ")

    region = acc[0:3]     # first 3 letters
    branch = acc[3:5]     # next 2
    customer = acc[5:]    # rest

    # categorize
    if region not in acc:
        acc[region] = {}
    if branch not in acc[region]:
        acc[region][branch] = []

    acc[region][branch].append(customer)

# show result
print("\nAccounts by Region and Branch:")
for region in acc:
    print("Region:", region)
    for branch in acc[region]:
        print("  Branch", branch, ":", acc[region][branch])