from services.bank_service import BankService

bank = BankService()

def menu():
    while True:
        print("\n===== Banking System =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Account")
        print("5. Delete Account")
        print("6. Show Statistics")
        print("7. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                name = input("Name: ")
                age = int(input("Age: "))
                email = input("Email: ")
                pin = int(input("PIN: "))

                acc_no = bank.create_account(name, age, email, pin)
                print(f"Account created successfully! Account No: {acc_no}")

            elif choice == "2":
                acc = input("Account No: ")
                pin = int(input("PIN: "))
                amt = int(input("Amount: "))

                balance = bank.deposit(acc, pin, amt)
                print(f"Updated Balance: {balance}")

            elif choice == "3":
                acc = input("Account No: ")
                pin = int(input("PIN: "))
                amt = int(input("Amount: "))

                balance = bank.withdraw(acc, pin, amt)
                print(f"Updated Balance: {balance}")

            elif choice == "4":
                acc = input("Account No: ")
                pin = int(input("PIN: "))

                user = bank.get_account(acc, pin)
                print(user)

            elif choice == "5":
                acc = input("Account No: ")
                pin = int(input("PIN: "))

                bank.delete_account(acc, pin)
                print("Account deleted successfully")

            elif choice == "6":
                stats = bank.get_statistics()
                print(stats)

            elif choice == "7":
                print("Exiting...")
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    menu()