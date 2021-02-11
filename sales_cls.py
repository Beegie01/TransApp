class Sales(Inventory):

    def __init__(self):
        Inventory.__init__(self)
        self.sales['Order_Date'].append(datetime.date(datetime.now()))
        self.sales['Order_Time'].append(datetime.time(datetime.now()))
        #self.order_id = None
        #self.prod_id = None
        #self.cust_id = None
        #self.qty = None
        #self.rate = None
        #self.amount_due = None
        #self.deposit = None
        #self.payment_status = None
        #self.date_of_completion = None

    def set_id(self):
        order_id = str(self.sales['Product_ID']) + self.sales['Customer_ID'][-1][:2] + str(self.sales['Order_Date'][-1].year) + str(self.sales['Order_Time'][-1].hour)\
        + str(self.sales['Order_Time'][-1].minute)
        self.sales['Order_ID'].append(order_id)
        print("\nOrder_ID has been set!")

    def new_order(self):

        # CORRESPONDING PRODUCT ID
        P = True
        while P:
            inp = input("Product ID:    ")
            try:
                prod_id = int(inp)
            except ValueError:
                print(f"Error: {inp} is not a number!")
                continue
            self.sales['Product_ID'].append(prod_id)
            print("Product ID Entered!")
            P = False

        # CORRESPONDING CUSTOMER ID
        C = True
        while C:
            inp = input("Customer ID:    ")

            if inp.isdigit() or len(inp) != 10:
                print(f"Error: {inp} is invalid!")
                continue
            self.sales['Customer_ID'].append(inp)
            print("Customer ID Entered!")
            C = False

        # QUANTITY ORDERED BY CUSTOMER
        Q = True
        while Q:
            val = input('\nQuantity:   ')
            try:
                qty = float(val)
            except ValueError:
                print(f"Error: {val} is not a number!")
                continue

            self.sales['Ordered_Quantity'].append(qty)
            print("\nQuantity Entered!")
            Q = False

        # SELLING RATE
        R = True
        while R:
            val = input('\nRate:    ')
            try:
                rate = float(val)
            except ValueError:
                print(f"Error: {val} is not a number!")
                continue

            self.sales['Rate'].append(rate)
            print("\nRate Entered!")
            R = False

        # CUSTOMER'S DEPOSIT
        D = True
        while D:
            val = input('\nAmount Deposited:    ')
            try:
                dep = float(val)
            except ValueError:
                print(f"Error: {val} is not a number!")
                continue

            self.sales['Amount_Deposited'].append(dep)
            due = (rate * qty) - dep
            if due < 0:
                self.sales['Amount_Due'].append(0)
                self.accounts['Balance'].append(abs(due))
            else:
                self.sales['Amount_Due'].append(due)
            print("\nRate Entered!")
            D = False

        # PAYMENT STATUS
        if self.sales['Amount_Due'][-1] == 0:
            self.sales['Payment_Status'].append('Payment Complete')
        elif self.sales['Amount_Due'][-1] > 0:
            self.sales['Payment_Status'].append('Pending Transaction')

        # PAYMENT DATE
        if self.sales['Payment_Status'][-1] == 'Payment Complete':
            D = True
            while D:
                Yr = True
                while Yr:
                    print("Please Enter Date of Last Payment Below\n")
                    acc_range = range(1920, 2022)
                    inp = input("Year:   ")

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
                    inp = input("Month:   ")

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
                    inp = input("Day:   ")

                    try:
                        day = int(inp)
                    except ValueError:
                        print(f'{val} is invalid!')
                        continue

                    if day not in acc_range:
                        print(f'{val} is out of range!')
                        continue
                    Day = False

                self.sales['Date_of_Completion'].append(date(yr,mon,day))
                print("Payment Date Entered!")
                D = False

            self.set_id()
            print("\n\nOne Order Added!")

        def save_row_to_file(self):
            file = "C:\\Users\\welcome\\Desktop\\Transapp\\orders.txt"

            handle = open(file, 'a')

            #order_of_col: Order_Date, Order_Time, Order_ID, Product_ID, Customer_ID, Order_Quantity, Rate, Amount_Due, Amount_Deposited, Payment_Status, Date_of_Completion
            text = f"\n{self.order_date}, {self.order_time}, {self.order_id}, {self.prod_id}, {self.cust_id}, {self.qty}, {self.rate}, {self.amount_due}, {self.deposit}, {self.payment_status}, {self.date_of_completion}"

            handle.write(text)

            handle.close()
