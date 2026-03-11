
print("Penrose Bake Shop")
print("-"*30)

menu = {'Brownie' : 2.5,
        'Croissant' : 3,
        'Choco Cookie' : 2.75}

for food, price in menu.items():
    print(f'{food:15} USD {price}')

bill = 0

order = input("Kindly place your Order:\n").title()

if order in menu:

    quantity = int(input(f'How Many {order}s do you wish to Order?\n'))

    bill += menu[order] * quantity
