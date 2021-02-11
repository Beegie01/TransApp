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

def adding_customers(customer_obj):
    # enter new customer details
    ADDING = True
    while ADDING:
        customer_obj.new_customer()

        if add_more():
            continue
        else:
            ADDING = False

def adding_purchases(purchase_obj):
    # enter new customer details
    ADDING = True
    while ADDING:
        purchase_obj.new_purchase()

        if add_more():
            continue
        else:
            ADDING = False

def play_on():
    response = self.quick_check()
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
                return self.exit_play()

def exit_play():
    print(f"\n\nThanks for playing!")
    quit()
