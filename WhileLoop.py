ACCOUNT_PIN = 123456

pin = int(input("Enter your PIN here:\n "))

while pin != ACCOUNT_PIN:
    pin = int(input("Sorry incorrect, re-enter your PIN here:\n "))