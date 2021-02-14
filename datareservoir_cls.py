import string
import datetime
from datetime import datetime, date, time

class DataReservoir:

    # INVENTORY DATABASE
    inventory = {'Product_ID': [1, 2, 3, 4, 5], 'Product_Name': ['Iron Rods', 'Nails', 'Steel Pipes', 'Angle Bars', 'Binding Wire'], 'Stock': {'Iron Rods': 0, 'Nails': 0, 'Steel Pipes': 0, 'Angle Bars': 0, 'Binding Wire': 0}}

    # PURCHASES DATABASE
    purchases = {'Purchase_Date': [], 'Purchase_Time': [], 'Purchase_ID': [], 'Product_ID': [], 'Purchased_Quantity': [], 'Rate_of_Purchase': [], 'Amount': []}

    # CUSTOMER DATABASE
    customers = {'Customer_ID': [], 'First_Name': [], 'Last_Name': [], 'Gender': [], 'Date_of_Birth': [], 'Birthday': [], 'Country': [], 'Region': [], 'Office_Address': [], 'Date_Opened': [], 'Time_Opened': []}

    # ACCOUNTS DATABASE
    accounts = {'Transaction_Date': [], 'Transaction_Time': [], 'Account_ID': [], 'Customer_ID': [], 'Debit': [], 'Credit': [], 'Balance': []}

    #SALES DATABASE
    sales = {'Order_Date': [], 'Order_Time': [], 'Order_ID': [], 'Product_ID': [], 'Customer_ID': [], 'Ordered_Quantity': [], 'Rate': [], 'Amount_Due': [], 'Amount_Deposited': [], 'Payment_Status': [], 'Date_of_Completion': []}
