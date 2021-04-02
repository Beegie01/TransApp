from colorama import init, Back, Fore
init()


def welc_scr():
    '''
    this is the start of the app
    '''
    print('\n'*10,\
    Back.LIGHTWHITE_EX, Fore.CYAN+\
    '\n**************************\
    \nWELCOME\nTO\nSAGE ABE\nTRANSACTIONS\nAPP\nPROJECT', \
    '\n**************************', '\n'*5,\
    '\n**************************\nTHE\nTRANS\nAPP\
    \nFEBRUARY\n2021\n**************************', Back.RESET, Fore.RESET)


def player_decide():
    '''
    user chooses what to do from available options
    '''
    print('\n'*5)

    next = '_null_'
    accepted_range = ['c', 'i', 'p', 'a', 's', 'e']

    print("\n"*5)
    print(Back.LIGHTWHITE_EX, Fore.CYAN)
    print(" MAIN\n TRANSAPP\n MENU")
    prompt = "\n'c' for customers,\
    \n'i' for inventory,\
    \n'a' for accounts, \
    \n's' for sales,\
    \n'p' for purchases\
    \n'e' for exit\n"

    while (next == '_null_') or next.isdigit() or (next.lower() not in accepted_range):
    	next = input(prompt)

    	#Error message 1
    	if next.isdigit():
    		print(f"{next} is an invalid choice.")
    		continue
    	#Error message 2
    	elif next.lower() not in accepted_range:
    		print(f"{next} is out of range.\
    		\nEnter 'a', 'c', 's', 'i', 'p', or 'e'")
    		continue

    return next.lower()


def ask_inp():
    prompt = "\nTo add more enter yes \nTo stop enter no"
    acc_range = ['yes', 'y', 'no', 'n']
    while True:
        inp = input(prompt)

        if inp.lower() not in acc_range:
            print(f'Error: {inp} is invalid!')
            continue
        return inp.lower()

def add_more():
    ans = ask_inp()
    if ans in ['yes', 'y']:
        return True
    elif ans in ['no', 'n']:
        return False

def play_on():
    response = quick_check()
    if response:
        pass

def quick_check():
    print("\n", Back.LIGHTWHITE_EX + Fore.GREEN + "Press Enter to continue, or 'e' to exit game:", Back.RESET, Fore.RESET)
    prompt = "\n"
    while True:
        val = input(prompt)

        acc_range = ['', 'e', 'exit']
        if val.lower() not in acc_range:
            print(f"\n{val} is not valid!")
            continue
        else:

            if val.lower() == '':
                '\n'
                break

            elif val.lower() in ['e', 'exit']:
                return exit_play()

def exit_play():
    print(Fore.RED, f"\n\nTRANSAPP CLOSING\n\nThanks for using TransApp!", Fore.RESET)
    quit()

def app_menu(customer_obj, purchase_obj, sales_obj, accounts_obj, inventory_obj):
	'''
	here player chooses an avatar and decides on who goes first
	'''

	print("\n"*25, Back.LIGHTWHITE_EX, Fore.CYAN,"\
    \nTo visit the inventory section, enter 'i'.\
	\nTo visit the customer section, enter 'c'.\
	\nTo visit the accounts section, enter 'a'.\
    \nTo visit the sales section, enter 's'.\
    \nTo visit the purchases section, enter 'p'.\
    \nTo exit, enter 'e'.")

	decision = player_decide()

	if decision == 'i':
		inventory_scr(inventory_obj)

	elif decision == 'c':
		customers_scr(customer_obj)

	elif decision == 'p':
		purchase_scr(purchase_obj)

	elif decision == 'a':
		acct_scr(accounts_obj)

	elif decision == 's':
		sales_scr(sales_obj)

	elif decision == 'e':
		exit_play()


