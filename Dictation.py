shopping_cart = ['eggs','milk','cheese','yoghurt','butter','more cheese']

shopping_cart_d = {'eggs' : '1 dozen',
                   'milk' : '4 cartons', 'cheese' : '100m Mozarella'}

for item,qty in shopping_cart_d.items():
    print(f'{item} - {qty}')

shopping_cart_d["ketchup"] = '1 bottle'

print()
for item,qty in shopping_cart_d.items():
    print(f'{item} - {qty}')

