import datetime
from datetime import datetime, date, time
import string
import mydict_funcs as mdf

class Inventory:


    products = {'Product_ID': [1, 2, 3, 4, 5], \
    'Product_Name': ['Iron Rods', 'Nails', 'Steel Pipes', 'Angle Bars', 'Binding Wire'], \
    'Stock': {'Iron Rods': 0, 'Nails': 0, 'Steel Pipes': 0, 'Angle Bars': 0, 'Binding Wire': 0}}

    def __init__ (self):
        self.today = datetime.today()
        self.inventory_date = datetime.date(self.today)
        self.inventory_time = datetime.time(self.today)
        self.new_product_id = None
        self.new_product_name = None
        self.new_product_stock = 0
        self.count = 5
        self.last_added = []
        self.all_added = []


    def __str__(self):
        return f"\nSTOCK AS OF {self.inventory_date}, AT {self.inventory_time}:\
        \n{self.products['Product_ID'][0]}. {self.products['Product_Name'][0]}: {self.products['Stock']['Iron Rods']} units\
        \n{self.products['Product_ID'][1]}. {self.products['Product_Name'][1]}: {self.products['Stock']['Nails']} units\
        \n{self.products['Product_ID'][2]}. {self.products['Product_Name'][2]}: {self.products['Stock']['Steel Pipes']} units\
        \n{self.products['Product_ID'][3]}. {self.products['Product_Name'][3]}: {self.products['Stock']['Angle Bars']} units\
        \n{self.products['Product_ID'][4]}. {self.products['Product_Name'][4]}: {self.products['Stock']['Binding Wire']} units\
        \n{self.all_added}"

    def new_prod_id(self):
        self.count += 1
        p_id = self.count

        self.new_product_id = p_id
        self.products['Product_ID'].append(p_id)
        print("\nNew Product ID has been set up!")

    def prod_name_inp(self):
        while True:
            counter = 0

            val = input('\nProduct Name:   ')

            if val.isdigit() or val.title() in self.products['Product_Name']:
                print(f'{val} is invalid!')
                continue

            for char in val:
                if char not in string.printable:
                    counter += 1

            if counter > 0:
                print(f"{val} contains wrong characters!\nPlease use only alphabets")
                continue
            return val.title()

    def new_prod_name(self):
        p_name_inp = self.prod_name_inp()

        self.new_product_name = p_name_inp
        self.products['Product_Name'].append(p_name_inp)
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
        \n1 for {self.products['Product_Name'][0]}\n2 for {self.products['Product_Name'][1]}\
        \n3 for {self.products['Product_Name'][2]}\n4 for {self.products['Product_Name'][3]}\
        \n5 for {self.products['Product_Name'][4]}\nEnter between 1-5:    "

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


    def stock_up(self):
        qty = self.stock_qty()

        #prod = self.prod_prompt()

        #if prod == self.products['Product_ID'][0]:
        self.products['Stock'][self.new_product_name] = qty
        self.new_product_stock += qty

        print("\nStock Updated!")

    def new_inventory(self):

        # Product Name
        self.new_prod_name()

        # Stock
        self.stock_up()

        # Product ID
        self.new_prod_id()

        add_list = [self.new_product_id, self.new_product_name, self.new_product_stock, str(self.inventory_date), str(self.inventory_time)]

        self.last_added = add_list
        print(self.last_added)
        self.all_added.append(self.last_added)
        print(self.all_added)
        print("\nNew Inventory Added!")

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
            self.products['Product_Name'].pop()
            print(f"{rec}\nHas Been Deleted!")
        else:
            print('\n\nNo new record to delete!')


    def commit_to_file(self):
        file = "C:\\Users\\welcome\\Desktop\\Transapp\\inventory.txt"

        handle = open(file, 'a')

        # Order of col: {row_num: [Inventory_ID, Product_Name, Stock, Date]}
        text = f"\n{str(mdf.index_row(self.all_added))}"

        # Ensuring that empty rows are not saved
        if len(self.all_added) > 0:

            handle.write(text)

            handle.close()

            print('\n\nNew Inventory Details Saved!')

        else:
            print("\n\nNo New Record To Save!")
