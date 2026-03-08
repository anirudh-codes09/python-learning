colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']
for color in colors:
    print(color)

print("-"*30)
new_color = input("Please enter a new color: ")
print("-"*30)

colors.append(new_color.lower())
for color in colors:
    print(color)


print("-"*30)
removed_color = input("Please remove a color: ")
print("-"*30)
while removed_color.lower() not in colors:
    removed_color = input("Please enter a valid color: ")

colors.remove(removed_color.lower())
for color in colors:
    print(color)

