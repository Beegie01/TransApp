from inventory_cls import *

class Purchase(Inventory):

    count = 0

    def __init__(self):
        Inventory.__init__(self)
        self.today = datetime.today()
        self.purchase_date = datetime.date(self.today)
        self.purchase_time = datetime.time(self.today)
        self.purchase_id = None
        self.product_id = None
        self.purchased_quantity = None
        self.rate_of_purchase = None
        self.amount = None
        self.last_added = []
        self.all_added = []

    def set_id(self):

        self.count += 1
        pur_id = str(self.purchase_date.year) + str(self.purchase_date.month)\
        + str(self.product_id) + str(self.purchase_time.hour) + str(self.purchase_time.minute)\
        + str(self.count)

        self.purchase_id = pur_id
        print("Purchase ID has been set!")


    def prod_id(self):

        acc_range = [Inventory.products['Product_ID'][0], Inventory.products['Product_ID'][1], \
        Inventory.products['Product_ID'][2], Inventory.products['Product_ID'][3], Inventory.products['Product_ID'][4]]

        while True:
            print(f"{Inventory.products['Product_ID'][0]} for {Inventory.products['Product_Name'][0]}\
            \n{Inventory.products['Product_ID'][1]} for {Inventory.products['Product_Name'][1]}\
            \n{Inventory.products['Product_ID'][2]} for {Inventory.products['Product_Name'][2]}\
            \n{Inventory.products['Product_ID'][3]} for {Inventory.products['Product_Name'][3]}\
            \n{Inventory.products['Product_ID'][4]} for {Inventory.products['Product_Name'][4]}")

            val = input("\nEnter between 1-5:    ")

            try:
                prd = int(val)
            except ValueError:
                print(f"Error: {val} is not a number!")
                continue

            if prd not in acc_range:
                print(f"{prd} is out of range!")
                continue

            self.product_id = prd
            print("Product Entered!")
            break

    def pur_qty(self):

        while True:
            val = input('\nQuantity:   ')
            try:
                qty = float(val)
            except ValueError:
                print(f"Error: {val} is not a number!")
                continue

            self.purchased_quantity = qty
            print("Quantity Entered!")
            self.update_stock(qty)
            break

    def pur_rate(self):
        while True:
            val = input('\nRate of Purchase:    ')
            try:
                rate = float(val)
            except ValueError:
                print(f"Error: {val} is not a number!")
                continue

            self.rate_of_purchase = rate
            self.amount = self.purchased_quantity * rate
            print("Rate Entered!")
            break

    def update_stock(self, qty):

        if self.product_id == Inventory.products['Product_ID'][0]:
            Inventory.products['Stock']['Iron Rods'] += qty
        elif self.product_id == Inventory.products['Product_ID'][1]:
            Inventory.products['Stock']['Nails'] += qty
        elif self.product_id == Inventory.products['Product_ID'][2]:
            Inventory.products['Stock']['Steel Pipes'] += qty
        elif self.product_id == Inventory.products['Product_ID'][3]:
            Inventory.products['Stock']['Angle Bars'] += qty
        elif self.product_id == Inventory.products['Product_ID'][4]:
            Inventory.products['Stock']['Binding Wire'] += qty

    def new_purchase(self):

        self.prod_id()

        self.pur_qty()

        self.pur_rate()

        self.set_id()

        add_list = [self.purchase_id, self.product_id, self.purchased_quantity, self.rate_of_purchase,\
         self.amount, self.purchase_date, self.purchase_time]

        self.last_added = add_list
        print(self.last_added)
        self.all_added.append(self.last_added)
        print(self.all_added)
        return print("\n\nOne Purchase added!")


    def clear_last_entry(self):
        if len(self.last_added) > 0:
            self.last_added.clear()
        if len(self.all_added) > 0:
            rec = self.all_added.pop()
            print(f"{rec}\nHas Been Deleted!")
        else:
            print('\n\nNo new record to delete!')


    def commit_to_file(self):
        file = "C:\\Users\\welcome\\Desktop\\Transapp\\purchases.txt"

        handle = open(file, 'a')

        #order_of_col: Purchase_Date, Purchase_Time, Product_ID, Purchase_Quantity, Rate_of_Purchase, Amount
        text = f"\n{[new for new in self.all_added]}"

        handle.write(text)

        handle.close()

        print('\n\nPurchase Details Saved!')
