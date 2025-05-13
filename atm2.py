money = 500

while True:
    print(f"\nCurrent balance: ${money}")
    try:
        withdraw = int(input("Enter amount to withdraw (or 0 to quit): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if withdraw == 0:
        print("Goodbye!")
        break

    previous_money = money  # Save current state before withdrawal
    money -= withdraw       # Attempt withdrawal

    if money < 0:
        print("Insufficient funds. Transaction canceled.")
        money = previous_money  # Revert to previous balance
    else:
        print(f"Withdrawal of ${withdraw} successful.")