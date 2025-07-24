balance = 1000
pin = "1234"
entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        if choice == "1":
            print("Your Balance is : ", balance)
        elif choice == "2":
            withdraw = int(input("Enter withdraw : "))
            if withdraw <= balance:
                total = balance - withdraw
                print("Successfully withdraw")
                print("Your balace is : ", total)
            elif withdraw > balance:
                print("You can't withdraw")
            elif withdraw < 0:
                print("You can't withdraw")
        elif choice == "3":
            deposit = int(input("Enter Deposit : "))
            if deposit < 0:
                print("You can't deposit!")
            else :
                totaldepo = balance + deposit
                print("Your balance is : ", totaldepo)
        elif choice == "4":
            print("EXIT!")
            break
else:
    print("Invalid PIN")