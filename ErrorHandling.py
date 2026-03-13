while True:
    try:
        num = int(input("Please enter a number:"))
    except ValueError:
        print("Please enter a valid number")
    else:
        print(num)
        break