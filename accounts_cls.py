import string
import datetime
from datetime import datetime, date, time

from datareservoir_cls import *

class Accounts(DataReservoir):

    def __init__(self):
        self.today = datetime.today()
        self.transaction_date = datetime.date(self.today)
        self.transaction_time = datetime.time(self.today)
        self.account_id = None
        self.customer_id = None
        self.debit = None
        self.credit = None
        self.balance = None
        self.last_added = []
        self.all_added = []


    def __str__(self):
        return f"\nCUSTOMER ACCOUNT DETAILS:\
        \nACCOUNT ID: {[n[0] for n in self.all_added]}\
        \nCUSTOMER ID: {[n[1] for n in self.all_added]}\
        \nDEBITED AMOUNT: {[n[2] for n in self.all_added]}\
        \nCREDITED AMOUNT: {[n[3] for n in self.all_added]}\
        \nBALANCE: {[n[4] for n in self.all_added]}\
        \nTRANSACTION DATE: {[n[5] for n in self.all_added]}\
        \nTRANSACTION TIME: {[n[6] for n in self.all_added]}"

    def set_id(self):
        acct_id = str(self.transaction_date.year) + str(self.transaction_time.hour)\
         + str(self.transaction_time.minute) + str(self.transaction_time.second)\
        + self.customer_id[-3:]

        self.account_id = acct_id
        print("Account ID has been set!")

    # CORRESPONDING CUSTOMER ID
    def new_cust_id(self):
        while True:
            inp = input("\nCustomer ID:    ")

            if inp.isdigit() or len(inp) != 10:
                print(f"Error: {inp} is invalid!")
                continue
            self.customer_id = inp
            print("Customer ID Entered!")
            break

        # DEBIT AMOUNT
    def dr_amount(self):
        while True:
            val = input('\nDebit:    ')
            try:
                dr = float(val)
            except ValueError:
                print(f"Error: {val} is not a number!")
                continue

            self.debit = dr
            print("\nDebited Amount Entered!")
            break

        # DEBIT AMOUNT
    def cr_amount(self):
        while True:
            val = input('\nCredit:    ')
            try:
                cr = float(val)
            except ValueError:
                print(f"Error: {val} is not a number!")
                continue

            self.credit = cr
            print("\nCredited Amount Entered!")
            break

        # BALANCE AMOUNT
    def bal(self):
        if self.credit > self.debit:
            self.balance = self.credit - self.debit
        else:
            self.balance = 0


    def new_transaction(self):

        # CUSTOMER ID
        self.new_cust_id()

        # DEBIT
        self.dr_amount()

        # CREDIT
        self.cr_amount()

        # BALANCE
        self.bal()

        self.set_id()

        add_list = [self.account_id, self.customer_id, self.debit,\
        self.credit, self.balance, self.transaction_date, self.transaction_time]

        self.last_added = add_list
        print(self.last_added)
        self.all_added.append(self.last_added)
        print(self.all_added)
        print("\n\nOne Transaction Added!")


    def commit_to_file(self):
        file = "C:\\Users\\welcome\\Desktop\\Transapp\\transactions.txt"

        handle = open(file, 'a')

        #order_of_col: Account_ID, Customer_ID, Debit, Credit, Balance, Transaction_Date, Transaction_Time

        text = f"\n{[new for new in self.all_added]}"

        handle.write(text)

        handle.close()

        print('Transaction Detail Saved!')
