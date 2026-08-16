# snack vending machine
# PART 1: a function that works out change and sends it back wit return
def calculate_change(paid,price):
    change= paid - price
    return change
# PART 2: set the snack price and greet the coustomer
snack_price = 25
print("=====SNACK VENDING MACHINE=====")
print(f"this snack cost{snack_price} units")
print("accepted coins: 1,5,10,25\n")
total_inserted= 0
coins_inserted = 0
# PART 3: keep accepting coins until enough money is inserted
while True:
    coin = int(input("insert a coin(1,5,10,0r 25):"))
    # PART 4: reject any coin that isn't a valid value
    if coin !=1 and coin !=5 and coin !=10 and coin !=25:
        print("invalid coin try again!\n")
        continue
  # PART 5 : add the valid coin  to the running total
    total_inserted += coin
    coins_inserted += 1
    print(f"inserted {coin}. total so far:{total_inserted}\n")
    # PART 6: stop asking for coins once enough has been inserted 
    if total_inserted >= snack_price:
        print("enough money inserted! \n")
        break
    # PART 7 work out the change using the value returned by calculate_change
    change_due= calculate_change(total_inserted, snack_price)
    print("dispensing your snack...")
    # PART 8