# inventory functions
def inventory_scr(inventory_obj):
    print(Back.LIGHTWHITE_EX, Fore.MAGENTA)
    while True:
        print("\n"*5, "INVENTORY RECORD\n\tMENU")
        # inventory menu
        ans = inventory_inp()

        if ans == 'n':
            adding_inventory(inventory_obj)
            continue

        elif ans == 's':
            commit_inv_data(inventory_obj)
            continue

        elif ans == 'v':
            inventory_obj.view_rec()
            play_on()

        elif ans == 'd':
            inventory_obj.clear_last_entry()
            continue

        elif ans == 'b':
            break

        elif ans == 'e':
            exit_play()


def inventory_inp():

    CONSTANT = 'inventory'

    prompt = f"\nTo add new {CONSTANT} records, enter 'n'.\
    \nTo save added {CONSTANT} records, enter 's'\
    \nTo view added records, enter 'v'\
    \nTo delete added records, enter 'd'\
    \nTo return to the main menu, enter 'b'\
    \nTo exit, enter 'e'\n"

    acc_range = ['n', 'e', 's', 'v', 'd', 'b']

    while True:
        inp = input(prompt)

        if inp.lower() not in acc_range:
            print(f"Error: Invalid entry!\n{inp} is out of range")
            continue
        return inp.lower()

def adding_inventory(inventory_obj):
    # enter new customer details
    ADDING = True
    while ADDING:
        inventory_obj.new_inventory()

        if add_more():
            continue
        else:
            ADDING = False

def commit_inv_data(inventory_obj):
    # save new customer entries
    inventory_obj.commit_to_file()



# customers functions
def customers_scr(customer_obj):

    print(Back.LIGHTWHITE_EX, Fore.BLUE)
    while True:
        print("\n"*5, "CUSTOMER RECORD\n\tMENU")
        ans = customers_inp()

        if ans == 'n':
            adding_customers(customer_obj)
            continue

        elif ans == 's':
            commit_cust_data(customer_obj)
            continue

        elif ans == 'v':
            customer_obj.view_rec()
            play_on()

        elif ans == 'd':
            customer_obj.clear_last_entry()
            continue

        elif ans == 'b':
            break

        elif ans == 'e':
            exit_play()


def customers_inp():
    CONSTANT = 'customer'

    prompt = f"\nTo add new {CONSTANT} records, enter 'n'.\
    \nTo save added {CONSTANT} records, enter 's'\
    \nTo view added records, enter 'v'\
    \nTo delete added records, enter 'd'\
    \nTo return to the main menu, enter 'b'\
    \nTo exit, enter 'e'\n"

    acc_range = ['n', 'e', 's', 'v', 'd', 'b']

    while True:
        inp = input(prompt)

        if inp.lower() not in acc_range:
            print(f"Error: Invalid entry!\n{inp} is out of range")
            continue
        return inp.lower()


def adding_customers(customer_obj):
    # enter new customer details
    ADDING = True
    while ADDING:
        customer_obj.new_customer()

        if add_more():
            continue
        else:
            ADDING = False

def commit_cust_data(customer_obj):
    # save new customer entries
    customer_obj.commit_to_file()





# purchases functions
def purchase_scr(purchase_obj):
    print(Back.LIGHTWHITE_EX, Fore.YELLOW)
    while True:
        print("\n"*5, "PURCHASE RECORD\n\tMENU")
        ans = purchase_inp()

        if ans == 'n':
            adding_purchases(purchase_obj)
            continue

        elif ans == 's':
            commit_pur_data(purchase_obj)
            continue

        elif ans == 'v':
            purchase_obj.view_rec()
            play_on()

        elif ans == 'd':
            purchase_obj.clear_last_entry()
            continue

        elif ans == 'b':
            break

        elif ans == 'e':
            exit_play()

