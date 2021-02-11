class Accounts(DataReservoir):

    def __init__(self):
        self.accounts['Transaction_Date'].append(datetime.date(datetime.now()))
        self.accounts['Transaction_Time'].append(datetime.time(datetime.now()))
        #self.acct_id = None
        #self.cust_id = None
        #self.debit = None
        #self.credit = None
        #self.balance = None


    def set_id(self):
        acct_id = str(self.accounts['Transaction_Date'][-1].year) + str(self.accounts['Transaction_Time'][-1].hour) + str(self.accounts['Transaction_Time'][-1].minute)\
        + self.accounts['Customer_ID'][-1][:3]
        self.accounts['Account_ID'].append(acct_id)
        print("Account_ID has been set!")

    def new_transaction(self):

        # CORRESPONDING CUSTOMER ID
        C = True
        while C:
            inp = input("Customer ID:    ")

            if inp.isdigit() or len(inp) != 10:
                print(f"Error: {inp} is invalid!")
                continue
            self.accounts['Customer_ID'].append(inp)
            print("Customer ID Entered!")
            C = False

        # DEBIT AMOUNT
        Dr = True
        while Dr:
            val = input('\nDebit:    ')
            try:
                dr = float(val)
            except ValueError:
                print(f"Error: {val} is not a number!")
                continue

            self.accounts['Debit'].append(dr)
            print("\nDebited Amount Entered!")
            Dr = False

        # DEBIT AMOUNT
        Cr = True
        while Cr:
            val = input('\nCredit:    ')
            try:
                cr = float(val)
            except ValueError:
                print(f"Error: {val} is not a number!")
                continue

            self.accounts['Credit'].append(cr)
            print("\nCredited Amount Entered!")
            Cr = False

        # BALANCE AMOUNT
        if self.accounts['Credit'][-1] > self.accounts['Debit'][-1]:
            self.accounts['Balance'].append(self.accounts['Credit'][-1] - self.accounts['Debit'][-1])
        else:
            self.accounts['Balance'].append(0)

        self.set_id()
        print("\n\nOne Transaction Added!")
