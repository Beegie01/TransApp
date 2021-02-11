import string
import datetime
from datetime import datetime, date, time

class DataReservoir:

    # INVENTORY DATABASE
    inventory = {'Product_ID': [], 'Product_Name': [], 'Stock': []}

    # PURCHASES DATABASE
    purchases = {'Purchase_Date': [], 'Purchase_Time': [], 'Purchase_ID': [], 'Product_ID': [], 'Purchased_Quantity': [], 'Rate_of_Purchase': [], 'Amount': []}

    # CUSTOMER DATABASE
    customers = {'Customer_ID': [], 'First_Name': [], 'Last_Name': [], 'Gender': [], 'Date_of_Birth': [], 'Birthday': [], 'Country': [], 'Region': [], 'Office_Address': [], 'Date_Opened': [], 'Time_Opened': []}

    # ACCOUNTS DATABASE
    accounts = {'Transaction_Date': [], 'Transaction_Time': [], 'Account_ID': [], 'Customer_ID': [], 'Debit': [], 'Credit': [], 'Balance': []}

    #SALES DATABASE
    sales = {'Order_Date': [], 'Order_Time': [], 'Order_ID': [], 'Product_ID': [], 'Customer_ID': [], 'Ordered_Quantity': [], 'Rate': [], 'Amount_Due': [], 'Amount_Deposited': [], 'Payment_Status': [], 'Date_of_Completion': []}



class Inventory(DataReservoir):

    products = ['Iron Rods', 'Nails', 'Steel Pipes', 'Angle Bars', 'Binding Wire']
    inventory_date = datetime.date(datetime.now())
    inventory_time = datetime.time(datetime.now())
    rods = {'name': products[0], 'ID': 1, 'stock': 0}
    nails = {'name': products[1], 'ID': 2, 'stock': 0}
    pipes = {'name': products[2], 'ID': 3, 'stock': 0}
    angles = {'name': products[3], 'ID': 4, 'stock': 0}
    bwires = {'name': products[4], 'ID': 5, 'stock': 0}



    def __str__(self):
        return f"\nSTOCK AS OF {self.inventory_date}:\
        \n{self.rods['ID']}. {self.rods['name']}: {self.rods['stock']} units\
        \n{self.nails['ID']}. {self.nails['name']}: {self.nails['stock']} units\
        \n{self.pipes['ID']}. {self.pipes['name']}: {self.pipes['stock']} units\
        \n{self.angles['ID']}. {self.angles['name']}: {self.angles['stock']} units\
        \n{self.bwires['ID']}. {self.bwires['name']}: {self.bwires['stock']} units"

    def store_inventory(self):
        self.inventory['Product_ID'].extend([self.rods['ID'], self.nails['ID'], self.pipes['ID'], self.angles['ID'], self.bwires['ID']])
        self.inventory['Product_Name'].extend([self.rods['name'], self.nails['name'], self.pipes['name'], self.angles['name'], self.bwires['name']])
        self.inventory['Stock'].append(sum(self.purchases['Purchase_Quantity']) - sum(self.sales['Order_Quantity']))


    def save_row_to_file(self):
        file = "C:\\Users\\welcome\\Desktop\\Transapp\\inventory.txt"

        handle = open(file, 'a')

        # Order of col: Inventory_ID, Product_Name, Stock, Date
        text = f"{self.rods['ID']}, {self.rods['name']}, {self.rods['stock']}, {self.inventory_date}\
        \n{self.nails['ID']}, {self.nails['name']}, {self.nails['stock']}, {self.inventory_date}\
        \n{self.pipes['ID']}, {self.pipes['name']}, {self.pipes['stock']}, {self.inventory_date}\
        \n{self.angles['ID']}, {self.angles['name']}, {self.angles['stock']}, {self.inventory_date}\
        \n{self.bwires['ID']}, {self.bwires['name']}, {self.bwires['stock']}, {self.inventory_date}"

        handle.write(text)

        handle.close()
