def welc_scr():
    '''
    this is the start of the app
    '''

    print('WELCOME')
    print('TO')
    print('SAGE ABE')
    print('TRANSACTIONS')
    print('APP')
    print('PROJECT')
    print('**************************')
    print('THE')
    print('TRANS')
    print('APP')
    print('**************************')
    print('FEBRUARY\n2021')
    print('**************************')
    print()

def player_decide():
    '''
    user chooses what to do from 3 options
    '''
    print('\n'*5)

    next = '_null_'
    accepted_range = ['c', 'i', 'p', 'a', 's']
    prompt = "Please enter 'c' for customers,\
    \n'i' for inventory,\
    \n'a' for accounts, \
    \n's' for sales,\
    \n'p' for purchases:        "

    while (next == '_null_') or next.isdigit() or (next.lower() not in accepted_range):
    	next = input(prompt)

    	#Error message 1
    	if next.isdigit():
    		print(f"{next} is an invalid choice.")
    		continue
    	#Error message 2
    	elif next.lower() not in accepted_range:
    		print(f"{next} is out of range.\
    		\nEnter 'a', 'c', 's', 'i', or 'p'.")
    		continue

    return next.lower()


def ask_inp():
    acc_range = ['yes', 'y', 'no', 'n']
    while True:
        inp = input("\nTo add more enter yes \nTo stop enter no\n")

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
    while True:
        val = input("\nPress Enter to continue, or 'e' to exit game:\n")

        acc_range = ['', 'e', 'exit']
        if val.lower() not in acc_range:
            print(f"\n{val} is not valid!")
            continue
        else:
            if val.lower() == '':
                '\n'
                return True
            elif val.lower() in ['e', 'exit']:
                return exit_play()

def exit_play():
    print(f"\n\nThanks for playing!")
    quit()


def app_menu(customer_obj, purchase_obj, sales_obj, accounts_obj, inventory_obj):
	'''
	here player chooses an avatar and decides on who goes first
	'''
	print("\n"*5)
	print("****TRANSACTIONS APP****")
	print("\n"*5,"**************2021************")
	print("\n"*5,"To visit the inventory section, enter 'i'.\
	\nTo visit the customer section, enter 'c'.\
	\nTo visit the accounts section, enter 'a'.\
    \nTo visit the sales section, enter 's'.\
    \nTo visit the purchases section, enter 'p'.")

	decision = player_decide()

	if decision == 'i':
		inventory_scr(inventory_obj)

	elif decision == 'c':
		customers_scr(customer_obj)

	elif decision == 'p':
		purchases_scr(purchase_obj)

	elif decision == 'a':
		acct_scr(accounts_obj)

	elif decision == 's':
		sales_scr(sales_obj)



# inventory functions
def inventory_inp():

    CONSTANT = 'inventory'

    prompt = f"\nTo add new {CONSTANT} records, enter 'n'.\
    \nTo save new {CONSTANT} records, enter 's'\
    \nTo view updates, enter 'v'\
    \nTo return to menu, press enter ''\
    \nTo exit, enter 'e'\n"

    acc_range = ['n', 'e', 's', 'v', '']

    while True:
        inp = input(prompt)

        if inp.lower() not in acc_range:
            print(f"Error: Invalid entry!\n{inp} is out of range")
            continue
        return inp.lower()

def inventory_scr(inventory_obj):
    ans = inventory_inp()
    if ans == 'n':
        adding_inventory(inventory_obj)

    elif ans == 's':
        commit_inv_data(inventory_obj)

    elif ans == 'v':
        print(inventory_obj)

    elif ans == '':
        pass

    elif ans == 'e':
        exit_play()

def adding_inventory(inventory_obj):
    # enter new customer details
    ADDING = True
    while ADDING:
        inventory_obj.new_customer()

        if add_more():
            continue
        else:
            to_menu()
            ADDING = False

def commit_inv_data(inventory_obj):
    # save new customer entries
    inventory_obj.commit_to_file()



