price = 10000000
print('price is: ' + price)
valid_credit = 500
new_price1 = str(price * 0.1)
new_price2 = str(price * 0.2)

credit = int(input('enter your credit score: '))
if credit > valid_credit:
    print('down-payment of the house for you is: '+ new_price1)
else:
    print('down-payment of the house for you is: ' + new_price2)