def withdraw(balance,amount):
    if amount>balance:
        raise Exception('Insufficient Balance')
    balance=balance-amount
    return balance
try:
    current=100
    amount=int(input('Enter the amount to withdraw: '))
    newbalance=withdraw(current,amount)
    print('Withdraw succesfull',newbalance)
except Exception as e:
    print(e)