class Purchase(Inventory):

    def __init__(self):
        Inventory.__init__(self)
        self.purchases['Purchase_Date'].append(datetime.date(datetime.now()))
        self.purchases['Purchase_Time'].append(datetime.time(datetime.now()))
        #self.purchase_id = None
        #self.prod_id = None
        #self.qty = None
        #self.rate = None
        #self.amount = None

    def set_id(self):
        pur_id = str(self.purchases['Purchase_Date'][-1].year) + str(self.purchases['Purchase_Date'][-1].month)\
        + str(self.purchases['Product_ID'][-1]) + str(self.purchases['Purchase_Time'][-1].hour) + str(self.purchases['Purchase_Time'][-1].minute)
        self.purchases['Purchase_ID'].append(pur_id)
        print("\nPurchase_ID has been set!")

    def new_purchase(self):

        acc_range = [self.rods['ID'], self.nails['ID'], self.pipes['ID'], self.angles['ID'], self.bwires['ID']]

        P = True
        while P:
            print(f"{self.rods['ID']} for {self.rods['name']}\
            \n{self.nails['ID']} for {self.nails['name']}\
            \n{self.pipes['ID']} for {self.pipes['name']}\
            \n{self.angles['ID']} for {self.angles['name']}\
            \n{self.bwires['ID']} for {self.bwires['name']}")

            val = input("Enter 1-5:    ")

            try:
                prd = int(val)
            except ValueError:
                print(f"Error: {val} is not a number!")
                continue

            if prd not in acc_range:
                print(f"{prd} is out of range!")
                continue

            self.purchases['Product_ID'].append(prd)
            print("\nProduct Entered!")
            P = False


        Q = True
        while Q:
            val = input('\nQuantity:   ')
            try:
                qty = float(val)
            except ValueError:
                print(f"Error: {val} is not a number!")
                continue

            self.qty = qty
            self.purchases['Purchased_Quantity'].append(self.qty)
            print("\nQuantity Entered!")
            Q = False

        R = True
        while R:
            val = input('\nRate:    ')
            try:
                rate = float(val)
            except ValueError:
                print(f"Error: {val} is not a number!")
                continue

            self.purchases['Rate_of_Purchase'].append(rate)
            print("\nRate Entered!")
            R = False

        self.purchases['Amount'].append(qty * rate)

        if self.purchases['Product_ID'][-1] == self.rods['ID']:
            self.rods['stock'] += self.qty
        elif self.purchases['Product_ID'][-1] == self.nails['ID']:
            self.nails['stock'] += self.qty
        elif self.purchases['Product_ID'][-1] == self.pipes['ID']:
            self.pipes['stock'] += self.qty
        elif self.purchases['Product_ID'][-1] == self.angles['ID']:
            self.angles['stock'] += self.qty
        elif self.purchases['Product_ID'][-1] == self.bwires['ID']:
            self.bwires['stock'] += self.qty

        self.set_id()
        return print("\n\nOne Purchase added!")

    def save_row_to_file(self):
            file = "C:\\Users\\welcome\\Desktop\\Transapp\\purchases.txt"

            handle = open(file, 'a')

            #order_of_col: Purchase_Date, Purchase_Time, Product_ID, Purchase_Quantity, Rate_of_Purchase, Amount
            text = f"\n{self.purchase_date}, {self.purchase_time}, {self.prod_id}, {self.qty}, {self.rate}, {self.amount}"

            handle.write(text)

            handle.close()
