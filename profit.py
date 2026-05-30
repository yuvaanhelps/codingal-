actual_cost = float(input("please enter the actual amount price:"))
sale_amount = float(input("please enter the actual sale price:"))
if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("total profit = {0}".format(amount))
else:
    print("no profit")


