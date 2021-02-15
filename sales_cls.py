import string
import datetime
from datetime import datetime, date, time

from inventory_cls import *
from accounts_cls import *
import mydict_funcs as mdf

class Sales(Inventory, Accounts):

    count = 0

    def __init__(self):
        Inventory.__init__(self)
        Accounts.__init__(self)
        self.today = datetime.today()
        self.order_date = datetime.date(self.today)
        self.order_time = datetime.time(self.today)
        self.order_id = None
        self.product_id = None
        self.customer_id = None
        self.ordered_quantity = None
        self.rate_of_order = None
        self.amount_due = None
        self.amount_deposited = None
        self.balance = None
        self.payment_status = None
        self.date_of_completion = None
        self.last_added = []
        self.all_added = []

    def set_id(self):
        self.count += 1
        order_id = str(self.product_id) + self.customer_id[:2] + str(self.order_date.year) + str(self.order_time.hour)\
        + str(self.order_time.minute) + str(self.count)
        self.order_id = order_id
        print("\nOrder ID has been set!")

    def __str__(self):
        return f"\nCUSTOMER ORDER DETAILS:\
        \nORDER ID: {[n[0] for n in self.all_added]}\
        \nORDER DATE: {[n[1] for n in self.all_added]}\
        \nORDER TIME: {[n[2] for n in self.all_added]}\
        \nPRODUCT ID: {[n[3] for n in self.all_added]}\
        \nCUSTOMER ID: {[n[4] for n in self.all_added]}\
        \nORDERED QUANTITY: {[n[5] for n in self.all_added]}\
        \nRATE OF ORDER: {[n[6] for n in self.all_added]}\
        \nAMOUNT DUE: {[n[7] for n in self.all_added]}\
        \nDEPOSITED AMOUNT: {[n[8] for n in self.all_added]}\
        \nBALANCE: {[n[9] for n in self.all_added]}\
        \nPAYMENT STATUS: {[n[10] for n in self.all_added]}\
        \nDATE OF COMPLETION: {[n[11] for n in self.all_added]}"


    def prd_id(self):
        # CORRESPONDING PRODUCT ID
        P = True
        while P:
            inp = input("\nProduct ID:    ")
            try:
                prod_id = int(inp)
            except ValueError:
                print(f"Error: {inp} is not a number!")
                continue
            self.product_id = prod_id
            print("Product ID Entered!")
            P = False

    def cust_id(self):
        # CORRESPONDING CUSTOMER ID
        C = True
        while C:
            inp = input("\nCustomer ID:    ")

            if inp.isdigit() or (len(inp) != 11) or (inp in string.punctuation):
                print(f"Error: {inp} is invalid!")
                continue
            self.customer_id = inp
            print("Customer ID Entered!")
            C = False

    def ord_qty(self):
        # QUANTITY ORDERED BY CUSTOMER
        Q = True
        while Q:
            val = input('\nQuantity:   ')
            try:
                qty = float(val)
            except ValueError:
                print(f"Error: {val} is not a number!")
                continue

            self.ordered_quantity = qty
            print("Ordered Quantity Entered!")
            Q = False

    def ord_rate(self):
        # SELLING RATE
        R = True
        while R:
            val = input('\nRate of Product:    ')
            try:
                rate = float(val)
            except ValueError:
                print(f"Error: {val} is not a number!")
                continue

            self.rate_of_order = rate
            print("Rate of Order Entered!")
            R = False

    def amount(self):
        # CUSTOMER'S DEPOSIT
        D = True
        while D:
            val = input('\nAmount Deposited:    ')
            try:
                dep = float(val)
            except ValueError:
                print(f"Error: {val} is not a number!")
                continue

            self.amount_deposited = dep
            due = (self.rate_of_order * self.ordered_quantity) - dep
            if due < 0:
                self.amount_due = 0
                self.balance = abs(due)
            else:
                self.amount_due = due
            print("Deposited Amount Entered!")
            D = False

    def pay_status(self):
        # PAYMENT STATUS
        if self.amount_due == 0:
            self.payment_status = 'Payment Complete'
        elif self.amount_due > 0:
            self.payment_status = 'Pending Transaction'


    def pay_date(self):
        # PAYMENT DATE
        if self.payment_status == 'Payment Complete':
            D = True
            while D:
                Yr = True
                while Yr:
                    print("\nPlease Enter Date of Last Payment Below\n")
                    acc_range = range(1920, 2022)
                    inp = input("\nYear:   ")

                    try:
                        yr = int(inp)
                    except ValueError:
                        print(f'{val} is invalid!')
                        continue

                    if yr not in acc_range:
                        print(f'{val} is out of range!')
                        continue
                    Yr = False

                Mon = True
                while Mon:
                    acc_range = range(1,13)
                    inp = input("\nMonth:   ")

                    try:
                        mon = int(inp)
                    except ValueError:
                        print(f'{val} is invalid!')
                        continue

                    if mon not in acc_range:
                        print(f'{val} is out of range!')
                        continue
                    Mon = False

                Day = True
                while Day:
                    acc_range = range(1,31)
                    inp = input("\nDay:   ")

                    try:
                        day = int(inp)
                    except ValueError:
                        print(f'{val} is invalid!')
                        continue

                    if day not in acc_range:
                        print(f'{val} is out of range!')
                        continue
                    Day = False

                self.date_of_completion = date(yr,mon,day)
                print("Payment Date Entered!")
                D = False
            else:
                print('Transaction Pending!')
            D = False

    def new_order(self):

        self.prd_id()

        self.cust_id()

        self.ord_qty()

        self.ord_rate()

        self.amount()

        self.pay_status()

        self.pay_date()

        self.set_id()

        add_list = [self.order_id, str(self.order_date), str(self.order_time), self.product_id, self.customer_id, \
        self.ordered_quantity, self.rate_of_order, self.amount_due, self.amount_deposited, self.balance,\
         self.payment_status, str(self.date_of_completion)]

        self.last_added = add_list
        print(self.last_added)
        self.all_added.append(self.last_added)
        print(self.all_added)
        print("\n\nOne Order Added!")

    def ask_view(self):

        acc_range = ['last', 'l', 'a', 'all']

        while True:
            inp = input("To View:\nAll added records, enter 'a'\nOnly last added entry, enter 'l'\n")

            if inp.lower() not in acc_range:
                print(f'Error: {inp} is invalid!')
                continue
            return inp.lower()

    def view_rec(self):
        ans = self.ask_view()

        if ans in ['last', 'l']:
            print(self.last_added)

        elif ans in ['all', 'a']:
            print(self)

    def clear_last_entry(self):
        if len(self.last_added) > 0:
            self.last_added.clear()
        if len(self.all_added) > 0:
            rec = self.all_added.pop()
            print(f"{rec}\nHas Been Deleted!")
        else:
            print('\n\nNo new record to delete!')


    def commit_to_file(self):
        file = "C:\\Users\\welcome\\Desktop\\Transapp\\sales.txt"

        handle = open(file, 'a')

        #order_of_col: {row_num: [Order_ID, Order_Date, Order_Time, Product_ID, Customer_ID, Ordered_Quantity, Rate, Amount_Due, Amount_Deposited, Payment_Status, Date_of_Completion]}
        # Ensuring that empty rows are not saved
        if len(self.all_added) > 0:

            handle.write(text)

            handle.close()

            print('\n\nOrder Details Saved!')

        else:
            print("\n\nNo New Record To Save!")
