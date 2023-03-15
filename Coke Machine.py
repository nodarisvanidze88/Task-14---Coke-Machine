cokePrice = 50
coins = [25, 10, 5]

while True:
    if cokePrice > 0:
        print("Amount Due: " + str(cokePrice))
        user = int(input("Insert coin: "))
        if user not in coins:
            print("Wrong coin, please insert another")
        else:
            cokePrice = cokePrice-user
    else:
        print("Change Owed: " + str(cokePrice))
        break
