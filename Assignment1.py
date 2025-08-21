

#TOTAL_FEES is the constant
TOTAL_FEES = 700
#paid is the variable
paid = int(input("Please enter the amount you wish to pay: -"))
balance = TOTAL_FEES - paid

if balance == 0:
    print("Lecture access granted!")
elif balance > 0:
    print("Please settle your balance of " + str(balance) + " inorder to receive lecture access.")
elif balance < 0:
    print("Your change will be credited. (maybe.)")
else:
    print("Invalid input.")