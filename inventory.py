invent = []
while True:
    item = input("Enter the item name (or type 'done' to finish): ")
    if not item:
        print("Item name cannot be empty. Please try again.")
        continue
    if item.lower() == 'done':
        print(f'Inventory(Item,Quantity)={invent}')
        break
    quan = int(input("Enter the quantity of the item: "))
    if quan <= 0:
        print("Please enter a valid quantity.")
        continue
    invent.append((item, quan))
