import time
import random
from datetime import datetime
import re


def main_menu():
    while True:
        print("\nWelcome to the Banking System!")
        print("1. Open new Bank Account")
        print("2. Activate Digital Banking facility")
        print("3. Login to Digital Banking")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            open_bank_account()
        elif choice == "2":
            activate_digi_banking()
        elif choice == "3":
            login_digi_banking()
        elif choice == "4":
            print("Thank you! Visit again.")
            break
        else:
            print("Invalid choice. Please try again.")

# new bank account opening
def open_bank_account():
    print("\nOpen a New Bank Account")

    while True:
        first_name = input("First Name (As per PAN Card): ").strip()
        if first_name.isalpha():
            break
        print("First name must contain only letters.")

    while True:
        last_name = input("Last Name (As per PAN Card): ").strip()
        if last_name.isalpha():
            break
        print("Last name must contain only letters.")

    while True:
        date_of_birth = input("Date of Birth (DD/MM/YY): ").strip()
        if re.match(r"\d{2}/\d{2}/\d{2}", date_of_birth):
            break
        print("Invalid date format. Use DD/MM/YY.")

    while True:
        aadhar_number = input("Aadhar Number (12 digits): ").strip()
        if re.match(r"^\d{12}$", aadhar_number):
            break
        print("Aadhar number must be 12 digits.")

    while True:
        pan_card = input("PAN Card Number (e.g. ABCDE1234F): ").strip().upper()
        if re.match(r"^[A-Z]{5}[0-9]{4}[A-Z]$", pan_card):
            break
        print("Invalid PAN format. Should be 5 letters, 4 digits, and 1 letter (e.g. ABCDE1234F).")

    while True:
        phone_number = input("Aadhar-linked Phone Number (10 digits): ").strip()
        if re.match(r"^[6-9]\d{9}$", phone_number):
            break
        print("Invalid phone number. Must be 10 digits and start with 6-9.")

    print("\nSelect Account Type:")
    print("1. Savings")
    print("2. Salary")
    print("3. Current")

    account_type_map = {
        "1": "Savings",
        "2": "Salary",
        "3": "Current"
    }

    while True:
        account_type_choice = input("Enter the number of your choice (1/2/3): ").strip()
        if account_type_choice in account_type_map:
            account_type = account_type_map[account_type_choice]
            break
        print("Invalid choice! Please enter 1, 2, or 3.")

    branch_select = input("Enter Preferred Branch: ").strip()

    full_name = f"{first_name} {last_name}"

    print("Verifying KYC...⌛")
    time.sleep(2)
    print("Verification Completed")

    print("Generating account number...⌛")
    time.sleep(1)
    account_number = random.randint(1000000000, 9999999999)
    print("Account number generated successfully!")

    bank_code = "BRCH"
    branch_code = str(random.randint(100000, 999999))
    ifsc_code = bank_code + "0" + branch_code

    while True:
        try:
            initial_deposit = float(input("Enter initial deposit amount (minimum ₹500): "))
            if initial_deposit >= 500:
                print("Deposited Successfully!")
                break
            else:
                print("Minimum deposit amount is ₹500.")
        except ValueError:
            print("Please enter a valid number.")

    with open("accounts.txt", "a") as file:
        file.write(f"{account_number},{ifsc_code},{first_name},{last_name},{date_of_birth},{aadhar_number},{pan_card},{phone_number},{account_type},{branch_select},{initial_deposit}\n")

    print(f"\nAccount created successfully for {full_name}")
    print(f"Account Number: {account_number}")
    print(f"IFSC Code: {ifsc_code}")
    print(f"Account Type: {account_type}")
    print(f"Current Balance: ₹{initial_deposit}")

    activation = input('Press "2" to activate Digital Banking facility: ').strip()
    if activation == "2":
        activate_digi_banking(phone_number, account_number) 
    else:
        print("You can activate digital banking later from the main menu.")

