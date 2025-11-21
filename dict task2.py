inventory={}

inventory['Product01'] = 'Mobile Phone'
inventory['Product01_quantity']=5
inventory['Product01_price']=20000
inventory['Product01_year']=2020

inventory['Product02'] = 'Laptop'
inventory['Product02_quantity']=10
inventory['Product02_price']=50000
inventory['Product02_year']=2023

print(inventory)

if 'Product01_year' in inventory and "Product02_year" in inventory:
    print("Both products have year information.")

del inventory['Product01_year']
del inventory['Product02_year']