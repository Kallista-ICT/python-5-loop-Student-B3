money = 500

while money > 0:
    print(f"You Have ${money}")
    try:
        broke = int(input("How Much Do You Wanna Withdraw Fam:"))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if broke == 0 :
        print("Don't Come Back.")
        break
    
    previous_money = money
    money -= broke

    if money < 0 :
        print("Insufficient Funds")
        money = previous_money
    else : 
        print(f"You've withdrawn ${money}")
    
    