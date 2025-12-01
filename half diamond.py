bank = [
    "KAR128831",
    "ISL140049",
    "NYC117720",
    "MUL105532",
    "QUE139120",
    "NYC143378",
    "ISL104481",
    "KAR111920",
    "MUL137712",
    "NYC129084",
    "QUE115570",
    "ISL126619",
    "KAR130029",
    "MUL143311",
    "NYC104490",
    "ISL119077",
    "QUE141150",
    "KAR149941",
    "MUL111208",
    "QUE137714",
    "MUL124033",
    "NYC132201",
    "ISL135630",
    "QUE129404",
    "KAR107721"
]

regions = ["NYC", "KAR", "ISL", "MUL", "QUE"]
branches = ["10", "11", "12", "13", "14"]

# Dictionaries for grouping
region_groups = {r: [] for r in regions}
branch_groups = {b: [] for b in branches}

# Process each account
for acc in bank:
    # Extracting using indexing
    region_code = acc[0:3]
    branch_code = acc[3:5]
    customer_number = acc[5:]

    # Print extracted parts
    print(f"ACCOUNT: {acc}")
    print(f"  Region Code: {region_code}")
    print(f"  Branch Code: {branch_code}")
    print(f"  Customer Number: {customer_number}")

    # Categorizing by region
    if region_code in region_groups:
        region_groups[region_code].append(acc)
    else:
        print("  Invalid Region Code!")

    # Categorizing by branch
    if branch_code in branch_groups:
        branch_groups[branch_code].append(acc)
    else:
        print("  Invalid Branch Code!")

    print("-----------------------------------")

# Final grouped output
print("\n=== Accounts Grouped by Region ===")
for r, items in region_groups.items():
    print(f"{r}: {items}")

print("\n=== Accounts Grouped by Branch ===")
for b, items in branch_groups.items():
    print(f"{b}: {items}")

   

        

