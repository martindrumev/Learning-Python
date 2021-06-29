giving_coins = float(input("Giving coins: "))
receiving_coins = 0

five_hundred = 0
one_hundred = 0
twenty_five = 0
ten = 0
five = 0
one = 0

while giving_coins != 0:
    if giving_coins >= 500:
        five_hundred = giving_coins // 500
        giving_coins = giving_coins % 500
    elif giving_coins >= 100:
        one_hundred = giving_coins // 100
        giving_coins = giving_coins % 100
    elif giving_coins >= 25:
        twenty_five = giving_coins // 25
        giving_coins = giving_coins % 25
    elif giving_coins >= 10:
        ten = giving_coins // 10
        giving_coins = giving_coins % 10
    elif giving_coins >= 5:
        five = giving_coins // 5
        giving_coins = giving_coins % 5
    elif giving_coins >= 1:
        one = giving_coins // 1
        giving_coins = giving_coins % 1

receiving_coins = five_hundred + one_hundred + twenty_five + ten + five + one
print("Totaal coins to receive: " + str(receiving_coins))
print("Coins of 500 to receive: " + str(five_hundred))
print("Coins of 100 to receive: " + str(one_hundred))
print("Coins of 25 to receive: " + str(twenty_five))
print("Coins of 10 to receive: " + str(ten))
print("Coins of 5 to receive: " + str(five))
print("Coins of 1 to receive: " + str(one))