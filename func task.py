def calculate_price(prices=None, discount=0, tax=0):
    if prices is None:
        prices = list(map(int, input("Enter the prices of the items (comma-separated): ").split(",")))
    payment_method = input("Enter the payment method (card/cash): ").lower()
    if payment_method == 'card':
        discount = 8
    elif payment_method == 'cash':
        discount = 10
    else:
        print("Invalid payment method. No discount applied.")
        discount

    discprice = [price - (price * discount / 100) for price in prices]
    tax = [price * 0.18 for price in discprice]
    total_price = sum(discprice) + sum(tax)
    print(total_price)
calculate_price(prices=list(map(int, input("Enter the prices of the items (comma-separated): ").split(","))), discount=5, tax=18)

