ac=float(input('Please enter your actual cost: £'))
sp=float(input('Please enter your selling price: £'))
if ac>sp:
    print('You have made a loss of £',ac-sp)
elif ac<sp:
    print('You have made a profit of £',sp-ac)
else:
    print('No profit')