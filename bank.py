from traceback import print_tb
import sys

db = list()
customers = list()
bank_accounts = list()


class BankAccount():
    transactions = []

    def __init__(self, account_number, balance, owner, type) -> None:
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.type = type
        bank_accounts.append(self)

    def __str__(self) -> str:
        return (
            self.account_number + " " + str(self.balance) + " " +
            self.owner + " " + self.type +
            "\n Transactions => " + str(self.transactions)
        )

    def add_to_bank(self):
        print("Enter Bank Here: ")
        b = input()
        for bank in db:
            if bank.name == b:
                bank.accounts.append(self)
            else:
                print("Bank Not Found.")

    def add_to_customer(self):
        print("Enter Customer Name: ")
        c = input()
        for customer in customers:
            if customer.name == c:
                customer.accounts.append(self)
            else:
                print("Customer Not Found")


class Bank():
    accounts = []

    def __init__(self, name):
        self.name = name

        db.append(self)

    def __str__(self) -> str:
        return self.name + "\n Accounts => " + str(self.accounts)


class Customer():
    accounts = []

    def __init__(self, name) -> None:
        self.name = name

        customers.append(self)

    def __str__(self) -> str:
        return self.name


class Transactions():
    def __init__(self, account, amount, type) -> None:
        self.account = account
        self.amount = amount
        self.type = type

    def add_to_account(self):
        for acc in bank_accounts:
            if acc.name == self.account:
                acc.transactions.append(self)
            else:
                print("Account Doesnt Exist.")


def main():
    print(
        "Enter A to create a bank or\n" +
        "Enter B to Create a customer or\n" +
        "Enter C to create a bank account\n" +
        "Enter D to add account to bank"
    )

    x = input()
    if x == "A":
        print("Enter a name for the bank: ")
        new_bank = input()
        Bank(new_bank)
        sys.exit(1)

    elif x == "B":
        print("Enter customer name: ")
        new_customer = input()
        Customer(new_customer)
        sys.exit(1)

    elif x == "C":
        print("Enter account number: ")
        new_account_number = input()
        print("Enter account balance: ")
        new_account_balance = input()
        print("Enter account owner: ")
        new_account_owner = input()
        print("Enter account type: ")
        new_account_type = input()

        BankAccount(new_account_number, new_account_balance,
                    new_account_owner, new_account_type)
        sys.exit(1)

    sys.exit(1)


if __name__ == "__main__":
    main()
