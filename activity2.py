actual_Cost=int(input("please enter the actual product price "))
sale_amount=int(input("Please enter the sale amount "))

if sale_amount>actual_Cost:
    amount=sale_amount-actual_Cost
    print("Total profit is ",amount)
else:
    print("no profit ")   

