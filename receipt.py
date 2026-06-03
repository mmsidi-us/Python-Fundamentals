item1_name = "Notebook"
item1_price = "4.99"
item1_qty = "2"

item2_name = "Pen Pack"
item2_price = "7.50"
item2_qty = "1"

item3_name = "Backpack"
item3_price = "34.99"
item3_qty = "1"

tax_rate = "0.075"   # 7.5% sales tax

subtotal1= float(item1_price)*float(item1_qty)
subtotal2= float(item2_price)*float(item2_qty)
subtotal3= float(item3_price)*float(item3_qty)
subtotal= subtotal1 + subtotal2 + subtotal3
tax= (subtotal * 0.075)
total= subtotal + tax
print('=' * 40)
print('          STORE RECEIPT')
print('=' * 40)
print(f'Notebook   ${item1_price} * {item1_qty}    ${subtotal1}')
print(f'Pen Pack   ${item2_price} * {item2_qty}    ${subtotal2}')
print(f'Backpack   ${item3_price} * {item3_qty}   ${subtotal3}')
print('-' * 40)
print(f"Subtotal:               ${subtotal}")
print(f"Tax (7.5%):             ${tax:.2f}")
print('=' * 40)
print(f"Total:                  ${total:.2f}")
print('=' * 40)
