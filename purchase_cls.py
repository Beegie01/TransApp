from inventory_cls import *

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


    def prod_id(self):

        acc_range = [self.inventory['Product_ID'][0], self.inventory['Product_ID'][1], \
        self.inventory['Product_ID'][2], self.inventory['Product_ID'][3], self.inventory['Product_ID'][4]]

        while True:
            print(f"{self.inventory['Product_ID'][0]} for {self.inventory['Product_Name'][0]}\
            \n{self.inventory['Product_ID'][1]} for {self.inventory['Product_Name'][1]}\
            \n{self.inventory['Product_ID'][2]} for {self.inventory['Product_Name'][2]}\
            \n{self.inventory['Product_ID'][3]} for {self.inventory['Product_Name'][3]}\
            \n{self.inventory['Product_ID'][4]} for {self.inventory['Product_Name'][4]}")

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
            break

    def pur_qty(self):

        while True:
            val = input('\nQuantity:   ')
            try:
                qty = float(val)
            except ValueError:
                print(f"Error: {val} is not a number!")
                continue

            self.purchases['Purchased_Quantity'].append(self.qty)
            print("\nQuantity Entered!")
            self.update_stock(qty)
            break

    def pur_rate(self):
        while True:
            val = input('\nRate:    ')
            try:
                rate = float(val)
            except ValueError:
                print(f"Error: {val} is not a number!")
                continue

            self.purchases['Rate_of_Purchase'].append(rate)
            print("\nRate Entered!")
            self.purchases['Amount'].append(qty * rate)
            break

    def update_stock(self, qty):

        if self.purchases['Product_ID'][-1] == self.inventory['Product_ID'][0]:
            self.inventory['Stock']['Iron Rods'] += qty
        elif self.purchases['Product_ID'][-1] == self.inventory['Product_ID'][1]:
            self.inventory['Stock']['Nails'] += qty
        elif self.purchases['Product_ID'][-1] == self.inventory['Product_ID'][2]:
            self.inventory['Stock']['Steel Pipes'] += qty
        elif self.purchases['Product_ID'][-1] == self.inventory['Product_ID'][3]:
            self.inventory['Stock']['Angle Bars'] += qty
        elif self.purchases['Product_ID'][-1] == self.inventory['Product_ID'][4]:
            self.inventory['Stock']['Binding Wire'] += qty

    def new_purchase(self):

        self.prod_id()

        self.pur_qty()

        self.pur_rate()

        self.set_id()
        return print("\n\nOne Purchase added!")


    def commit_to_file(self):
        file = "C:\\Users\\welcome\\Desktop\\Transapp\\purchases.txt"

        handle = open(file, 'a')

        DELIM = ', '
        #order_of_col: Purchase_Date, Purchase_Time, Product_ID, Purchase_Quantity, Rate_of_Purchase, Amount
        text = f"\n{DELIM.join(self.purchases['Purchase_Date'])}, {DELIM.join(self.purchases['Purchase_Time'])}, {DELIM.join(self.purchases['Product_ID'])}, {DELIM.join(self.purchases['Purchased_Quantity'])}, {DELIM.join(self.purchases['Rate_of_Purchase'])}, {DELIM.join(self.purchases['Amount'])}"

        handle.write(text)

        handle.close()

        print('New Purchase Detail Saved!')
