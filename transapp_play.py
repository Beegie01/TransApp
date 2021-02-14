from inventory_cls import *
from datareservoir_cls import *
from customer_cls import *
from accounts_cls import *
from purchase_cls import *
from sales_cls import *
from transapp_funcs import *


# welcome screen
welc_scr()

# create datareservoir object
data = DataReservoir()
# create inventory object
inventory_today = Inventory()

# create new purchase object
purchases_today = Purchase()

# create new customer object
customers_today = Customer()

# create new order object
sales_today = Sales()

# create a new transaction object
transact_today = Accounts()

running_app = True

while running_app:
    # enter new customer details
    app_menu(customers_today, purchases_today, sales_today, transact_today, inventory_today)

    play_on()