# customers functions
def customers_inp():
    CONSTANT = 'customer'

    prompt = f"\nTo add new {CONSTANT} records, enter 'n'.\
    \nTo save new {CONSTANT} records, enter 's'\
    \nTo view updates, enter 'v'\
    \nTo return to menu, press enter ''\
    \nTo exit, enter 'e'\n"

    acc_range = ['n', 'e', 's', 'v', '']

    while True:
        inp = input(prompt)

        if inp.lower() not in acc_range:
            print(f"Error: Invalid entry!\n{inp} is out of range")
            continue
        return inp.lower()

def customers_scr(customer_obj):
    ans = customers_inp()
    if ans == 'n':
        adding_customers(customer_obj)

    elif ans == 's':
        commit_cust_data(customer_obj)

    elif ans == 'v':
        print(customer_obj)

    elif ans == '':
        pass

    elif ans == 'e':
        exit_play()


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
def purchase_inp():

    CONSTANT = 'purchase'

    prompt = f"\nTo add new {CONSTANT} records, enter 'n'.\
    \nTo save new {CONSTANT} records, enter 's'\
    \nTo view updates, enter 'v'\
    \nTo return to menu, press enter ''\
    \nTo exit, enter 'e'\n"

    acc_range = ['n', 'e', 's', 'v', '']
    while True:
        inp = input(prompt)

        if inp.lower() not in acc_range:
            print(f"Error: Invalid entry!\n{inp} is out of range")
            continue
        return inp.lower()

def purchase_scr(purchase_obj):
    ans = purchase_inp()
    if ans == 'n':
        adding_purchases(purchase_obj)

    elif ans == 's':
        commit_pur_data(purchase_obj)

    elif ans == 'v':
        print(purchase_obj)

    elif ans == '':
        pass

    elif ans == 'e':
        exit_play()

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
def sales_inp():

    CONSTANT = 'sales'

    prompt = f"\nTo add new {CONSTANT} records, enter 'n'.\
    \nTo save new {CONSTANT} records, enter 's'\
    \nTo view updates, enter 'v'\
    \nTo return to menu, press enter ''\
    \nTo exit, enter 'e'\n"

    acc_range = ['n', 'e', 's', 'v', '']

    while True:
        inp = input(prompt)

        if inp.lower() not in acc_range:
            print(f"Error: Invalid entry!\n{inp} is out of range")
            continue
        return inp.lower()

def sales_scr(sales_obj):
    ans = sales_inp()
    if ans == 'n':
        adding_saless(sales_obj)

    elif ans == 's':
        commit_sales_data(sales_obj)

    elif ans == 'v':
        print(sales_obj)

    elif ans == '':
        pass

    elif ans == 'e':
        exit_play()

def adding_saless(sales_obj):
    # enter new customer details
    ADDING = True
    while ADDING:
        sales_obj.new_order()

        if add_more():
            continue
        else:
            ADDING = False

def commit_sales_data(sales_obj):
    # save new customer entries
    sales_obj.commit_to_file()




# accts functions
def acct_inp():

    CONSTANT = 'acct'

    prompt = f"\nTo add new {CONSTANT} records, enter 'n'.\
    \nTo save new {CONSTANT} records, enter 's'\
    \nTo view updates, enter 'v'\
    \nTo return to menu, press enter ''\
    \nTo exit, enter 'e'\n"

    acc_range = ['n', 'e', 's', 'v', '']

    while True:
        inp = input(prompt)

        if inp.lower() not in acc_range:
            print(f"Error: Invalid entry!\n{inp} is out of range")
            continue
        return inp.lower()

def acct_scr(accounts_obj):
    ans = acct_inp()
    if ans == 'n':
        adding_accts(accounts_obj)

    elif ans == 's':
        commit_acct_data(accounts_obj)

    elif ans == 'v':
        print(accounts_obj)

    elif ans == '':
        pass

    elif ans == 'e':
        exit_play()

def adding_accts(accounts_obj):
    # enter new customer details
    ADDING = True
    while ADDING:
        accounts_obj.new_transaction()

        if add_more():
            continue
        else:
            ADDING = False

def commit_acct_data(accounts_obj):
    # save new customer entries
    accounts_obj.commit_to_file()
