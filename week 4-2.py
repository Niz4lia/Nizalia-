# Initial inventory
inventory = {
    "Laptop": 10,
    "Smartphone": 25,
    "Tablet": 15,
    "Headphones": 30,
    "Smartwatch": 20
}
inventory.update({
    "Smartphone": inventory["Smartphone"] + 10,
    "Headphones": inventory["Headphones"] + 5
})

print("Updated inventory after new shipments:")
print(inventory)


lasti,quant = inventory.popitem()
print(f"\nSold item: {lasti}, Quantity removed: {quant}")
print("Inventory after selling last item:")
print(inventory)
print()

camera= inventory.get("Camera", "Out of Stock")
print(f"Camera stock: {camera}")
