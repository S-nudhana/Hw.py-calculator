price = int(input('Enter the price of the meal:'))
vat = price * 0.07
total = vat + price

print('Price of meal:',price)
print('VAT:',vat)
print('Total Amount:',total)

pay = int(input('Amount Tender:'))
print('Amount tender',pay)
print('Total Amount:',total)
print('Change:',pay - total)