def purchase_inp():

    CONSTANT = 'purchase'

    prompt = f"\nTo add new {CONSTANT} records, enter 'n'.\
    \nTo save added {CONSTANT} records, enter 's'\
    \nTo view added records, enter 'v'\
    \nTo delete added records, enter 'd'\
    \nTo return to the main menu, enter 'b'\
    \nTo exit, enter 'e'\n"

    acc_range = ['n', 'e', 's', 'v', 'd', 'b']
    while True:
        inp = input(prompt)

        if inp.lower() not in acc_range:
            print(f"Error: Invalid entry!\n{inp} is out of range")
            continue
        return inp.lower()

def adding_purchases(purchase_obj):
    # enter new customer details
    ADDING = True
    while ADDING:
        purchase_obj.new_purchase()

        if add_more():
            continue
        else:
            ADDING = False

def commit_pur_data(purchase_obj):
    # save new customer entries
    purchase_obj.commit_to_file()




# saless functions
def sales_scr(sales_obj):

    print(Back.LIGHTWHITE_EX, Fore.LIGHTGREEN_EX)
    while True:
        print("\n"*5, "SALES RECORD\n\tMENU")

        ans = sales_inp()

        if ans == 'n':
            adding_saless(sales_obj)
            continue

        elif ans == 's':
            commit_sales_data(sales_obj)
            continue

        elif ans == 'v':
            sales_obj.view_rec()
            play_on()

        elif ans == 'd':
            sales_obj.clear_last_entry()
            continue

        elif ans == 'b':
            break

        elif ans == 'e':
            exit_play()


def sales_inp():

    CONSTANT = 'sales'

    prompt = f"\nTo add new {CONSTANT} records, enter 'n'.\
    \nTo save added {CONSTANT} records, enter 's'\
    \nTo view added records, enter 'v'\
    \nTo delete added records, enter 'd'\
    \nTo return to the main menu, enter 'b'\
    \nTo exit, enter 'e'\n"

    acc_range = ['n', 'e', 's', 'v', 'd', 'b']

    while True:
        inp = input(prompt)

        if inp.lower() not in acc_range:
            print(f"Error: Invalid entry!\n{inp} is out of range")
            continue
        return inp.lower()


def adding_saless(sales_obj):
    # enter new customer details
    ADDING = True
    while ADDING:
        sales_obj.new_order()

        if add_more():
            continue
        else:
            play_on()
            ADDING = False


def commit_sales_data(sales_obj):
    # save new customer entries
    sales_obj.commit_to_file()




# accts functions
def acct_scr(accounts_obj):

    print(Back.LIGHTWHITE_EX, Fore.GREEN)
    while True:
        print("\n"*5, "ACCOUNT RECORD\n\t MENU")

        ans = acct_inp()

        if ans == 'n':
            adding_accts(accounts_obj)
            continue

        elif ans == 's':
            commit_acct_data(accounts_obj)
            continue

        elif ans == 'v':
            accounts_obj.view_rec()
            play_on()

        elif ans == 'd':
            accounts_obj.clear_last_entry()
            continue

        elif ans == 'b':
            break

        elif ans == 'e':
            exit_play()


def acct_inp():

    CONSTANT = 'acct'

    prompt = f"\nTo add new {CONSTANT} records, enter 'n'.\
    \nTo save added {CONSTANT} records, enter 's'\
    \nTo view added records, enter 'v'\
    \nTo delete added records, enter 'd'\
    \nTo return to the main menu, enter 'b'\
    \nTo exit, enter 'e'\n"

    acc_range = ['n', 'e', 's', 'v', 'b', 'd']

    while True:
        inp = input(prompt)

        if inp.lower() not in acc_range:
            print(f"Error: Invalid entry!\n{inp} is out of range")
            continue
        return inp.lower()


def adding_accts(accounts_obj):
    # enter new customer details
    ADDING = True
    while ADDING:
        accounts_obj.new_transaction()

        if add_more():
            continue
        else:
            play_on()
            ADDING = False

def commit_acct_data(accounts_obj):
    # save new customer entries
    accounts_obj.commit_to_file()
