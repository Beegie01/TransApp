from datareservoir_cls import *

class Inventory(DataReservoir):

    def __init__ (self):
        self.inventory_date = datetime.date(datetime.now())
        self.inventory_time = datetime.time(datetime.now())


    def __str__(self):
        return f"\nSTOCK AS OF {self.inventory_date}, AT {self.inventory_time}:\
        \n{self.inventory['Product_ID'][0]}. {self.inventory['Product_Name'][0]}: {self.inventory['Stock']['Iron Rods']} units\
        \n{self.inventory['Product_ID'][1]}. {self.inventory['Product_Name'][1]}: {self.inventory['Stock']['Nails']} units\
        \n{self.inventory['Product_ID'][2]}. {self.inventory['Product_Name'][2]}: {self.inventory['Stock']['Steel Pipes']} units\
        \n{self.inventory['Product_ID'][3]}. {self.inventory['Product_Name'][3]}: {self.inventory['Stock']['Angle Bars']} units\
        \n{self.inventory['Product_ID'][4]}. {self.inventory['Product_Name'][4]}: {self.inventory['Stock']['Binding Wire']} units"

    def new_prod_id(self):
        p_id = self.inventory['Product_ID'][-1] + 1
        self.inventory['Product_ID'].append(p_id)
        print("New Product ID Entered!")

    def prod_name_inp(self):
        while True:
            val = input('\nProduct Name:   ')

            if val.isdigit():
                print(f'{val} is invalid!')
                continue

            for char in val:
                if char not in string.ascii_letters:
                    counter += 1

            if counter > 0:
                print(f"{val} contains wrong characters!\nPlease use only alphabets")
                continue
            return val.title()

    def new_prod_name(self):
        p_name_inp = self.prod_name_inp()

        self.inventory['Product_Name'].append(p_name_inp)
        print("New Product Name Entered!")

    def stock_qty(self):
        while True:
            val = input('\nStock:   ')
            try:
                qty = float(val)
            except ValueError:
                print(f"Error: {val} is not a number!")
                continue
            return qty

    def prod_prompt(self):

        acc_range = range(1,6)
        prompt = f"What Product Stock Do You Want To Update?\
        \n1 for {self.inventory['Product_Name'][0]}\n2 for {self.inventory['Product_Name'][1]}\
        \n3 for {self.inventory['Product_Name'][2]}\n4 for {self.inventory['Product_Name'][3]}\
        \n5 for {self.inventory['Product_Name'][4]}\nEnter 1-5:    "
        while True:
            val = input(prompt)

            try:
                prd = int(val)
            except ValueError:
                print(f"Error: {val} is not a number!")
                continue

            if prd not in acc_range:
                print(f"{prd} is out of range!")
                continue
        return prd


    def update_stock(self, inp):
        qty = self.stock_qty()

        prod = self.prod_prompt()

        if prod == self.inventory['Product_ID'][0]:
            self.inventory['Stock']['Iron Rods'] += qty
        elif prod == self.inventory['Product_ID'][1]:
            self.inventory['Stock']['Nails'] += qty
        elif prod == self.inventory['Product_ID'][2]:
            self.inventory['Stock']['Steel Pipes'] += qty
        elif prod == self.inventory['Product_ID'][3]:
            self.inventory['Stock']['Angle Bars'] += qty
        elif prod == self.inventory['Product_ID'][4]:
            self.inventory['Stock']['Binding Wire'] += qty

        print("\nStock Updated!")

    def new_inventory(self):

        # Product ID
        self.new_prod_id()

        # Product Name
        self.new_prod_name()

        # Stock
        self.update_stock()

        print("New Inventory Added!")


    def commit_to_file(self):
        file = "C:\\Users\\welcome\\Desktop\\Transapp\\inventory.txt"

        handle = open(file, 'a')

        DELIM = ', '
        # Order of col: Inventory_ID, Product_Name, Stock, Date
        text = f"{DELIM.join(self.inventory['Product_ID'])}, {DELIM.join(self.inventory['Product_Name'])}, {DELIM.join(self.inventory['Stock'])}"

        handle.write(text)

        handle.close()

        print('Inventory Detail Saved!')