# Activate Digital Banking
def activate_digi_banking(phone_number=None, account_number=None):
    print("\nDigital Banking Facility Activation")

    if not phone_number:
        phone_number = input("Enter your registered phone number: ").strip()

    found = False
    with open("accounts.txt", "r") as file:
        for line in file:
            details = line.strip().split(",")
            if len(details) >= 8 and details[7] == phone_number:
                full_name = f"{details[2]} {details[3]}"
                account_number = details[0]
                found = True
                break

    if not found:
        print("Phone number not found! Please open a bank account first.")
        return

    print(f"\nHello {full_name}, verification successful")

    attempts = 3
    while attempts > 0:
        verification = input("Re-enter your phone number for verification: ").strip()
        print("Verifying phone number...⌛")
        time.sleep(1)

        if verification == phone_number:
            print("Verification Successful!")
            break
        else:
            attempts -= 1
            print(f"Incorrect phone number. {attempts} attempt(s) left.")
    if attempts == 0:
        print("Too many failed attempts! Try again later.")
        return

    # Create User ID
    while True:
        user_id = input("Create username (min 6 characters, letters & numbers only): ").strip()
        if len(user_id) >= 6 and user_id.isalnum():
            break
        print("Invalid username. Try again.")

    # Create Password
    while True:
        password = input("Create password (min 8 characters, letters & numbers only): ").strip()
        if len(password) >= 8 and password.isalnum():
            break
        print("Invalid password. Try again.")

    with open("digital_users.txt", "a") as file:
        file.write(f"{user_id},{password},{account_number}\n")

    print("\nDigital banking activated successfully!")
    print(f"Your username: {user_id}")

# Login to Digital Banking
def login_digi_banking():
    print("\nDigital Banking Login")
    enter_userid = input("Username: ").strip()
    enter_password = input("Password: ").strip()

    user_found = False
    with open("digital_users.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) >= 3 and parts[0] == enter_userid and parts[1] == enter_password:
                account_number = parts[2]
                user_found = True
                break

    if not user_found:
        print("Invalid username or password. Try again.")
        return

    with open("accounts.txt", "r") as file:
        for line in file:
            acc_info = line.strip().split(",")
            if len(acc_info) >= 11 and acc_info[0] == account_number:
                full_name = f"{acc_info[2]} {acc_info[3]}"
                ifsc_code = acc_info[1]
                initial_deposit = float(acc_info[10])
                break

    print(f"\nLogin successful! Welcome, {full_name}")
    print(f"Account Number: {account_number}\nIFSC Code: {ifsc_code}\nCurrent Balance: ₹{get_balance(account_number, initial_deposit)}")

    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")
        choice = input("Choose an option (1/2/3/4): ").strip()

        if choice == "1":
            balance = get_balance(account_number, initial_deposit)
            print(f"Current Balance: ₹{balance}")
        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount > 0:
                    log_transaction(account_number, "Deposit", amount)
                    print(f"Deposit successful! New Balance: ₹{get_balance(account_number, initial_deposit)}")
                else:
                    print("Amount must be positive.")
            except ValueError:
                print("Invalid amount.")
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: "))
                balance = get_balance(account_number, initial_deposit)
                if 0 < amount <= balance:
                    log_transaction(account_number, "Withdrawal", amount)
                    print(f"Withdrawal successful! New Balance: ₹{get_balance(account_number, initial_deposit)}")
                else:
                    print("Insufficient balance or invalid amount.")
            except ValueError:
                print("Invalid amount.")
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid option. Try again.")

# Record transaction
def log_transaction(account_number, transaction_type, amount):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("transactions.txt", "a") as file:
        file.write(f"{account_number},{transaction_type},{amount},{now}\n")

# Calculate current balance
def get_balance(account_number, initial_deposit):
    balance = initial_deposit
    try:
        with open("transactions.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) >= 3 and parts[0] == str(account_number):
                    t_type = parts[1]
                    amt = float(parts[2])
                    if t_type == "Deposit":
                        balance += amt
                    elif t_type == "Withdrawal":
                        balance -= amt
    except FileNotFoundError:
        pass
    return balance

main_menu()

