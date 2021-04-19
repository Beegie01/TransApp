import tkinter as tk, datetime, random, os, string, re, itertools
from tkinter import messagebox, scrolledtext, ttk
from inventory_cls import Inventory
from customer_cls import Customer
from account_cls import Account, AcctTrans
from sales_cls import Sales
from user_login import User


dir_path = 'C:\\Users\\welcome\\Desktop\\MyFuncs'

if dir_path not in os.sys.path:
    os.sys.path.append(dir_path)

from mydict_funcs import del_item

eme, pe = None, None


class TransApp:
    # create general folder for users' data
    #  make each folder a package by
    # creating an initialize file for each of our folders at specified path
    with open(f'{os.getcwd()}\\__init__.py', 'w', encoding='utf8') as hand:
        hand.writelines('')
    os.makedirs(f'{os.getcwd()}\\TransAppUsers', exist_ok=True)

    def __init__(self, master): #, inventory_obj, customer_obj, sales_obj):
        self.master = master
        # user login 
        self.login_user = User()
        # create initialize file for python at specified path
        with open(f'{self.login_user.dir_path}\\__init__.py', 'w', encoding='utf8') as hand:
            hand.writelines('')
        # create an object of inventory
        self.inv_obj = Inventory()
        # create an object of customer
        self.cust_obj = Customer()
        # create an object of account
        self.acct_obj = Account()
        # create an object of customers account transactions
        self.acctrans_obj = AcctTrans()
        # create an object of sales
        self.sales_obj = Sales()
        

        # menu bar section
        self.menu_bar = tk.Menu(self.master)
        main_menu = tk.Menu(self.menu_bar, tearoff=0)
        main_menu.add_command(label="HOME", command=lambda: self.menupage(event=None))
        main_menu.add_command(label="SIGN OUT", command=lambda: self.firstpage(event=None))
        main_menu.add_command(label="EXIT", command=lambda: self.master.destroy())
        self.menu_bar.add_cascade(menu=main_menu, label='MENU')

        # status bar frame
        self.status_bar_frame = None

        # frame for front page containing one row and one column
        self.introFrame = None

        # frame for menu page containing four rows and one column
        self.homeFrame = None

        # frame for inventory page containing three rows and one column
        self.sectionFrame = None

        # frame for input of new inventory
        self.new_frame = None

        # frame for submission status
        self.submit_frame = None

        self.display_frame = None

        self.edit_frame = None
        
        # list of entries
        self.day = list(range(1, 32))
        self.month = {1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUN', 7: 'JUL', 8: 'AUG',
                      9: 'SEP', 10: 'NOV', 12: 'DEC'}
        self.year = list(range(1900, 2022))

    def setup_frames(self):
        # status bar frame
        self.status_bar_frame = tk.LabelFrame(master=self.master, bg='gold')
        self.status_bar_frame.rowconfigure(0, weight=1)
        self.status_bar_frame.columnconfigure([0, 1, 2, 3, 4], weight=1)
        self.status_bar_frame.grid(row=0, column=0, columnspan=5, sticky='we')

        # frame for front page containing one row and one column
        self.introFrame = tk.Frame(master=self.master, bg='GOLD')
        self.introFrame.rowconfigure(0, weight=1)
        self.introFrame.columnconfigure(0, weight=1)
        self.introFrame.focus()
        self.introFrame.bind('<Return>', self.firstpage)

        # frame for menu page containing four rows and one column
        self.homeFrame = tk.LabelFrame(master=self.master, text='HOME', fg='black', font=('arial black', 12))
        self.homeFrame.rowconfigure([0, 1, 2, 3], weight=1)
        self.homeFrame.columnconfigure(0, weight=1)

        # frame for inventory page containing three rows and one column
        self.sectionFrame = tk.LabelFrame(master=self.master, text='INVENTORY', font=('arial black', 12), bg='purple',
                                      fg='white')
        self.sectionFrame.rowconfigure([0, 1, 2, 3], weight=1)
        self.sectionFrame.columnconfigure(0, weight=1)

        # frame for input of new inventory
        self.new_frame = tk.LabelFrame(self.master, text='NEW PRODUCT', fg='white', font=('arial black', 12),
                                            bg='purple')
        self.new_frame.rowconfigure(list(range(4)), weight=1)
        self.new_frame.columnconfigure(list(range(3)), weight=1)

        # frame for submission status
        self.submit_frame = tk.LabelFrame(self.master, text='DO YOU WANT TO SAVE?', fg='white',
                                          font=('arial black', 12), bg='purple')
        self.submit_frame.rowconfigure([0, 1], weight=1)
        self.submit_frame.columnconfigure(0, weight=1)

        self.edit_frame = tk.LabelFrame(self.master, font=('arial black', 12), bg='purple')
        self.edit_frame.rowconfigure(0, weight=1)
        self.edit_frame.columnconfigure(0, weight=1)

    def make_frame(self, page_title=None, background_color='purple', foreground_color='white'):
        # specify the frame text, fg, bg
        return tk.LabelFrame(self.master, text=page_title, bg=background_color, fg=foreground_color, font=('arial black', 12))

    def setup_status_bar(self):
        # status bar
        tk.Label(master=self.status_bar_frame, font=('arial black', 10), fg='black', bg='gold',
                                    text=f"{datetime.datetime.date(datetime.datetime.today())}"
                 ).grid(row=0, column=4, sticky='ew')
        tk.Label(master=self.status_bar_frame, font=('arial black', 10), fg='black', bg='gold',
                 text="TransApp-2021").grid(row=0, column=3, sticky='nsew')
        
    def firstpage(self, event):

        self.display_frame = tk.LabelFrame(master=self.master, text='SETUP', bg='gold', font=('arial black', 12))

        menu = tk.Menu()

        self.master.config(menu=menu)

        # status bar frame
        # make status bar reflect logged in user name
        tk.Label(master=self.status_bar_frame, font=('arial black', 10), fg='black', bg='gold',
                 text="").grid(row=0, column=0, sticky='nsew')

        # signup button
        tk.Button(self.display_frame, text='New User', bg='green', fg='white', command=self.signup_page).grid(row=0,
                                                                                                      columnspan=3,
                                                                                                      padx=60, pady=5,
                                                                                                      sticky='nsew')

        # login button
        tk.Button(self.display_frame, text='Existing User', bg='blue', fg='white', command=self.loginpage).grid(row=1,
                                                                                                        columnspan=3,
                                                                                                        padx=40, pady=5,
                                                                                                        sticky='nsew')

        # exit button
        tk.Button(self.display_frame, text='Exit App', bg='red', fg='white', command=self.master.destroy).grid(row=2,
                                                                                                       columnspan=3,
                                                                                                       padx=20, pady=5,
                                                                                                       sticky='nsew')
        if self.display_frame is not None:
            self.display_frame.grid_forget()
        if self.introFrame is not None:
            self.introFrame.grid_forget()

        self.display_frame.rowconfigure(list(range(3)), weight=1)
        self.display_frame.columnconfigure(list(range(3)), weight=1)
        self.display_frame.grid(row=1, rowspan=4, column=0, columnspan=5, sticky='nsew')

    def signup_page(self):
        global eme, pe, cpe, ce
        # set up frame
        self.display_frame = tk.LabelFrame(master=self.master, text='CREATE NEW USER', bg='gold', font=('arial black', 12))

        tk.Label(self.display_frame, text='Company Name', fg='black', bg='gold', font=('calibri', 13, 'bold')
                 ).grid(row=0, sticky='e')
        ce = tk.Entry(self.display_frame, font=('calibri', 14, 'bold'), width=60)
        ce.grid(row=0, column=1, sticky='w', padx=3, pady=5)

        tk.Label(self.display_frame, text='Email', fg='black', bg='gold', font=('calibri', 12, 'bold')).grid(row=1, sticky='e')
        eme = tk.Entry(self.display_frame, font=('calibri', 12), width=30)
        eme.grid(row=1, column=1, sticky='w', padx=3, pady=5)

        tk.Label(self.display_frame, text='Password', fg='black', bg='gold', font=('calibri', 12, 'bold')).grid(row=3,
                                                                                                        sticky='e')
        pe = tk.Entry(self.display_frame, font=('calibri', 12), show='*', width=30)
        pe.grid(row=3, column=1, sticky='w', padx=3, pady=5)

        # radio button to show and hide password entries
        passw = tk.BooleanVar(self.display_frame)
        passw.set(False)
        tk.Checkbutton(self.display_frame, text='Show Password', fg='black', bg='gold', font=('calibri', 10, 'bold'),
                       variable=passw, command=lambda: self.showpassword(passw.get())).grid(row=2, column=1, sticky='sw')

        tk.Label(self.display_frame, text='Confirm Password', fg='black', bg='gold', font=('calibri', 12, 'bold')
                 ).grid(row=4, sticky='e')
        cpe = tk.Entry(self.display_frame, font=('calibri', 12), show='*', width=30)
        cpe.grid(row=4, column=1, sticky='w', padx=3, pady=5)

        # submit signup button
        ttk.Button(self.display_frame, text='Create User',  width=15,
                   command=self.setattr).grid(row=6, column=1, sticky='e')

        # front page
        ttk.Button(self.display_frame, text='Back', width=8, command=self.firstpage).grid(row=6, column=0, sticky='e')

        self.display_frame.rowconfigure(list(range(6)), weight=1)
        self.display_frame.columnconfigure(list(range(3)), weight=1)
        self.display_frame.grid(row=1, rowspan=4, column=0, columnspan=5, sticky='nsew')

    def showpassword(self, entry):
        # print(type(entry), entry)
        global pe, cpe
        if entry:
            pe.config(show='')
            if cpe is not None:
                cpe.config(show='')
        else:
            pe.config(show='*')
            if cpe is not None:
                cpe.config(show='*')

    def setattr(self):
        global eme, pe, cpe, ce

        email, pwd, confpwd, coy = eme.get(), pe.get(), cpe.get(), ce.get()
        # extract username from email address
        stop = email.find("@")
        user = email[:stop].capitalize()

        # collect all existing usernames into a list
        for path, folders, files in os.walk(self.login_user.dir_path):
            for folder in folders:
                self.login_user.usernames.append(folder)

        # check if password is a match
        if pwd != confpwd:
            return messagebox.showerror(title='Check Password', message='Password does not match')

        mandatory_entries = [email, pwd, coy]
        str_type_entries = [email, coy]

        wspace = string.whitespace
        puncs = string.punctuation

        # check for empty fields
        if [True for entry in mandatory_entries if (entry in wspace)]:
            return messagebox.showerror(title='Blank Field', message='BLANK FIELD(S) DETECTED!')

        # check for fields with invalid data types
        for entry in str_type_entries:
            try:
                float(entry)
                # figures have been entered, if no error was raised
                return messagebox.showerror(title='Invalid Data Type',
                                            message=f'Number {entry} is not allowed here!')
            except ValueError as VE:
                continue

        # email constraints
        if not (re.findall(r'(.+)@(.+)[.](.+)', email)):  # ('@' not in email) or ('.' not in email):
            return messagebox.showerror(title='INCORRECT EMAIL', message='Incorrect email address'
                                                                         '\n\nPlease EMAIL for @ or .')
        # password length
        if len(pwd) < 5:
            return messagebox.showerror(title='Password too short',
                                        message='Password Must Contain 5 or more characters')

        upper_found, lower_found, punc_found = False, False, False

        # implementing password constraints
        for char in pwd:
            if char.islower() and not (lower_found):
                lower_found = True

            elif char.isupper() and not (upper_found):
                upper_found = True

            elif char in puncs and not (punc_found):
                punc_found = True

        if not (upper_found):
            return messagebox.showerror(title='No Uppercase in Password', message='Password Must Contain Uppercase')

        if not (lower_found):
            return messagebox.showerror(title='No Lowercase in Password', message='Password Must Contain Lowercase')

        if not (punc_found):
            return messagebox.showerror(title='No Symbol in Password', message='Password Must Contain a symbol')

        if user in self.login_user.usernames:
            return messagebox.showerror(title='Username Not Unique', message='Username Already Exists in the Database')

        # after confirm data integrity
        # store variables
        self.login_user.username, self.login_user.password, self.login_user.company_name, self.login_user.email = user, pwd, coy.title(), email.lower()

        # create unique folder for user
        os.mkdir(f'{self.login_user.dir_path}\\{self.login_user.username}')

        self.login_user.filepath = f'{self.login_user.dir_path}\\{self.login_user.username}'

        os.makedirs(f'{self.login_user.filepath}\\Inventory', exist_ok=True)
        os.makedirs(f'{self.login_user.filepath}\\Accounts', exist_ok=True)
        os.makedirs(f'{self.login_user.filepath}\\AccTransactions', exist_ok=True)
        os.makedirs(f'{self.login_user.filepath}\\Customers', exist_ok=True)
        os.makedirs(f'{self.login_user.filepath}\\Sales', exist_ok=True)

        save_obj(self.login_user)

        self.display_frame = tk.LabelFrame(self.master, bg='gold')

        tk.Label(self.display_frame, text=f'New User Created!\n{self.login_user.username}', fg='black', bg='gold',
                 font=('calibri', 12, 'bold')).grid(row=1, columnspan=3, sticky='NSEW')
        ttk.Button(self.display_frame, text="Login Page", command=self.loginpage).grid(row=4, columnspan=3, sticky='ew')

        self.display_frame.rowconfigure(list(range(8)), weight=1)
        self.display_frame.columnconfigure(list(range(3)), weight=1)
        self.display_frame.grid(row=1, rowspan=4, column=0, columnspan=5, sticky='nsew')

    def loginpage(self):
        global eme, pe, cpe, signinb
        cpe = None
        self.display_frame = tk.LabelFrame(master=self.master, text='LOGIN USER', bg='gold', font=('arial black', 12))

        tk.Label(self.display_frame, text='Email', fg='black', bg='gold', font=('calibri', 12, 'bold')).grid(row=0, sticky='e')
        eme = tk.Entry(self.display_frame, font=('calibri', 12), width=30)
        eme.grid(row=0, column=1, sticky='w', padx=3, pady=5)
        eme.focus_set()

        tk.Label(self.display_frame, text='Password', fg='black', bg='gold', font=('calibri', 12, 'bold')).grid(row=1,
                                                                                                        sticky='e')
        pe = tk.Entry(self.display_frame, font=('calibri', 12), show='*', width=15)
        pe.grid(row=1, column=1, sticky='w', padx=3, pady=5)
        eme.bind('<Return>', self.cursor_to_password)
        pe.bind('<Return>', lambda event: login(event, self, self.login_user))

        # radio button to show and hide password entries
        passw = tk.BooleanVar(self.display_frame)
        passw.set(False)
        tk.Checkbutton(self.display_frame, text='Show Password', fg='black', bg='gold', font=('calibri', 12, 'bold'),
                       variable=passw, command=lambda: self.showpassword(passw.get())).grid(row=1, column=1, sticky='e')

        # login/signin button
        signinb = tk.Button(self.display_frame, text="Sign in", font=('calibri', 12, 'bold'), bg='green', fg='white',
                  width=10)
        signinb.bind('<Button-1>',  lambda event: login(event, self, self.login_user))
        signinb.grid(row=2, column=1, sticky='n')

        # front page
        ttk.Button(self.display_frame, text='Back', width=10, command=self.firstpage).grid(row=3, column=0, sticky='e')

        if self.display_frame is not None:
            self.display_frame.grid_forget()

        self.display_frame.rowconfigure(list(range(4)), weight=1)
        self.display_frame.columnconfigure(list(range(3)), weight=1)
        self.display_frame.grid(row=1, rowspan=4, column=0, columnspan=5, sticky='nsew')

    def cursor_to_password(self, event):
        global pe
        pe.focus_set()

    def frontpage(self):
        global startbtn
        # place label on frame
        frontlabel = tk.Label(master=self.introFrame, text='\nTRANSAPP\n\nBY\n\nBEEGIE\n\nMARCH, 2021', fg='black', bg='gold', font=('Arial Black', 20))
        frontlabel.grid(row=0, sticky='nsew')
        tk.Button(self.introFrame, text=" TO START, PRESS 'ENTER' ", command=lambda: self.firstpage(event=None),
                  fg='white', bg='green', font=('arial black', 10, 'bold')).grid(row=1, sticky='sew')

        # place label frame on app frame starting at row 1, column 0
        self.introFrame.grid(row=0, rowspan=4, column=0, columnspan=5, sticky='nsew')

    def menupage(self, event):
        # bind universal events
        self.master.tk_focusFollowsMouse()  # from this point on, focus follows the mouse pointer

        # frame for menu page containing four rows and one column
        self.homeFrame = tk.LabelFrame(master=self.master, text='HOME', fg='black', font=('arial black', 12))
        self.homeFrame.rowconfigure(list(range(3)), weight=1)
        self.homeFrame.columnconfigure(0, weight=1)

        # make status bar reflect logged in user name
        tk.Label(master=self.status_bar_frame, font=('arial black', 10), fg='black', bg='gold',
                 text=f"Logged-in: {self.login_user.company_name}").grid(row=0, column=0, sticky='nsew')

        # make menu bar reflect
        self.master.config(menu=self.menu_bar)

        # set current user's data files
        self.inv_obj.inv_data = f'{self.login_user.filepath}\\Inventory\\inv_data.txt'
        self.inv_obj.inv_edits = f'{self.login_user.filepath}\\Inventory\\edited_inv.txt'
        self.inv_obj.inv_dels = f'{self.login_user.filepath}\\Inventory\\deleted_inv.txt'
        
        self.cust_obj.cust_data = f'{self.login_user.filepath}\\Customers\\cust_data.txt'
        self.cust_obj.cust_edits = f'{self.login_user.filepath}\\Customers\\edited_cust.txt'
        self.cust_obj.cust_dels = f'{self.login_user.filepath}\\Customers\\deleted_cust.txt'
        
        self.sales_obj.sales_data = f'{self.login_user.filepath}\\Sales\\sales_data.txt'
        self.sales_obj.sales_edits = f'{self.login_user.filepath}\\Sales\\edited_sales.txt'
        self.sales_obj.sales_dels = f'{self.login_user.filepath}\\Sales\\deleted_sales.txt'
        
        self.acct_obj.acct_data = f'{self.login_user.filepath}\\Accounts\\acct_data.txt'
        self.acct_obj.acct_edits = f'{self.login_user.filepath}\\Accounts\\edited_acct.txt'
        self.acct_obj.acct_dels = f'{self.login_user.filepath}\\Accounts\\deleted_acct.txt'
        
        self.acctrans_obj.acctrans_data = f'{self.login_user.filepath}\\AccTransactions\\acctrans_data.txt'
        self.acctrans_obj.acctrans_edits = f'{self.login_user.filepath}\\AccTransactions\\edited_acctrans.txt'
        self.acctrans_obj.acctrans_dels = f'{self.login_user.filepath}\\AccTransactions\\deleted_acctrans.txt'

        # menu sections
        self.inventoryb = tk.Button(self.homeFrame, text="INVENTORY", fg='white', bg='purple',
                                    font=('arial black', 14), command=lambda: self.invenpage())

        self.accountb = tk.Button(self.homeFrame, text="ACCOUNTS", fg='white', bg='green',
                                  font=('arial black', 14), command=lambda: self.acctpage())

        self.salesb = tk.Button(self.homeFrame, text="SALES", fg='white', bg='blue',
                                font=('arial black', 14), command=lambda: self.salepage())

        # menu sections
        self.inventoryb.grid(row=0, padx=45, sticky='nsew')
        self.salesb.grid(row=1, padx=30, sticky='nsew')
        self.accountb.grid(row=2, padx=15, sticky='nsew')

        # display frame of menupage
        # clear frame space
        if self.introFrame is not None:
            self.introFrame.grid_forget()
        if self.sectionFrame is not None:
            self.sectionFrame.grid_forget()
        if self.display_frame is not None:
            self.display_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()
        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_frame is not None:
            self.edit_frame.grid_forget()

        self.homeFrame.grid(row=1, rowspan=5, column=0, columnspan=5, sticky='nsew')

    def salepage(self):
        # frame for customer sales page containing three rows and one column
        self.sectionFrame = tk.LabelFrame(master=self.master, text='SALES', font=('arial black', 12), bg='brown',
                                          fg='white')
        self.sectionFrame.rowconfigure(list(range(5)), weight=1)
        self.sectionFrame.columnconfigure(0, weight=1)

        # display sales options
        tk.Button(self.sectionFrame, text='CUSTOMERS', bg='white', fg='blue', font=('arial black', 14),
                  command=lambda: self.custpage()).grid(row=0, padx=40, pady=10, sticky='nsew')
        tk.Button(self.sectionFrame, text='VIEW CUSTOMER ORDERS', bg='white', fg='green', font=('arial black', 14),
                  command=lambda: self.display_sale()).grid(row=1, padx=40, pady=10, sticky='nsew')
        tk.Button(self.sectionFrame, text='BOOK NEW ORDER', bg='white', fg='brown', font=('arial black', 14),
                  command=self.new_sale).grid(row=2, padx=60, pady=10, sticky='nsew')
        tk.Button(self.sectionFrame, text='UPDATE ORDER', bg='white', fg='orange', font=('arial black', 14),
                  command=self.edit_sale).grid(row=3, padx=80, pady=10, sticky='nsew')
        tk.Button(self.sectionFrame, text='DELETE ORDER', bg='white', fg='red', font=('arial black', 14),
                  command=self.delete_sale).grid(row=4, padx=100, pady=10, sticky='nsew')

        # display inventory page's frame
        if self.display_frame is not None:
            self.display_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()
        if self.homeFrame is not None:
            self.homeFrame.grid_forget()

        self.sectionFrame.grid(row=1, rowspan=4, column=0, columnspan=5, sticky='nsew')

    def new_sale(self):
        global prod_ids, prod_names, quants, units, entry_dates
        global customer_ids, fnames, mnames, lnames, genders, dobs, nationalities, states_of_origin, office_addrs, dates_opened
        global dates_opened, acct_ids, cust_ids, acct_types, acct_bals

        bg, fg = 'brown', 'white'

        prod_ids, prod_names, quants, units, entry_dates = self.inv_fields()  # all inventory fields

        customer_ids, fnames, mnames, lnames, genders, dobs, nationalities, states_of_origin, office_addrs, dates_opened = self.cust_fields()  # all customer fields

        dates_opened, acct_ids, cust_ids, acct_types, acct_bals = self.acct_fields()  # all account fields

        cust_details = [(cid, fn, ln) for cid, fn, mn, ln, g, db, n, s, off, do in zip(customer_ids, fnames, mnames, lnames, genders, dobs, nationalities, states_of_origin, office_addrs, dates_opened)]
        prod_details = [(pid, pn) for pid, pn, q, u, d in zip(prod_ids, prod_names, quants, units, entry_dates)]

        # when no product account exists
        if len(prod_ids) < 1:
            return messagebox.showerror(message='No Record of Existing Products')

        # frame for input of new inventory
        self.new_frame = tk.LabelFrame(self.master, text='BOOKING NEW ORDER', fg=fg, font=('arial black', 12),
                                       bg=bg)
        self.new_frame.rowconfigure(list(range(15)), weight=1)
        self.new_frame.columnconfigure(list(range(8)), weight=1)

        # place new sale form
        # Order labels and entries
        tk.Label(self.new_frame, text='Select:', font=('calibri', 12),
                 bg=bg, fg=fg, height=1).grid(row=0, rowspan=2, column=0, stick='sw', padx=15)
        # product
        tk.Label(self.new_frame, text='Product', font=('calibri', 12),
                 bg=bg, fg=fg, height=1).grid(row=0, column=1, stick='sw', padx=15)
        self.pr_idname_Cbox = ttk.Combobox(self.new_frame, font=('calibri', 10, 'bold'), height=2,  width=25,
                                           values=prod_details, state='readonly')
        self.pr_idname_Cbox.set(prod_details[0])
        self.pr_idname_Cbox.grid(row=1, column=1, padx=15, stick='nw')

        # customer
        tk.Label(self.new_frame, text='Customer', font=('calibri', 12),
                 bg=bg, fg=fg, height=1).grid(row=0, column=2, stick='sw')
        self.cust_idnames_Cbox = ttk.Combobox(self.new_frame, font=('calibri', 10, 'bold'), height=2, width=30,
                                              values=cust_details, state='readonly')
        self.cust_idnames_Cbox.grid(row=1, column=2, padx=2, stick='nw')
        self.cust_idnames_Cbox.set(cust_details[0])

        tk.Button(self.new_frame, command=lambda: self.place_ids(self.pr_idname_Cbox.get(), self.cust_idnames_Cbox.get()),
                   font=("Calibri", 10, 'bold'), fg='black', bg='light blue', height=1, width=10,
                  text='Select').grid(row=1, column=5, sticky='nw')
        tk.Button(self.new_frame, text='Cancel', font=("Calibri", 10, 'bold'), fg='red', bg='white', height=1,
                  width=10, command=self.salepage).grid(row=1, column=6, stick='n')

        # display inventory page's frame
        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.sectionFrame is not None:
            self.sectionFrame.grid_forget()
        self.new_frame.grid(row=1, rowspan=8, column=0, columnspan=3, sticky='nsew')

    def place_ids(self, prod_selection, cust_selection):
        global prod_ids, prod_names, quants, units, entry_dates
        global customer_ids, fnames, mnames, lnames, genders, dobs, nationalities, states_of_origin, office_addrs, dates_opened
        global dates_opened, acct_ids, cust_ids, acct_types, acct_bals
        bg, fg = 'brown', 'white'

        # print(prod_selection.split())
        prframe = tk.Frame(self.new_frame, bg=bg, padx=10)
        prframe.grid(row=2, rowspan=2, column=1, sticky='ew')
        cuframe = tk.Frame(self.new_frame, bg=bg, padx=10)
        cuframe.grid(row=2, rowspan=2, column=1, sticky='ew')

        pid, pn = prod_selection.split()  # selection split into a list of strings
        tk.Label(self.new_frame, text='Selected:', font=('calibri', 12),
                 bg=bg, fg=fg, height=1).grid(row=2, column=0, sticky='w')

        tk.Label(prframe, text='Product ID:', font=('calibri', 12), anchor='e',
                 bg=bg, fg=fg, height=1).grid(row=0, column=0, sticky='ew')
        self.prid = tk.Entry(prframe, font=('calibri', 10, 'bold'), fg='white', bg='black', width=10)
        self.prid.insert(0, pid)
        self.prid.grid(row=1, column=0, sticky='ew')
        self.prid.config(state='disabled')

        # print(cust_selection.split())  # selection split into a list
        cid, fn, ln = cust_selection.split()
        tk.Label(cuframe, text='Customer ID:', font=('calibri', 12),
                 bg=bg, fg=fg, height=1).grid(row=0, column=1, sticky='ew')
        self.cuid = tk.Entry(cuframe, font=('calibri', 10, 'bold'), fg='white', bg='black', width=10)
        self.cuid.insert(0, cid)
        self.cuid.grid(row=1, column=1, sticky='ew')
        self.cuid.config(state='disabled')

        Found = False
        sel_currs, sel_acids = [], []
        for d, a, c, t, b in zip(dates_opened, acct_ids, cust_ids, acct_types, acct_bals):
            if c == cid:
                sel_currs.append(t)  # a list of all the customer's account-types/currencies
                sel_acids.append(a)  # a list of all the customer's account numbers
                Found = True
        if not Found:
            return messagebox.showinfo(message="Customer's account is inactive")

        # select the account type from account number
        tk.Label(self.new_frame, text='Select Account', font=('calibri', 12),
                 bg=bg, fg=fg, height=1).grid(row=0, column=2, stick='sw')
        self.currCbox = ttk.Combobox(self.new_frame, font=('calibri', 10, 'bold'), values=sel_acids)
        self.currCbox.grid(row=1, column=2, padx=2, stick='nw')
        self.currCbox.set('None')
        self.currCbox.config(state='readonly')
        self.currCbox.bind('<FocusIn>', self.disp_curr)
        self.currCbox.bind('<FocusOut>', self.disp_curr2)

        # currency
        tk.Label(self.new_frame, text='Currency', font=('calibri', 12), bg=bg, fg=fg,
                 height=1).grid(row=6, column=2, stick='sw')
        self.currEntry = ttk.Entry(self.new_frame, font=('calibri', 10, 'bold'))
        self.currEntry.grid(row=7, column=2, padx=2, stick='nw')
        self.currEntry.insert(0, 'None Selected')
        self.currEntry.config(state='disabled')

        # ordered quantity
        tk.Label(self.new_frame, text='Quantity', font=('calibri', 12), bg=bg, fg=fg,
                 height=1).grid(row=4, column=0, padx=15, stick='sw')
        self.ord_qtyEntry = tk.Entry(self.new_frame, font=('calibri', 10, 'bold'), fg='black')
        self.ord_qtyEntry.grid(row=5, column=0, padx=15, stick='nw')
        evt1 = '<KeyRelease>'
        self.ord_qtyEntry.bind(evt1, self.calc_price)

        # unit of measurement
        tk.Label(self.new_frame, text='Unit', font=('calibri', 12),
                 bg=bg, fg=fg, height=1).grid(row=4, column=1, stick='sw')
        self.ord_unitEntry = tk.Entry(self.new_frame, font=('calibri', 10, 'bold'), bg='black', fg='white')
        self.ord_unitEntry.grid(row=5, column=1, padx=2, stick='nw')
        for prdid, pn, q, u, d in zip(prod_ids, prod_names, quants, units, entry_dates):
            if prdid == pid:
                self.ord_unitEntry.insert(0, f'{u}')
        self.ord_unitEntry.config(state='disabled')

        # rate of order
        tk.Label(self.new_frame, text='Rate/Unit', font=('calibri', 12),
                 bg=bg, fg=fg, height=1).grid(row=6, column=3, stick='sw')
        self.ord_rateEntry = tk.Entry(self.new_frame, font=('calibri', 10, 'bold'))
        self.ord_rateEntry.grid(row=7, column=3, padx=2, stick='nw')
        evt2 = '<KeyRelease>'
        self.ord_rateEntry.bind(evt2, self.calc_price)

        # price
        tk.Label(self.new_frame, text='Price', font=('calibri', 12), bg=bg, fg=fg,
                 height=1).grid(row=6, column=4, stick='sw')
        self.ord_priceEntry = tk.Entry(self.new_frame, font=('calibri', 10, 'bold'), fg='white', bg='black')
        self.ord_priceEntry.grid(row=7, column=4, padx=2,  stick='nw')
        self.ord_priceEntry.insert(0, 'Yet to be determined')
        self.ord_priceEntry.config(state='disabled')
        #
        # # customer order date
        # tk.Label(self.new_frame, text='Date of Order', font=('calibri', 12),
        #          bg=bg, fg=fg, height=1).grid(row=5, column=0, padx=10, stick='nsew')
        # # day
        # tk.Label(self.new_frame, text='Day', font=('calibri', 12), bg=bg, fg=fg,
        #          height=1).grid(row=5, column=1, padx=5, stick='nw')
        # self.orddayEntry = tk.Entry(self.new_frame, font=('calibri', 10, 'bold'), width=10)
        # self.orddayEntry.insert(0, str(datetime.date.today().day))
        # self.orddayEntry.grid(row=6, column=1, padx=5, pady=30, stick='sw')
        # # month
        # tk.Label(self.new_frame, text='Month', font=('calibri', 12), bg=bg, fg=fg,
        #          height=1).grid(row=5, column=2, padx=5, stick='nw')
        # self.ordmonthEntry = tk.Entry(self.new_frame, font=('calibri', 10, 'bold'), width=10)
        # self.ordmonthEntry.insert(0, str(datetime.date.today().month))
        # self.ordmonthEntry.grid(row=6, column=2, padx=5, pady=30, stick='sw')
        # # year
        # tk.Label(self.new_frame, text='Year', font=('calibri', 12), bg=bg, fg=fg,
        #          height=1).grid(row=5, column=3, stick='nw')
        # self.ordyrEntry = tk.Entry(self.new_frame, font=('calibri', 10, 'bold'), width=10)
        # self.ordyrEntry.insert(0, str(datetime.date.today().year))
        # self.ordyrEntry.grid(row=6, column=3, pady=30, stick='sw')
        #
        # # customer amount deposited
        # tk.Label(self.new_frame, text='Deposit', font=('calibri', 12), bg=bg, fg=fg,
        #          height=1).grid(row=7, column=0, padx=10, stick='nsew')
        # self.depEntry = tk.Entry(self.new_frame, font=('calibri', 10, 'bold'), width=10)
        # self.depEntry.grid(row=8, column=0, padx=5, pady=30, stick='sw')
        #
        # # payment status
        # tk.Label(self.new_frame, text='Payment Status', font=('calibri', 12), bg=bg, fg=fg,
        #          height=1).grid(row=7, column=1, padx=5, stick='nsew')
        # self.pay_statText = tk.Text(self.new_frame, font=('calibri', 10, 'bold'), width=10, height=3)
        # self.pay_statText.grid(row=8, column=1, padx=5, pady=30, sticky='ew')
        #
        # payment = tk.StringVar(value='None')
        # complRadio = tk.Radiobutton(self.new_frame, text='Complete', value='Complete', variable=payment, font=('calibri', 16), bg='blue', fg='black', command=lambda: self.sel_paystat(payment.get()), state='normal')
        # complRadio.grid(row=9, column=1, padx=2, sticky='w')
        # incomplRadio = tk.Radiobutton(self.new_frame, text='Incomplete', value='Incomplete', variable=payment, font=('calibri', 16),
        #                              bg='blue', fg='black', command=lambda: self.sel_paystat(payment.get()), state='normal')
        # incomplRadio.grid(row=9, column=2, padx=2, sticky='w')

        tk.Button(self.new_frame, text='Submit', font=("Calibri", 14, 'bold'), fg='white', bg='green', width=10,
                  height=1, command=self.submit_sale).grid(row=13, column=2, padx=10, sticky='se')

    def calc_price(self, event):
        qty, rate = self.ord_qtyEntry.get(), self.ord_rateEntry.get()  # store qty and rate
        if qty not in string.whitespace and rate not in string.whitespace:

            try:
                calc_amnt = float(qty) * float(rate)
                self.ord_priceEntry.config(state='normal')
                self.ord_priceEntry.delete(0, 'end')
                self.ord_priceEntry.insert(0, calc_amnt)
                self.ord_priceEntry.config(state='disabled')
            except:
                return messagebox.showerror(message='Quantity and Rate should be given in figures')
        else:
            self.ord_priceEntry.config(state='normal')
            self.ord_priceEntry.delete(0, 'end')
            self.ord_priceEntry.insert(0, 'Yet to be determined')
            self.ord_priceEntry.config(state='disabled')

    def disp_curr(self, event):
        global dates_opened, acct_ids, cust_ids, acct_types, acct_bals
        aid = self.currCbox.get()  # selected account id
        self.currEntry.config(state='normal')
        for d, a, c, t, b in zip(dates_opened, acct_ids, cust_ids, acct_types, acct_bals):
            if a == aid:
                self.currEntry.delete(0, 'end')
                self.currEntry.insert(0, t)  # display selected customer's account-type/currency
        self.currEntry.config(state='disabled')
        self.currCbox.unbind('<FocusIn>')  # no longer respond to focus in
        self.currCbox.bind('<Button-1>')  # now respond to mouse left click

    def disp_curr2(self, event):
        self.currCbox.bind('<FocusIn>', self.disp_curr)  # upon focus out rebind focus in

    def inv_fields(self):
        invdata = self.read_inv()

        prod_ids = [v for line in invdata for k, v in eval(line).items() if k == 'prod_id']
        prod_names = [v for line in invdata for k, v in eval(line).items() if k == 'prod_name']
        quants = [v for line in invdata for k, v in eval(line).items() if k == 'qty']
        units = [v for line in invdata for k, v in eval(line).items() if k == 'unit']
        entry_dates =  [v for line in invdata for k, v in eval(line).items() if k == 'entry_date']

        return prod_ids, prod_names, quants, units, entry_dates

    def sel_paystat(self, payment_status):
        self.sales_obj.payment_status = payment_status
        print(self.sales_obj.payment_status)

    def submit_sale(self):
        pass

    def savesale(self):
        pass

    def read_sale(self):
        pass

    def display_sale(self):
        pass

    def edit_sale(self):
        pass

    def editing_sale(self):
        pass

    def update_sale(self):
        pass

    def delete_sale(self):
        pass

    def erase_sale(self):
        pass

    def acctpage(self):
        # frame for customer accounts page containing three rows and one column
        self.sectionFrame = tk.LabelFrame(master=self.master, text='CUSTOMER ACCOUNTS', font=('arial black', 12), bg='brown',
                                          fg='white')
        self.sectionFrame.rowconfigure([0, 1, 2, 3], weight=1)
        self.sectionFrame.columnconfigure(0, weight=1)

        # display sales options
        tk.Button(self.sectionFrame, text='VIEW ACCOUNTS', bg='white', fg='green', font=('arial black', 14), 
                  command=lambda: self.display_acct()).grid(row=0, padx=40, pady=10, sticky='nsew')
        tk.Button(self.sectionFrame, text='CREATE ACCOUNT', bg='white', fg='blue',
                  font=('arial black', 14), command=self.new_acct).grid(row=1, padx=60, pady=10, sticky='nsew')
        tk.Button(self.sectionFrame, text='UPDATE ACCOUNT', bg='white', fg='orange',
                  font=('arial black', 14), command=self.edit_acct).grid(row=2, padx=80, pady=10, sticky='nsew')
        tk.Button(self.sectionFrame, text='ACCOUNT TRANSACTIONS', bg='white', fg='brown',
                  font=('arial black', 14), command=self.acctranspage).grid(row=3, padx=100, pady=10, sticky='nsew')
        
        # display inventory page's frame
        if self.display_frame is not None:
            self.display_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()
        if self.homeFrame is not None:
            self.homeFrame.grid_forget()

        self.sectionFrame.grid(row=1, rowspan=4, column=0, columnspan=5, sticky='nsew')

    def new_acct(self):
        global custs, cname_cbox
        bg, fg = 'green', 'white'

        # frame for input of new inventory
        self.new_frame = tk.LabelFrame(self.master, text='REGISTER NEW ACCOUNT FOR CUSTOMER', fg=fg, font=('arial black', 12),
                                       bg=bg)
        self.new_frame.rowconfigure(list(range(7)), weight=1)
        self.new_frame.columnconfigure(list(range(5)), weight=1)

        # create a list of existing customers
        customer_ids = None

        customer_ids, fnames, mnames, lnames, genders, dobs, nationalities, states_of_origin, office_addrs, dates_opened = self.cust_fields()

        # when no customer account exists
        if customer_ids is None:
            return messagebox.showerror(message='No Record of Existing Customers')

        print(f'{customer_ids}\n{fnames}\n{mnames}\n{lnames}')
        # create list of tuples containing (first, mid, last names) of each customer
        custs = [(i, f, m, l) for i, f, m, l in zip(customer_ids, fnames, mnames, lnames)]
        cust_names = [(f, m, l) for f, m, l in zip(fnames, mnames, lnames)]
        print(f'Customers: {custs}')

        # place new account form
        # use company name to select customer ID
        tk.Label(self.new_frame, text='Create Account For:', font=('calibri', 13),
                 bg=bg, fg=fg, height=1).grid(row=0, column=0, padx=10, stick='nse')
        cname_cbox = ttk.Combobox(self.new_frame, value=cust_names, font=('calibri', 13), width=24, state='readonly')
        for f, m, l in cust_names:
            cname_cbox.set((f, m, l))
            break
        cname_cbox.grid(row=0, column=1, sticky='w')
        ttk.Button(self.new_frame, text='SELECT', command=lambda: self.popup_acctform(cname_cbox.get())
                   ).grid(row=0, column=2, sticky='w')
        ttk.Button(self.new_frame, text='ACCOUNTS MENU', width=18,
                   command=self.acctpage).grid(row=0, column=3, padx=5, stick='e')

        # display inventory page's frame
        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.sectionFrame is not None:
            self.sectionFrame.grid_forget()
        self.new_frame.grid(row=1, rowspan=8, column=0, columnspan=3, sticky='nsew')

    def popup_acctform(self, selected_customer):
        global custs, cust_id, fname, lname
        bg, fg = 'green', 'white'

        # display corresponding customer id
        fname, mname, lname = selected_customer.split()
        for cid, f, m, l in custs:
            if str(f) == str(fname) and str(m) == str(mname) and str(l) == str(lname):
                # print(f, m, l)
                tk.Label(self.new_frame, text='Selected Customer ID:', font=('calibri', 13),
                         bg=bg, fg=fg).grid(row=1, column=0, padx=10, sticky='e')
                cust_id = tk.Entry(self.new_frame, font=('calibri', 13, 'bold'), width=12, fg='black')
                cust_id.insert(0, f'{cid}')
                cust_id.grid(row=1, column=1, sticky='w')
                cust_id.config(state='readonly')

        # select currency/type of account
        currs = ['NGN', 'GBP', 'USD', 'CAD', 'AUD', 'GHC']
        tk.Label(self.new_frame, text='Account Currency', font=('calibri', 13),
                 bg=bg, fg=fg, height=1).grid(row=2, column=0, padx=10, stick='nse')
        self.currencyCbox = ttk.Combobox(self.new_frame, value=currs, font=('calibri', 13, 'bold'), width=5, state='readonly')
        self.currencyCbox.set(currs[0])
        self.currencyCbox.grid(row=2, column=1, sticky='w')

        # balance
        tk.Label(self.new_frame, text='Account Balance:', font=('calibri', 13),
                 bg=bg, fg=fg, height=1).grid(row=3, column=0, padx=10, stick='nse')
        self.amntEntry = tk.Entry(self.new_frame, font=('calibri', 13, 'bold'), fg='black', width=18)
        self.amntEntry.insert(0, '0')
        self.amntEntry.grid(row=3, column=1, sticky='w')
        self.amntEntry.config(state='disabled')

        # date of registration
        tk.Label(self.new_frame, text='Date Opened:', font=('calibri', 13),
                 bg=bg, fg=fg, height=1).grid(row=4, column=0, padx=10, sticky='e')
        # day
        tk.Label(self.new_frame, text='Day', font=('calibri', 13),
                 bg=bg, fg=fg, height=1).grid(row=4, column=1, sticky='nw')
        self.transdayCbox = ttk.Combobox(self.new_frame, value=self.day, font=('calibri', 13, 'bold'),
                                         width=3, state='readonly')
        self.transdayCbox.set(str(datetime.date.today().day))
        self.transdayCbox.grid(row=4, column=1, padx=5, pady=30, sticky='w')
        # month
        tk.Label(self.new_frame, text='Month', font=('calibri', 13), bg=bg, fg=fg,
                 height=1).grid(row=4, column=2, sticky='nw')
        self.transmonthCbox = ttk.Combobox(self.new_frame, value=[v for k, v in self.month.items()],
                                           font=('calibri', 13, 'bold'), width=4, state='readonly')
        self.transmonthCbox.set(self.month[datetime.date.today().month])
        self.transmonthCbox.grid(row=4, column=2, padx=5, pady=30, sticky='w')
        # year
        tk.Label(self.new_frame, text='Year', font=('calibri', 13), bg=bg, fg=fg,
                 height=1).grid(row=4, column=3, sticky='nw')
        self.transyrCbox = ttk.Combobox(self.new_frame, value=self.year, font=('calibri', 13, 'bold'),
                                        width=4, state='readonly')
        self.transyrCbox.set(str(datetime.date.today().year))
        self.transyrCbox.grid(row=4, column=3, pady=30, sticky='w')

        tk.Button(self.new_frame, text='CREATE ACCOUNT', fg=bg, bg=fg,
                  font=('calibri', 13), command=lambda: self.submit_acct()).grid(row=6, column=2, sticky='e')

    def submit_acct(self):
        global cust_id, fname, lname
        bg, fg = 'green', 'white'
        # frame for submission status
        self.submit_frame = tk.LabelFrame(self.master, text='DO YOU WANT TO SAVE?', fg=fg, bg=bg,
                                          font=('arial black', 12))
        self.submit_frame.rowconfigure(list(range(4)), weight=1)
        self.submit_frame.columnconfigure(list(range(4)), weight=1)

        # define the necessary variables
        cid, curr, amount = cust_id.get(), self.currencyCbox.get(), self.amntEntry.get()
        trday, trmon, tryr = self.transdayCbox.get(), self.transmonthCbox.get(), self.transyrCbox.get()

        mandatory_entries = [amount]
        num_type_entries = [amount]
        wspace = string.whitespace
        puncs = string.punctuation

        lines = {}
        acct = []

        # check for empty field
        if [True for entry in mandatory_entries if (entry in wspace) or (entry is None)]:
            return messagebox.showerror(title='Blank Field', message='BLANK FIELD(S) DETECTED!')
        # check for fields with punctuations
        if [True for entry in mandatory_entries if (entry in puncs)]:
            return messagebox.showerror(title='Punctuation Error',
                                        message='FIELD(S) CANNOT CONTAIN PUNCTUATION MARK(S)!')

        # check for fields with invalid data types
        try:
            float(amount)
        except ValueError as VE:
            # non-figures have been entered, if no error was raised
            return messagebox.showerror(title='Invalid Data Type',
                                        message=f'{amount} is not a number\nPlease enter a number!')

        # check if customer account already exists
        # especially with same currency
        # create a list of existing customers
        with open(self.acct_obj.acct_data, 'r', encoding='utf8') as hand:
            data = hand.readlines()
        # create list of account details for each customer
        customer_ids = [v for line in data for k, v in eval(line).items() if k == 'customer_id']
        acct_ids = [v for line in data for k, v in eval(line).items() if k == 'account_id']
        currencies = [v for line in data for k, v in eval(line).items() if k == 'currency']
        dates_opened = [v for line in data for k, v in eval(line).items() if k == 'date_opened']

        # when customer already has an existing account with same currency
        if cid in customer_ids:
            # create list of tuples containing (cust_id, acct_id, currency, dates_opened) for each customer
            for c, a, r, d in zip(customer_ids, acct_ids, currencies, dates_opened):
                if c == cid and r == curr:
                    return messagebox.showerror(title='Same-Currency Account Already Exists',
                                                message=f'Customer {c} Already Has An Existing {r} account\n\nCreated: {d}')

        self.acct_obj.account_id = f'{lname[:2]}{fname[:2]}{self.ID_gen()}{curr}'
        self.acct_obj.customer_id = cid
        self.acct_obj.date_opened = f'{datetime.date.today().year}-{self.month[datetime.date.today().month]}-{datetime.date.today().day}'
        self.acct_obj.balance, self.acct_obj.currency = amount, curr

        print(self.acct_obj.__dict__)

        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg=bg, fg=fg,
                 text=f"ACCOUNT ID\n{self.acct_obj.account_id}").grid(row=0, column=0, sticky='ew')
        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg=bg, fg=fg,
                 text=f"CUSTOMER ID\n{self.acct_obj.customer_id}").grid(row=0, column=1, sticky='ew')
        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg=bg, fg=fg,
                 text=f"BALANCE\n{self.acct_obj.balance}").grid(row=0, column=2, sticky='ew')
        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg=bg, fg=fg,
                 text=f"CURRENCY\n{self.acct_obj.currency}").grid(row=0, column=3, sticky='ew')
        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg=bg, fg=fg,
                 text=f"DATE OPENED\n{self.acct_obj.date_opened}").grid(row=1, column=1, sticky='ew')

        # save and cancel buttons
        tk.Button(self.submit_frame, text='Save', font=("Calibri", 14, 'bold'), fg='green', bg='white',
                  height=3, width=10, command=self.saveacct).grid(row=3, column=0, padx=5, stick='ew')
        tk.Button(self.submit_frame, text='Cancel', font=("Calibri", 14, 'bold'), bg='red', fg='white',
                  height=3, width=10, command=self.new_acct).grid(row=3, column=3, padx=5, stick='ew')

        if self.display_frame is not None:
            self.display_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        self.submit_frame.grid(row=1, sticky='nsew')

    def saveacct(self):
        bg, fg = 'green', 'white'

        with open(self.acct_obj.acct_data, 'a',
                  encoding='utf8') as hand:
            hand.writelines(f"{self.acct_obj.__dict__}\n")

        self.submit_frame = self.make_frame(background_color='green')

        tk.Label(self.submit_frame, text='NEW CUSTOMER ACCOUNT CREATED!', font=("arial", 14, 'bold'),
                         bg=bg, fg=fg).grid(row=0, column=0, columnspan=4, sticky='nsew')

        tk.Button(self.submit_frame, text='Add Another', font=("Calibri", 14, 'bold'), bg='blue', fg=fg,
                  height=5, width=15, command=self.new_acct).grid(row=1, column=0, padx=5, stick='ew')

        tk.Button(self.submit_frame, text='Accounts Page', font=("Calibri", 14, 'bold'), fg=bg, bg=fg,
                  height=5, width=15, command=self.acctpage).grid(row=1, column=3, padx=5, stick='ew')

        self.submit_frame.rowconfigure([0, 1], weight=1)
        self.submit_frame.columnconfigure(list(range(4)), weight=1)
        self.submit_frame.grid(row=1, sticky='nsew')

    def read_acct(self):
        with open(self.acct_obj.acct_data, 'r', encoding='utf8') as hand:
            # customer atributes is a list of record strings
            acct_atr = hand.readlines()
        return acct_atr

    def display_acct(self):
        global acctdata, acct, lines
        bg, fg = 'green', 'white'
        acct = []
        lines = {}

        # setup display frame
        self.display_frame = self.make_frame(page_title='CUSTOMER ACCOUNTS VIEW', background_color=bg)

        # create a list of existing customer accounts
        dates_opened, acct_ids, cust_ids, acct_types, acct_bals = self.acct_fields()

        if len(acct_ids) < 1:
            return messagebox.showinfo(message='There are no existing accounts to view'
                                               '\n\nPlease create account(s) for customer(s)')
        # select account id
        tk.Label(self.display_frame, text='Select Customer Account:', font=('calibri', 13),
                 bg=bg, fg=fg, height=1).grid(row=0, column=0, padx=10, stick='nse')
        cacct_Cbox = ttk.Combobox(self.display_frame, value=acct_ids, font=('calibri', 13), width=24, state='readonly')
        cacct_Cbox.set(acct_ids[0])
        cacct_Cbox.grid(row=0, column=1, sticky='w')
        ttk.Button(self.display_frame, text='SELECT', command=lambda: self.pop_acctview(cacct_Cbox.get())
                   ).grid(row=0, column=2, sticky='w')

        tk.Button(self.display_frame, text='Accounts Page', font=("Calibri", 12, 'bold'), fg=bg, bg=fg, height=1, 
                  width=15, command=self.acctpage).grid(row=2, column=3, padx=5, pady=5, stick='se')

        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_frame is not None:
            self.edit_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        self.display_frame.rowconfigure(list(range(3)), weight=1)
        self.display_frame.columnconfigure(list(range(9)), weight=1)
        self.display_frame.grid(row=1, rowspan=2, column=0, columnspan=4, sticky='nsew')

    def pop_acctview(self, selected_acctid):
        global acctdata
        bg, fg = 'green', 'white'

        acct = self.fetch_acct(selected_acctid)  # get fields of the selected account
        acct_bal = self.get_bal(selected_acctid)  # get current account balance
        custid, f_name, m_name, l_name, sex, dbirth, country, state, office, dopened  = self.fetch_cust(acct['customer_id'])  # get fields of the selected customer
        c_name = f'{f_name} {l_name}'  # customer's first and last names

        if acct_bal is None:
            return messagebox.showinfo(
                message=f'{selected_acctid} is an inactive account\nPlease select another account')

        # display headings for customer records
        # create scrolled text field to display customer records
        st = scrolledtext.ScrolledText(self.display_frame, bg=bg, fg=fg, wrap='word',
                                       font=("Calibri", 14, 'bold'), relief='flat')
        st.grid(row=0, column=0, columnspan=8, sticky='nsew')
        # display headings for customer records
        st.insert(index='end',
                  chars='ACCOUNT ID,\tCUSTOMER ID,\tCUSTOMER NAME,\tCURRENCY,\tBALANCE,\tDATE OPENED\n\n')

        st.insert(index='end',
                  chars=f"{acct['account_id']},\t{acct['customer_id']},\t{c_name},\t{acct['currency']},\t{acct_bal},\t{acct['date_opened']}\n\n")
        # make text field read-only
        st.config(state='disabled')
        # ensure that text can be copied to clipboard
        st.bind('<1>', lambda event: st.focus_set())
        
    def fetch_acct(self, selected_acctid):
        '''
        returns the details of the selected account in a dictionary format
        :param selected_acctid:
        :return:--> {'date_opened': '', 'account_id': '', 'customer_id': '', 'currency': '', 'balance': ''}
        '''
        dates_opened, acct_ids, cust_ids, acct_types, acct_bals = self.acct_fields()

        acct = {'date_opened': '', 'account_id': '', 'customer_id': '', 'currency': '', 'balance': ''}

        for d, ai, cid, curr, bal in zip(dates_opened, acct_ids, cust_ids, acct_types, acct_bals):
            if ai == selected_acctid:
                acct['date_opened'], acct['account_id'], acct['customer_id'], acct['currency'], acct['balance'] = d, ai, cid, curr, bal

        return acct
        
    def acct_fields(self):
        '''
        to generate a tuple of lists containing transactions in separate fields
        :return:--> (dates_opened, acct_ids, cust_ids, acct_types, acct_bals)
        '''

        with open(self.acct_obj.acct_data, 'r', encoding='utf8') as hand:
            acctdata = hand.readlines()
            # creating a list of customer transaction fields for each transaction
            dates_opened = [v for line in acctdata for k, v in eval(line).items() if k == 'date_opened']
            acct_ids = [v for line in acctdata for k, v in eval(line).items() if k == 'account_id']
            cust_ids = [v for line in acctdata for k, v in eval(line).items() if k == 'customer_id']
            acct_types = [v for line in acctdata for k, v in eval(line).items() if k == 'currency']
            acct_bals = [v for line in acctdata for k, v in eval(line).items() if k == 'balance']

        return dates_opened, acct_ids, cust_ids, acct_types, acct_bals

    def get_bal(self, selected_acctid):
        '''
        calculate the current balance of the selected account
        :param selected_acctid:
        :return: --> float(acct_bal)
        '''
        creds, debs = [], []

        trans = self.get_active_acctrans(selected_acctid)  # calculate customer's current account balance

        if trans is None:
            return None
        # print(trans)
        for ind in range(len([v for k, v in trans.items() if k == 'trans_date'][0])):
            # print(ind)
            if trans['trans_type'][ind] == 'Credit':
                creds.append(float(trans['amount'][ind]))
            if trans['trans_type'][ind] == 'Debit':
                debs.append(float(trans['amount'][ind]))
        # current balance
        # print(f"Debits: {debs}\nCredits: {creds}")
        acct_bal = sum(creds) - sum(debs)
        return acct_bal

    def edit_acct(self):
        bg, fg = 'green', 'white'
        acct = []
        lines = {}

        # setup display frame
        self.display_frame = self.make_frame(page_title='CUSTOMER ACCOUNTS VIEW', background_color=bg)

        # create a list of existing customer accounts
        dates_opened, acct_ids, cust_ids, acct_types, acct_bals = self.acct_fields()

        if len(acct_ids) < 1:
            return messagebox.showinfo(message='There are no existing accounts to view'
                                               '\n\nPlease create account(s) for customer(s)')
        # select account id
        tk.Label(self.display_frame, text='Select Customer Account:', font=('calibri', 13),
                 bg=bg, fg=fg, height=1).grid(row=0, column=0, padx=10, stick='nse')
        cacct_Cbox = ttk.Combobox(self.display_frame, value=acct_ids, font=('calibri', 13), width=24, state='readonly')
        cacct_Cbox.set(acct_ids[0])
        cacct_Cbox.grid(row=0, column=1, sticky='w')
        ttk.Button(self.display_frame, text='SELECT', command=lambda: self.pop_editacct_form(cacct_Cbox.get())
                   ).grid(row=0, column=2, sticky='w')

        tk.Button(self.display_frame, text='Accounts Page', font=("Calibri", 12, 'bold'), fg=bg, bg=fg, height=1,
                  width=15, command=self.acctpage).grid(row=2, column=3, padx=5, pady=5, stick='se')

        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_frame is not None:
            self.edit_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        self.display_frame.rowconfigure(list(range(3)), weight=1)
        self.display_frame.columnconfigure(list(range(9)), weight=1)
        self.display_frame.grid(row=1, rowspan=2, column=0, columnspan=4, sticky='nsew')

    def pop_editacct_form(self, selected_acctid):
        bg, fg = 'green', 'white'

        acct = self.fetch_acct(selected_acctid)  # get fields of the selected account
        acct_bal = self.get_bal(selected_acctid)  # get current account balance
        custid, f_name, m_name, l_name, sex, dbirth, country, state, office, dopened = self.fetch_cust(
            acct['customer_id'])  # get fields of the selected customer
        c_name = f'{f_name} {l_name}'  # customer's first and last names

        if acct_bal is None:
            return messagebox.showinfo(
                message=f'{selected_acctid} is an inactive account\nPlease select another account')

        # display headings for customer records
        # create scrolled text field to display customer records
        st = scrolledtext.ScrolledText(self.display_frame, bg=bg, fg=fg, wrap='word',
                                       font=("Calibri", 14, 'bold'), relief='flat')
        st.grid(row=0, column=0, columnspan=8, sticky='nsew')
        # display headings for customer records
        st.insert(index='end',
                  chars='ACCOUNT ID,\tCUSTOMER ID,\tCUSTOMER NAME,\tCURRENCY,\tBALANCE,\tDATE OPENED\n\n')

        st.insert(index='end',
                  chars=f"{acct['account_id']},\t{acct['customer_id']},\t{c_name},\t{acct['currency']},\t{acct_bal},\t{acct['date_opened']}\n\n")
        # make text field read-only
        st.config(state='disabled')
        # ensure that text can be copied to clipboard
        st.bind('<1>', lambda event: st.focus_set())

        # to edit the given row number (at row entry - 1)
        tk.Label(self.display_frame, text='CONFIRM ACCOUNT ID:', font=("Calibri", 12, 'bold'), bg=bg,
                 fg=fg).grid(row=2, column=0, padx=2, sticky='e')
        # select transid
        edit_acctidCbox = ttk.Combobox(self.display_frame, width=12, value=acct['account_id'],
                                        font=("Calibri", 12, 'bold'), state='readonly')
        edit_acctidCbox.set(acct['account_id'])
        edit_acctidCbox.grid(row=2, column=1, sticky='w')

        # edit button
        ttk.Button(self.display_frame, text='Confirm', width=15, command=lambda:
        self.editing_acct(edit_acctidCbox.get())).grid(row=2, column=2, sticky='w')

    def editing_acct(self, selected_acctid):
        bg, fg = 'green', 'white'
        self.display_frame = self.make_frame(page_title='EDIT SELECTED ACCOUNT', background_color=bg)

        acct = self.fetch_acct(selected_acctid)
        acct_bal = self.get_bal(selected_acctid)

        # print(self.acct_obj.__dict__)
        self.acct_obj.__dict__.update(acct)  # setting the account instance to have the selected account details
        # print(self.acct_obj.__dict__)

        # display editable fields in entries for user
        tk.Label(self.display_frame, text="ACCOUNT ID", font=("Calibri", 12, 'bold'),
                 bg=bg, fg=fg).grid(row=1, column=0, sticky='sw', padx=25, pady=15)
        self.accid_entry = tk.Entry(self.display_frame, font=("Calibri", 12, 'bold'))
        self.accid_entry.insert(0, string=f'{self.acct_obj.account_id}')
        self.accid_entry.config(state='disabled')
        self.accid_entry.grid(row=2, column=0, sticky='w', padx=25, pady=5)

        tk.Label(self.display_frame, text="CUSTOMER ID", font=("Calibri", 12, 'bold'),
                 bg=bg, fg=fg).grid(row=1, column=1, sticky='sw', padx=25, pady=15)
        self.cid_entry = tk.Entry(self.display_frame, font=("Calibri", 12, 'bold'))
        self.cid_entry.insert(0, string=f'{self.acct_obj.customer_id}')
        self.cid_entry.config(state='disabled')
        self.cid_entry.grid(row=2, column=1, sticky='w', padx=25, pady=5)

        tk.Label(self.display_frame, text="CURRENCY", font=("Calibri", 12, 'bold'),
                 bg=bg, fg=fg).grid(row=1, column=2, sticky='sw', padx=25, pady=15)
        currs = ['NGN', 'GBP', 'USD', 'CAD', 'AUD', 'GHC']
        self.acurr_Cbox = ttk.Combobox(self.display_frame, font=("Calibri", 12, 'bold'), value=currs, state='readonly')
        self.acurr_Cbox.set(f'{self.acct_obj.currency}')
        self.acurr_Cbox.grid(row=2, column=2, sticky='w', padx=25, pady=5)

        tk.Label(self.display_frame, text="CURRENT BALANCE", font=("Calibri", 12, 'bold'),
                 bg=bg, fg=fg).grid(row=3, column=0, sticky='sw', padx=25, pady=15)
        self.acbal_entry = tk.Entry(self.display_frame, font=("Calibri", 12, 'bold'))
        self.acbal_entry.insert(0, string=f'{acct_bal}')
        self.acbal_entry.config(state='disabled')
        self.acbal_entry.grid(row=4, column=0, sticky='w', padx=25, pady=5)

        # update and customer page buttons
        tk.Button(self.display_frame, text='Update', font=("Calibri", 12, 'bold'), bg='orange', fg='white',
                  height=1, width=15, command=lambda: self.update_acct(selected_acctid)).grid(row=6, column=1, padx=5, pady=5, stick='w')

        tk.Button(self.display_frame, text='Accounts Page', font=("Calibri", 12, 'bold'),
                  bg='blue', fg='white', height=1, width=15, command=self.acctpage).grid(row=6, column=2, padx=5,
                                                                                             pady=5, stick='e')

        # clear the frames before and after this page
        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_frame is not None:
            self.edit_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        # display an adjustible frame containing the selected info
        self.display_frame.rowconfigure(list(range(7)), weight=1)
        self.display_frame.columnconfigure(list(range(4)), weight=1)
        self.display_frame.grid(row=1, rowspan=2, column=0, columnspan=4, sticky='nsew')

    def update_acct(self, selected_acctid):
        bg, fg = 'green', 'white'
        typ, accid = self.acurr_Cbox.get(), self.accid_entry.get()
        dates_opened, acct_ids, cust_ids, acct_types, acct_bals = self.acct_fields()
        beg = accid[:4]

        new_accid = f'{accid[:9]}{typ}'  # modifying the account id to reflect the change

        if (typ == self.acct_obj.currency):
            return messagebox.showerror(title='Same Values As Values',
                                        message='No Changes Made!\n\nPlease Check The Following Fields: \nAccount Type')

        # print(beg, typ)
        # print([True for ai in acct_ids if ai.startswith(beg) and ai.endswith(typ)])
        # print(type(new_accid), acct_ids)
        if [True for ai in acct_ids if ai.startswith(beg) and ai.endswith(typ)]:  # check if user already has selected account type
            return messagebox.showerror(title='Account Already Exists',
                                        message=f'User Already Has a {typ} Account\n\nPlease Choose another Account Type')

        if not(messagebox.askyesno(message='Do You Want To Save Changes Made?')):
            messagebox.showinfo(message='No Changes Made')
            return self.edit_acctrans()

        self.save_edited_acct()  # save entry before changes made is implemented
        self.acct_obj.account_id, self.acct_obj.currency = new_accid, typ  # setting the account instance to changes made
        # print(self.acct_obj.__dict__)  # edited version

        self.alter_acctid_trans(selected_acctid, new_accid)  # change the account id for old transactions

        for ind in range(len(acct_ids)):  # fetch the particular transaction for editing
            if acct_ids[ind] == selected_acctid:
                acct_ids[ind], cust_ids[ind], acct_types[ind], acct_bals[ind], dates_opened[
                    ind] = self.acct_obj.account_id, self.acct_obj.customer_id, self.acct_obj.currency, self.acct_obj.balance, self.acct_obj.date_opened

        # when confirmation is given by user
        self.display_frame = self.make_frame(background_color=bg)

        tk.Label(self.display_frame, text=f"UPDATE STATUS", font=("Calibri", 20, 'bold'),
                 bg=bg, fg=fg).grid(row=0, column=0, columnspan=2, sticky='nsew', padx=25)

        tk.Label(self.display_frame, text=f"ACCOUNT ID\n{self.acct_obj.account_id}",
                 font=("Calibri", 16, 'bold'), bg=bg, fg=fg).grid(row=1, column=1, sticky='nsew', padx=25)
        tk.Label(self.display_frame, text=f"CUSTOMER ID\n{self.acct_obj.customer_id}",
                 font=("Calibri", 16, 'bold'), bg=bg, fg=fg).grid(row=1, column=2, sticky='nsew', padx=25)
        tk.Label(self.display_frame, text=f"CURRENCY\n{self.acct_obj.currency}",
                 font=("Calibri", 16, 'bold'), bg=bg, fg=fg).grid(row=1, column=3, sticky='nsew', padx=25)
        tk.Label(self.display_frame, text=f"BALANCE\n{self.acct_obj.balance}",
                 font=("Calibri", 16, 'bold'), bg=bg, fg=fg).grid(row=2, column=1, sticky='nsew', padx=25)
        tk.Label(self.display_frame, text=f"DATE OPENED\n{self.acct_obj.date_opened}",
                 font=("Calibri", 16, 'bold'), bg=bg, fg=fg).grid(row=2, column=2, sticky='nsew', padx=25)
        tk.Label(self.display_frame, text="HAS BEEN UPDATED!!", font=("Calibri", 20, 'bold'),
                 bg=bg, fg=fg).grid(row=3, column=1, columnspan=2, sticky='NSEW', padx=25)

        tk.Button(self.display_frame, text='Accounts Page', font=("Calibri", 12, 'bold'), fg=bg, bg=fg,
                  height=1, width=15, command=self.acctpage).grid(row=4, column=2, padx=5, pady=5, stick='se')
        tk.Button(self.display_frame, text='Transactions Page', font=("Calibri", 12, 'bold'), fg=bg, bg=fg,
                  height=1, width=15, command=self.acctranspage).grid(row=4, column=1, padx=5, pady=5, stick='se')

        # save updated version to file
        with open(self.acct_obj.acct_data, 'w', encoding='utf8') as hand:
            for do, ai, ci, at, ab in zip(dates_opened, acct_ids, cust_ids, acct_types, acct_bals):
                if ai == selected_acctid:
                    # print(self.acct_obj.__dict__)
                    hand.writelines(f'{self.acct_obj.__dict__}\n')
                    continue
                dd = {'date_opened': do, 'account_id': ai, 'customer_id': ci, 'currency': at, 'balance': ab,
                      'acct_data': self.acct_obj.acct_data, 'acct_edits': self.acct_obj.acct_edits,
                      'acct_dels': self.acct_obj.acct_dels}
                # print(dd)
                hand.writelines(f'{dd}\n')

        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_frame is not None:
            self.edit_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        self.display_frame.rowconfigure([0, 1, 2, 3], weight=1)
        self.display_frame.columnconfigure(list(range(4)), weight=1)
        self.display_frame.grid(row=1, rowspan=4, column=0, columnspan=4, sticky='nsew')

    def alter_acctid_trans(self, selected_acctid, new_acctid):
        trans_ids, trans_dates, trans_acctids, trans_types, trans_amnts = self.acctrans_fields()  # all transactions
        with open(self.acctrans_obj.acctrans_data, 'w', encoding='utf8') as hand:
            for ti, td, ta, tt, tamt in zip(trans_ids, trans_dates, trans_acctids, trans_types, trans_amnts):
                if ta == selected_acctid:  #  where there is the old account id
                    ta = new_acctid  # set as new account id
                self.acctrans_obj.trans_id, self.acctrans_obj.trans_date, self.acctrans_obj.account_id, self.acctrans_obj.trans_type, self.acctrans_obj.amount = ti, td, ta, tt, tamt
                print(self.acctrans_obj.__dict__)
                hand.writelines(f'{self.acctrans_obj.__dict__}\n')

        print(f'transactions of {new_acctid} has been set')

    def save_edited_acct(self):
        with open(self.acct_obj.acct_edits, 'a', encoding='utf8') as hand:
            hand.writelines(f'{self.acct_obj.__dict__}\n')

    def acctranspage(self):
        # frame for customer accounts page containing three rows and one column
        self.sectionFrame = tk.LabelFrame(master=self.master, text='CUSTOMER TRANSACTIONS', font=('arial black', 12),
                                          bg='brown',
                                          fg='white')
        self.sectionFrame.rowconfigure([0, 1, 2, 3], weight=1)
        self.sectionFrame.columnconfigure(0, weight=1)

        # display sales options
        tk.Button(self.sectionFrame, text='VIEW TRANSACTIONS', bg='white', fg='green', font=('arial black', 14),
                  command=lambda: self.display_acctrans()).grid(row=0, padx=40, pady=10, sticky='nsew')
        tk.Button(self.sectionFrame, text='ENTER NEW TRANSACTION', bg='white', fg='blue',
                  font=('arial black', 14), command=self.new_acctrans).grid(row=1, padx=60, pady=10, sticky='nsew')
        tk.Button(self.sectionFrame, text='UPDATE TRANSACTION', bg='white', fg='orange',
                  font=('arial black', 14), command=self.edit_acctrans).grid(row=2, padx=80, pady=10, sticky='nsew')
        tk.Button(self.sectionFrame, text='DELETE TRANSACTION', bg='white', fg='red',
                  font=('arial black', 14), command=self.delete_acctrans).grid(row=3, padx=100, pady=10, sticky='nsew')

        # display inventory page's frame
        if self.display_frame is not None:
            self.display_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()
        if self.homeFrame is not None:
            self.homeFrame.grid_forget()

        self.sectionFrame.grid(row=1, rowspan=4, column=0, columnspan=5, sticky='nsew')

    def new_acctrans(self):
        global customer_ids, acct_ids, currencies, acct_bals, dates_opened
        bg, fg = 'orange', 'white'

        # frame for input of new inventory
        self.new_frame = tk.LabelFrame(self.master, text='REGISTER CUSTOMER TRANSACTION', font=('arial black', 12), bg=bg)
        self.new_frame.rowconfigure(list(range(6)), weight=1)
        self.new_frame.columnconfigure(list(range(5)), weight=1)

        # create a list of existing customer accounts
        dates_opened, acct_ids, cust_ids, acct_types, acct_bals = self.acct_fields()

        if len(acct_ids) < 1:
            return messagebox.showerror(title='No Existing Active Account',
                                        message='To register a new transaction\nYou must first create and activate a customer account')

        # place new account form
        # use company name to select customer ID
        tk.Label(self.new_frame, text='Select Customer:', font=('calibri', 13),
                 bg=bg, fg=fg, height=1).grid(row=0, column=0, padx=10, stick='nse')
        cacctCbox = ttk.Combobox(self.new_frame, value=acct_ids, font=('calibri', 13), width=24, state='readonly')
        cacctCbox.set(acct_ids[0])
        cacctCbox.grid(row=0, column=1, sticky='w')
        ttk.Button(self.new_frame, text='SELECT', command=lambda: self.popform(cacctCbox.get())
                   ).grid(row=0, column=2, sticky='w')

        tk.Button(self.new_frame, text='CANCEL', fg=bg, bg=fg,
                  font=('calibri', 13), command=lambda: self.acctranspage()).grid(row=0, column=3, sticky='e')

        # display inventory page's frame
        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.sectionFrame is not None:
            self.sectionFrame.grid_forget()
        self.new_frame.grid(row=1, rowspan=6, column=0, columnspan=3, sticky='nsew')
        
    def popform(self, selected_acctid):

        bg, fg = 'orange', 'white'

        acct_bal = self.get_bal(selected_acctid)

        # choose transaction type
        dorc = ['Debit', 'Credit']
        tk.Label(self.new_frame, text='Type: ', font=('calibri', 13),
                 bg=bg, fg=fg, height=1).grid(row=1, column=0, padx=10, stick='nse')
        self.deb_cred = ttk.Combobox(self.new_frame, value=dorc, font=('calibri', 13, 'bold'), width=5, state='readonly')
        self.deb_cred.set(dorc[0])
        self.deb_cred.grid(row=1, column=1, sticky='w')

        # amount
        tk.Label(self.new_frame, text='Enter Amount:', font=('calibri', 13),
                 bg=bg, fg=fg, height=1).grid(row=2, column=0, padx=10, stick='nse')
        self.amntEntry = tk.Entry(self.new_frame, font=('calibri', 13, 'bold'), fg='black', width=18)
        self.amntEntry.insert(0, '0')
        self.amntEntry.grid(row=2, column=1, sticky='w')

        tk.Label(self.new_frame, text='Current Balance', font=('calibri', 13),
                 bg=bg, fg=fg, height=1).grid(row=2, column=2, padx=10, stick='nse')
        self.balEntry = tk.Entry(self.new_frame, font=('calibri', 13, 'bold'), fg='black', width=18)
        self.balEntry.insert(0, str(acct_bal))
        self.balEntry.config(state='readonly')
        self.balEntry.grid(row=2, column=3, sticky='w')

        # transaction date
        # date of registration
        tk.Label(self.new_frame, text='Transaction Date:', font=('calibri', 13),
                 bg=bg, fg=fg, height=1).grid(row=3, column=0, padx=10, sticky='e')
        # day
        tk.Label(self.new_frame, text='Day', font=('calibri', 13),
                 bg=bg, fg=fg, height=1).grid(row=3, column=1, sticky='nw')
        self.transdayCbox = ttk.Combobox(self.new_frame, value=self.day, font=('calibri', 13, 'bold'), width=2,
                                         state='readonly')
        self.transdayCbox.set(str(datetime.date.today().day))
        self.transdayCbox.grid(row=3, column=1, padx=5, pady=30, sticky='w')
        # month
        tk.Label(self.new_frame, text='Month', font=('calibri', 13), bg=bg, fg=fg,
                 height=1).grid(row=3, column=2, sticky='nw')
        self.transmonthCbox = ttk.Combobox(self.new_frame, value=[v for k, v in self.month.items()],
                                           font=('calibri', 13, 'bold'), width=4, state='readonly')
        self.transmonthCbox.set(self.month[datetime.date.today().month])
        self.transmonthCbox.grid(row=3, column=2, padx=5, pady=30, sticky='w')
        # year
        tk.Label(self.new_frame, text='Year', font=('calibri', 13), bg=bg, fg=fg,
                 height=1).grid(row=3, column=3, sticky='nw')
        self.transyrCbox = ttk.Combobox(self.new_frame, value=self.year, font=('calibri', 13, 'bold'), width=4,
                                        state='readonly')
        self.transyrCbox.set(str(datetime.date.today().year))
        self.transyrCbox.grid(row=3, column=3, pady=30, sticky='w')

        ttk.Button(self.new_frame, text='ACCOUNTS MENU', width=18,
                   command=self.acctpage).grid(row=5, column=1, padx=5, stick='e')

        tk.Button(self.new_frame, text='ENTER TRANSACTION', fg='green', bg='white',
                  font=('calibri', 13), command=lambda: self.submit_acctrans(selected_acctid)).grid(row=5, column=3, sticky='e')

    def submit_acctrans(self, selected_acctid):
        global customer_ids, acct_ids, currencies, acct_bals, dates_opened
        bg, fg = 'orange', 'white'

        self.submit_frame = tk.LabelFrame(self.master, text='DO YOU WANT TO SAVE?', fg=fg, bg=bg,
                                          font=('arial black', 12))
        self.submit_frame.rowconfigure(list(range(4)), weight=1)
        self.submit_frame.columnconfigure(list(range(4)), weight=1)

        acctid, type, amnt, bal = selected_acctid, self.deb_cred.get(), self.amntEntry.get(), self.balEntry.get()
        tdate = f'{self.transyrCbox.get()}-{self.transmonthCbox.get()}-{self.transdayCbox.get()}'
        
        wspace = string.whitespace
        
        # run necessary checks
        # check for empty field
        if amnt in wspace:
            return messagebox.showerror(title='Blank Field', message='BLANK FIELD(S) DETECTED!')

        # check for fields with invalid data types
        try:
            if float(amnt) <= 0:
                return messagebox.showerror(title='Invalid Amount',
                                            message=f'{amnt} is not a valid amount\nPlease enter a positive amount!')
            if type == 'Debit' and float(amnt) > float(bal):
                return messagebox.showerror(title='Insufficient Funds',
                                            message=f'DEBIT amount: {amnt} cannot exceed your current balance: {bal}')
        except ValueError as VE:
            # non-figures have been entered, if no error was raised
            return messagebox.showerror(title='Invalid Data Type',
                                        message=f'Amount: {amnt} and/or Balance: {bal} is not a number')

        # if transaction id is existing, simply continue
        trans = self.get_active_acctrans()
        if trans is None:  # if no prior transaction
            # print(trans)  # this should be None
            start = uniqueid()  # randomly generate a ten-digit number as the starting sequence
            seq = next(start)  # return the generator value
        else:  # if there are existing transactions
            print(trans)
            seq = max([int(ind) for ind in trans['trans_id']]) + 1  # simply increment last/maximum number in the sequence by 1

        self.acctrans_obj.trans_id = f'{seq}'
        self.acctrans_obj.account_id, self.acctrans_obj.trans_type = acctid, type
        self.acctrans_obj.amount, self.acctrans_obj.trans_date = amnt, tdate
        print(self.acctrans_obj.__dict__)

        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg=bg, fg=fg,
                 text=f"TRANSACTION ID\n{self.acctrans_obj.trans_id}").grid(row=0, column=0, sticky='ew')
        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg=bg, fg=fg,
                 text=f"ACCOUNT ID\n{self.acctrans_obj.account_id}").grid(row=0, column=1, sticky='ew')
        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg=bg, fg=fg,
                 text=f"TRANSACTION TYPE\n{self.acctrans_obj.trans_type}").grid(row=0, column=2, sticky='ew')
        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg=bg, fg=fg,
                 text=f"AMOUNT\n{self.acctrans_obj.amount}").grid(row=0, column=3, sticky='ew')
        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg=bg, fg=fg,
                 text=f"TRANSACTION DATE\n{self.acctrans_obj.trans_date}").grid(row=0, column=4, sticky='ew')

        # save and cancel buttons
        tk.Button(self.submit_frame, text='Save', font=("Calibri", 14, 'bold'), fg='green', bg='white',
                  height=3, width=10, command=self.saveacctrans).grid(row=3, column=0, padx=5, stick='ew')
        tk.Button(self.submit_frame, text='Cancel', font=("Calibri", 14, 'bold'), bg='red', fg='white',
                  height=3, width=10, command=self.new_acctrans).grid(row=3, column=3, padx=5, stick='ew')
        tk.Button(self.submit_frame, text='ACCOUNTS MENU', font=("Calibri", 14, 'bold'), bg='green', fg='white',
                  height=3, width=18, command=self.acctpage).grid(row=4, column=1, padx=5, stick='e')

        if self.display_frame is not None:
            self.display_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()
            
        self.submit_frame.grid(row=1, sticky='nsew')
        
    def saveacctrans(self):
        bg, fg = 'orange', 'white'
        with open(self.acctrans_obj.acctrans_data, 'a',
                  encoding='utf8') as hand:
            hand.writelines(f"{self.acctrans_obj.__dict__}\n")

        self.submit_frame = self.make_frame(background_color=bg)

        tk.Label(self.submit_frame, text='NEW CUSTOMER TRANSACTION HAS BEEN ADDED!', font=("arial", 14, 'bold'),
                 bg=bg, fg=fg).grid(row=0, column=0, columnspan=4, sticky='nsew')

        tk.Button(self.submit_frame, text='Add Another', font=("Calibri", 14, 'bold'), bg='blue', fg=fg,
                  height=5, width=15, command=self.new_acctrans).grid(row=1, column=0, padx=5, stick='ew')

        tk.Button(self.submit_frame, text='Accounts Page', font=("Calibri", 14, 'bold'), fg=bg, bg=fg,
                  height=5, width=15, command=self.acctranspage()).grid(row=1, column=3, padx=5, stick='ew')

        self.submit_frame.rowconfigure([0, 1], weight=1)
        self.submit_frame.columnconfigure(list(range(4)), weight=1)
        self.submit_frame.grid(row=1, sticky='nsew')

    def read_acctrans(self):
        with open(self.acctrans_obj.acctrans_data, 'r', encoding='utf8') as hand:
            # customer atributes is a list of record strings
            acctrans_atr = hand.readlines()
        return acctrans_atr

    def display_acctrans(self):
        global customer_ids, acct_ids, currencies, acct_bals, dates_opened
        global acctdata
        bg, fg = 'orange', 'white'

        # setup display frame
        self.display_frame = self.make_frame(page_title="CUSTOMER'S FINANCIAL ACTIVITIES", background_color=bg)

        tk.Button(self.display_frame, text='Transactions Page', font=("Calibri", 12, 'bold'), fg=bg, bg=fg, height=1,
                  width=15, command=self.acctranspage).grid(row=2, column=3, padx=5, pady=5, stick='se')

        # create a list of existing customer accounts
        acctdata = self.read_acct()

        # creating a list of customer account details for each customer
        acct_ids = [v for line in acctdata for k, v in eval(line).items() if k == 'account_id']
        
        if len(acct_ids) < 1:
            return messagebox.showerror(title='No Existing Active Account', 
                                        message='There are no available transactions to display')
        # select account id
        tk.Label(self.display_frame, text='Select Customer Account:', font=('calibri', 13),
                 bg=bg, fg=fg, height=1).grid(row=0, column=0, padx=10, stick='nse')
        cacct_Cbox = ttk.Combobox(self.display_frame, value=acct_ids, font=('calibri', 13), width=24, state='readonly')
        cacct_Cbox.set(acct_ids[0])
        cacct_Cbox.grid(row=0, column=1, sticky='w')
        ttk.Button(self.display_frame, text='SELECT', command=lambda: self.pop_view(cacct_Cbox.get())
                   ).grid(row=0, column=2, sticky='w')

        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_frame is not None:
            self.edit_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        self.display_frame.rowconfigure(list(range(3)), weight=1)
        self.display_frame.columnconfigure(list(range(9)), weight=1)
        self.display_frame.grid(row=1, rowspan=2, column=0, columnspan=4, sticky='nsew')

    def pop_view(self, selected_acctid):
        global customer_ids, acct_ids, currencies, acct_bals, dates_opened, acctdata
        # global trans_dates, trans_types, trans_acctids, trans_amnts
        bg, fg = 'orange', 'white'

        acct = self.fetch_acct(selected_acctid)  # customer's account information
        for k, v in acct.items():
            if k == 'currency':
                acct_type = v
            if k == 'balance':
                acct_bal = float(v)

        trans = self.get_active_acctrans(selected_acctid)

        if trans is None:
            return messagebox.showinfo(title='Inactive Account Selected',
                message=f'{selected_acctid} is inactive,\nPlease activate or\n\nSelect an active account to view')
                
        # display headings for customer records
        # create scrolled text field to display customer records
        st = scrolledtext.ScrolledText(self.display_frame, bg=bg, fg=fg, wrap='word',
                                       font=("Calibri", 14, 'bold'), relief='flat')
        st.grid(row=0, column=0, columnspan=8, sticky='nsew')
        # display headings for customer records
        st.insert(index='end',
                  chars='TRANSACTION ID, TRANSACTION DATE, ACCOUNT ID, TRANSACTION TYPE, AMOUNT, BALANCE\n\n')
        # print(len([v for k, v in trans.items() if k == 'trans_date'][0]), trans)
        for ind in range(len([v for k, v in trans.items() if k == 'trans_date'][0])):
            # print(ind)
            if trans['trans_type'][ind] == 'Credit':
                acct_bal += float(trans['amount'][ind])
            else:  #if trans['trans_type'][ind] == 'Debit':
                acct_bal -= float(trans['amount'][ind])

            # print(acct_bal, trans['trans_type'][ind], float(trans['amount'][ind]))

            st.insert(index='end',
                      chars=f"{trans['trans_id'][ind]},\t"
                            f"{trans['trans_date'][ind]},\t"
                            f" {trans['account_id'][ind]},\t"
                            f"{trans['trans_type'][ind]},\t"
                            f"{acct_type}{trans['amount'][ind]},\t"
                            f"{acct_type}{acct_bal}\n\n")

        # make text field read-only
        st.config(state='disabled')
        # ensure that text can be copied to clipboard
        st.bind('<1>', lambda event: st.focus_set())

    def get_active_acctrans(self, selected_acctid=None):
        '''
        to generate a dictionary of transaction fields for the same account
        :return:
        '''
        trans_ids, trans_dates, trans_acctids, trans_types, trans_amnts = self.acctrans_fields()

        trans = {'trans_id': [], 'trans_date': [], 'account_id': [], 'trans_type': [], 'amount': []}
        Empty = True

        for i, d, ai, tt, tamt in zip(trans_ids, trans_dates, trans_acctids, trans_types, trans_amnts):
            if ai == selected_acctid:  # return selected transaction at trans id
                trans['trans_id'].append(i), trans['trans_date'].append(d), trans['account_id'].append(ai), trans['trans_type'].append(tt), trans[
                    'amount'].append(tamt)
                Empty = False

            elif selected_acctid is None:  # return all transactions
                trans['trans_id'].append(i), trans['trans_date'].append(d), trans['account_id'].append(ai), trans[
                    'trans_type'].append(tt), trans[
                    'amount'].append(tamt)
                Empty = False

        if Empty:
            return None
        return trans

    def fetch_transaction(self, selected_transid):
        trans_ids, trans_dates, trans_acctids, trans_types, trans_amnts = self.acctrans_fields()

        trans = {'trans_id': None, 'trans_date': None, 'account_id': None, 'trans_type': None, 'amount': None}

        for i, d, ai, tt, tamt in zip(trans_ids, trans_dates, trans_acctids, trans_types, trans_amnts):
            if i == selected_transid:  # return selected transaction at trans id
                trans['trans_id'], trans['trans_date'], trans['account_id'], trans['trans_type'], trans['amount'] = i, d, ai, tt, tamt
        return trans

    def acctrans_fields(self):
        '''
        to generate a tuple of lists containing transactions in separate fields
        :return:--> (trans_ids, trans_dates, trans_acctids, trans_types, trans_amnts)
        '''
        with open(self.acctrans_obj.acctrans_data, 'r', encoding='utf8') as hand:
            acctransdata = hand.readlines()

        # creating a list of customer transaction fields for each transaction
        trans_ids = [v for line in acctransdata for k, v in eval(line).items() if k == 'trans_id']
        trans_dates = [v for line in acctransdata for k, v in eval(line).items() if k == 'trans_date']
        trans_acctids = [v for line in acctransdata for k, v in eval(line).items() if k == 'account_id']
        trans_types = [v for line in acctransdata for k, v in eval(line).items() if k == 'trans_type']
        trans_amnts = [v for line in acctransdata for k, v in eval(line).items() if k == 'amount']

        return trans_ids, trans_dates, trans_acctids, trans_types, trans_amnts

    def edit_acctrans(self):
        bg, fg = 'brown', 'white'
        # setup display frame
        self.display_frame = self.make_frame(page_title='UPDATE CUSTOMER TRANSACTIONS', background_color=bg)
        
        tk.Button(self.display_frame, text='Transactions Page', font=("Calibri", 12, 'bold'), fg=bg, bg=fg, height=1,
                  width=15, command=self.acctranspage).grid(row=2, column=3, padx=5, pady=5, stick='se')
        dates_opened, acct_ids, cust_ids, acct_types, acct_bals = self.acct_fields()
        
        if len(acct_ids) < 1:
            return messagebox.showerror(title='No Existing Active Account', 
                                        message='There are no transactions available for update')
        
        # select account id
        tk.Label(self.display_frame, text='Select Account:', font=('calibri', 13),
                 bg=bg, fg=fg, height=1).grid(row=0, column=0, padx=10, stick='nse')
        cacct_Cbox = ttk.Combobox(self.display_frame, value=acct_ids, font=('calibri', 13), width=24, state='readonly')
        cacct_Cbox.set(acct_ids[0])
        cacct_Cbox.grid(row=0, column=1, sticky='w')
        ttk.Button(self.display_frame, text='SELECT', command=lambda: self.pop_edit_acctrans_form(cacct_Cbox.get())
                   ).grid(row=0, column=2, sticky='w')

        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_frame is not None:
            self.edit_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        self.display_frame.rowconfigure(list(range(3)), weight=1)
        self.display_frame.columnconfigure(list(range(9)), weight=1)
        self.display_frame.grid(row=1, rowspan=2, column=0, columnspan=4, sticky='nsew')
        
    def pop_edit_acctrans_form(self, selected_acctid):
        global trans, acct_bal
        bg, fg = 'brown', 'white'

        acct_bal = self.get_bal(selected_acctid)

        acct = self.fetch_acct(selected_acctid)  # customer's account information
        for k, v in acct.items():
            if k == 'currency':
                acct_type = v
            if k == 'balance':
                acct_bal = float(v)

        trans = self.get_active_acctrans(selected_acctid)  # customer's transactions

        if trans is None:
            return messagebox.showinfo(title='Inactive Account Selected',
                                       message=f'{selected_acctid} is inactive,\nPlease activate or\n\nSelect an active account to view')

        # display headings for customer records
        # create scrolled text field to display customer records
        st = scrolledtext.ScrolledText(self.display_frame, bg=bg, fg=fg, wrap='word',
                                       font=("Calibri", 14, 'bold'), relief='flat')
        st.grid(row=0, column=0, columnspan=8, sticky='nsew')
        # display headings for customer records
        st.insert(index='end',
                  chars='TRANSACTION ID, TRANSACTION DATE, ACCOUNT ID, TRANSACTION TYPE, AMOUNT, BALANCE\n\n')
        # print(len([v for k, v in trans.items() if k == 'trans_date'][0]), trans)
        for ind in range(len([v for k, v in trans.items() if k == 'trans_date'][0])):
            print(ind)
            if trans['trans_type'][ind] == 'Credit':
                acct_bal += float(trans['amount'][ind])
            else:  # if trans['trans_type'][ind] == 'Debit':
                acct_bal -= float(trans['amount'][ind])

            # print(acct_bal, trans['trans_type'][ind], float(trans['amount'][ind]))

            st.insert(index='end',
                      chars=f"{trans['trans_id'][ind]},\t"
                            f"{trans['trans_date'][ind]},\t"
                            f" {trans['account_id'][ind]},\t"
                            f"{trans['trans_type'][ind]},\t"
                            f"{acct_type}{trans['amount'][ind]},\t"
                            f"{acct_type}{acct_bal}\n\n")
        # make text field read-only
        st.config(state='disabled')
        # ensure that text can be copied to clipboard
        st.bind('<1>', lambda event: st.focus_set())

        # to edit the given row number (at row entry - 1)
        tk.Label(self.display_frame, text='SELECT TRANSACTION ID:', font=("Calibri", 12, 'bold'), bg=bg,
                 fg=fg).grid(row=2, column=0, padx=2, sticky='e')
        # select transid
        edit_transidCbox = ttk.Combobox(self.display_frame, width=12, value=trans['trans_id'], font=("Calibri", 12, 'bold'), state='readonly')
        edit_transidCbox.set(trans['trans_id'][0])
        edit_transidCbox.grid(row=2, column=1, sticky='w')

        # edit button
        ttk.Button(self.display_frame, text='Edit', width=10, command=lambda:
        self.editing_acctrans(edit_transidCbox.get())).grid(row=2, column=2, sticky='w')

    def editing_acctrans(self, selected_transid):
        global trans, acct_bal
        bg, fg = 'brown', 'white'
        self.display_frame = self.make_frame(page_title='EDIT SELECTED TRANSACTION', background_color=bg)

        trans = self.get_active_acctrans()
        # print(trans)

        for ind in range(len([v for k, v in trans.items() if k == 'trans_date'][0])):  # fetch the particular transaction for editing
            if trans['trans_id'][ind] == selected_transid:
                self.acctrans_obj.trans_id, self.acctrans_obj.account_id, self.acctrans_obj.trans_type, self.acctrans_obj.amount, self.acctrans_obj.trans_date = trans['trans_id'][ind], trans['account_id'][ind], trans['trans_type'][ind], trans['amount'][ind], trans['trans_date'][ind]

        # print(f"Copied: {self.acctrans_obj.__dict__}")
        # display editable fields in entries for user
        tk.Label(self.display_frame, text="TRANSACTION ID", font=("Calibri", 12, 'bold'),
                 bg=bg, fg=fg).grid(row=1, column=0, sticky='sw', padx=25, pady=15)
        self.trid_entry = tk.Entry(self.display_frame, font=("Calibri", 12, 'bold'))
        self.trid_entry.insert(0, string=f'{self.acctrans_obj.trans_id}')
        self.trid_entry.config(state='disabled')
        self.trid_entry.grid(row=2, column=0, sticky='w', padx=25, pady=5)

        tk.Label(self.display_frame, text="ACCOUNT ID", font=("Calibri", 12, 'bold'),
                 bg=bg, fg=fg).grid(row=1, column=1, sticky='sw', padx=25, pady=15)
        self.traid_entry = tk.Entry(self.display_frame, font=("Calibri", 12, 'bold'))
        self.traid_entry.insert(0, string=f'{self.acctrans_obj.trans_id}')
        self.traid_entry.config(state='disabled')
        self.traid_entry.grid(row=2, column=1, sticky='w', padx=25, pady=5)

        tk.Label(self.display_frame, text="DATE OF TRANSACTION", font=("Calibri", 12, 'bold'),
                 bg=bg, fg=fg).grid(row=1, column=2, sticky='sw', padx=25, pady=15)
        self.trdate_entry = tk.Entry(self.display_frame, font=("Calibri", 12, 'bold'))
        self.trdate_entry.insert(0, string=f'{self.acctrans_obj.trans_date}')
        self.trdate_entry.config(state='disabled')
        self.trdate_entry.grid(row=2, column=2, sticky='w', padx=25, pady=5)

        dorc = ['Debit', 'Credit']
        tk.Label(self.display_frame, text="TYPE OF TRANSACTION", font=("Calibri", 12, 'bold'),
                 bg=bg, fg=fg).grid(row=3, column=0, sticky='sw', padx=25, pady=15)
        self.trtyp_Cbox = ttk.Combobox(self.display_frame, font=("Calibri", 12, 'bold'), state='readonly', value=dorc)
        self.trtyp_Cbox.set(f'{self.acctrans_obj.trans_type}')
        self.trtyp_Cbox.grid(row=4, column=0, sticky='w', padx=25, pady=5)

        tk.Label(self.display_frame, text="AMOUNT", font=("Calibri", 12, 'bold'),
                 bg=bg, fg=fg).grid(row=3, column=1, sticky='sw', padx=25, pady=15)
        self.tramt_entry = tk.Entry(self.display_frame, font=("Calibri", 12, 'bold'))
        self.tramt_entry.insert(0, string=f'{self.acctrans_obj.amount}')
        self.tramt_entry.grid(row=4, column=1, sticky='w', padx=25, pady=5)

        tk.Label(self.display_frame, text="CURRENT BALANCE", font=("Calibri", 12, 'bold'),
                 bg=bg, fg=fg).grid(row=3, column=2, sticky='sw', padx=25, pady=15)
        self.trbal_entry = tk.Entry(self.display_frame, font=("Calibri", 12, 'bold'))
        self.trbal_entry.insert(0, string=f'{acct_bal}')
        self.trbal_entry.grid(row=4, column=2, sticky='w', padx=25, pady=5)

        # update and customer page buttons
        tk.Button(self.display_frame, text='Update', font=("Calibri", 12, 'bold'),
                  bg='orange', fg='white', height=1, width=15, command=self.update_acctrans).grid(row=6, column=1, padx=5,
                                                                                              pady=5, stick='w')

        tk.Button(self.display_frame, text='Transaction Page', font=("Calibri", 12, 'bold'),
                  bg='blue', fg='white', height=1, width=15, command=self.acctranspage).grid(row=6, column=2, padx=5,
                                                                                         pady=5, stick='e')

        # clear the frames before and after this page
        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_frame is not None:
            self.edit_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        # display an adjustible frame containing the selected info
        self.display_frame.rowconfigure(list(range(7)), weight=1)
        self.display_frame.columnconfigure(list(range(4)), weight=1)
        self.display_frame.grid(row=1, rowspan=2, column=0, columnspan=4, sticky='nsew')

    def update_acctrans(self):
        global trans, acct_bal
        bg, fg = 'brown', 'white'
        typ, amnt = self.trtyp_Cbox.get(), self.tramt_entry.get()

        try:
            if float(amnt) <= 0:
                return messagebox.showerror(message='You have entered a bad value into the Amount fields')
            elif type == 'Debit' and acct_bal < float(amnt):
                return messagebox.showerror(message=f'Amount: {amnt} cannot exceed current Balance {acct_bal}')


        except ValueError:
            return messagebox.showerror(message='Please Check The Following Fields: \nTransaction Type, \nAmount fields')

        if (typ == self.acctrans_obj.trans_type) and (amnt == self.acctrans_obj.amount):
            return messagebox.showerror(title='Same Values As Values',
                                        message='No Changes Made!\n\nPlease Check The Following Fields: \nTransaction Type, \nAmount fields')

        if not(messagebox.askyesno(message='Do You Want To Save Changes Made?')):
            messagebox.showinfo(message='No Changes Made')
            return self.edit_acctrans()

        self.save_edited_acctrans()  # save entry before changes made is implemented

        if typ != self.acctrans_obj.trans_type:
            self.acctrans_obj.trans_type = typ
        if amnt != self.acctrans_obj.amount:
            self.acctrans_obj.amount = amnt
        # print(self.acctrans_obj.__dict__)

        # print(f'Old: {trans}')
        for ind in range(len([v for k, v in trans.items() if k == 'trans_date'][0])):  # fetch the particular transaction for editing
            if trans['trans_id'][ind] == self.acctrans_obj.trans_id:
                trans['trans_id'][ind], trans['account_id'][ind], trans['trans_type'][ind], trans['amount'][ind], trans['trans_date'][ind] = self.acctrans_obj.trans_id, self.acctrans_obj.account_id, self.acctrans_obj.trans_type, self.acctrans_obj.amount, self.acctrans_obj.trans_date
        # print(f'New: {trans}')

        # save updated version to file
        with open(self.acctrans_obj.acctrans_data, 'w', encoding='utf8') as hand:
            trans_len = [len(v) for k, v in trans.items() if k == 'trans_id'][0]
            for ind in range(trans_len):
                curr_dict = {k: v[ind] for k, v in trans.items()}
                # print(ind, curr_dict)
                hand.writelines(f"{curr_dict}\n")

        # when confirmation is given by user
        self.display_frame = self.make_frame(background_color=bg)

        tk.Label(self.display_frame, text=f"TRANSACTION STATUS", font=("Calibri", 20, 'bold'),
                 bg=bg, fg=fg).grid(row=0, column=0, columnspan=2, sticky='nsew', padx=25)

        tk.Label(self.display_frame, text=f"TRANSACTION ID\n{self.acctrans_obj.trans_id}", font=("Calibri", 16, 'bold'),
                 bg=bg, fg=fg).grid(row=1, column=1, sticky='nsew', padx=25)

        tk.Label(self.display_frame, text=f"ACCOUNT ID\n{self.acctrans_obj.account_id}", font=("Calibri", 16, 'bold'),
                 bg=bg, fg=fg).grid(row=1, column=2, sticky='nsew', padx=25)

        tk.Label(self.display_frame, text=f"TRANSACTION DATE\n{self.acctrans_obj.trans_date}", font=("Calibri", 16, 'bold'),
                 bg=bg, fg=fg).grid(row=1, column=0, sticky='nsew', padx=25)

        tk.Label(self.display_frame, text=f"TRANSACTION TYPE\n{self.acctrans_obj.trans_type}", font=("Calibri", 16, 'bold'),
                 bg=bg, fg=fg).grid(row=2, column=0, sticky='nsew', padx=25)

        tk.Label(self.display_frame, text=f"AMOUNT\n{self.acctrans_obj.amount}", font=("Calibri", 16, 'bold'),
                 bg=bg, fg=fg).grid(row=2, column=1, sticky='nsew', padx=25)

        tk.Label(self.display_frame, text="HAS BEEN UPDATED!!", font=("Calibri", 20, 'bold'),
                 bg=bg, fg=fg).grid(row=3, column=1, columnspan=2, sticky='NSEW', padx=25)

        tk.Button(self.display_frame, text='Transactions Page', font=("Calibri", 12, 'bold'),
                             fg=bg, bg=fg, height=1, width=15, command=self.acctranspage).grid(row=4, column=2, padx=5, pady=5, stick='se')

        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_frame is not None:
            self.edit_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        self.display_frame.rowconfigure([0, 1, 2, 3], weight=1)
        self.display_frame.columnconfigure(list(range(4)), weight=1)
        self.display_frame.grid(row=1, rowspan=4, column=0, columnspan=4, sticky='nsew')

    def save_edited_acctrans(self):
        with open(self.acctrans_obj.acctrans_edits, 'a', encoding='utf8') as hand:
            hand.writelines(f'{self.acctrans_obj.__dict__}\n')
    
    def delete_acctrans(self):
        bg, fg = 'red', 'white'
        # setup display frame
        self.display_frame = self.make_frame(page_title='DELETE CUSTOMER TRANSACTIONS', background_color=bg)
        
        tk.Button(self.display_frame, text='Transactions Page', font=("Calibri", 12, 'bold'), fg=bg, bg=fg, height=1,
                  width=15, command=self.acctranspage).grid(row=2, column=3, padx=5, pady=5, stick='se')
        dates_opened, acct_ids, cust_ids, acct_types, acct_bals = self.acct_fields()

        if len(acct_ids) < 1:
            return messagebox.showerror(title='No Existing Active Account',
                                        message='There are no transactions available for deletion')

        # select account id
        tk.Label(self.display_frame, text='Select Account:', font=('calibri', 13),
                 bg=bg, fg=fg, height=1).grid(row=0, column=0, padx=10, stick='nse')
        cacct_Cbox = ttk.Combobox(self.display_frame, value=acct_ids, font=('calibri', 13), width=24, state='readonly')
        cacct_Cbox.set(acct_ids[0])
        cacct_Cbox.grid(row=0, column=1, sticky='w')
        ttk.Button(self.display_frame, text='SELECT', command=lambda: self.pop_del_acctrans_form(cacct_Cbox.get())
                   ).grid(row=0, column=2, sticky='w')

        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_frame is not None:
            self.edit_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        self.display_frame.rowconfigure(list(range(3)), weight=1)
        self.display_frame.columnconfigure(list(range(9)), weight=1)
        self.display_frame.grid(row=1, rowspan=2, column=0, columnspan=4, sticky='nsew')
        
    def pop_del_acctrans_form(self, selected_acctid):
        global trans, acct_bal, all_trans
        bg, fg = 'red', 'white'

        acct_bal = self.get_bal(selected_acctid)

        acct = self.fetch_acct(selected_acctid)  # customer's account information
        for k, v in acct.items():
            if k == 'currency':
                acct_type = v
            if k == 'balance':
                acct_bal = float(v)

        trans = self.get_active_acctrans(selected_acctid)  # selected account transactions
        all_trans = self.get_active_acctrans()  # all transactions

        if trans is None:
            return messagebox.showinfo(title='Inactive Account Selected',
                                       message=f'{selected_acctid} is inactive,\nPlease activate or\n\nSelect an active account to view')

        # display headings for customer records
        # create scrolled text field to display customer records
        st = scrolledtext.ScrolledText(self.display_frame, bg=bg, fg=fg, wrap='word',
                                       font=("Calibri", 14, 'bold'), relief='flat')
        st.grid(row=0, column=0, columnspan=8, sticky='nsew')
        # display headings for customer records
        st.insert(index='end',
                  chars='TRANSACTION ID, TRANSACTION DATE, ACCOUNT ID, TRANSACTION TYPE, AMOUNT, BALANCE\n\n')
        # print(len([v for k, v in trans.items() if k == 'trans_date'][0]), trans)
        for ind in range(len([v for k, v in trans.items() if k == 'trans_date'][0])):
            print(ind)
            if trans['trans_type'][ind] == 'Credit':
                acct_bal += float(trans['amount'][ind])
            else:  # if trans['trans_type'][ind] == 'Debit':
                acct_bal -= float(trans['amount'][ind])

            # print(acct_bal, trans['trans_type'][ind], float(trans['amount'][ind]))

            st.insert(index='end',
                      chars=f"{trans['trans_id'][ind]},\t"
                            f"{trans['trans_date'][ind]},\t"
                            f" {trans['account_id'][ind]},\t"
                            f"{trans['trans_type'][ind]},\t"
                            f"{acct_type}{trans['amount'][ind]},\t"
                            f"{acct_type}{acct_bal}\n\n")
        # make text field read-only
        st.config(state='disabled')
        # ensure that text can be copied to clipboard
        st.bind('<1>', lambda event: st.focus_set())

        # to edit the given row number (at row entry - 1)
        tk.Label(self.display_frame, text='SELECT TRANSACTION ID:', font=("Calibri", 12, 'bold'), bg=bg,
                 fg=fg).grid(row=2, column=0, padx=2, sticky='e')
        # select transid
        edit_transidCbox = ttk.Combobox(self.display_frame, width=12, value=trans['trans_id'],
                                        font=("Calibri", 12, 'bold'), state='readonly')
        edit_transidCbox.set(trans['trans_id'][0])
        edit_transidCbox.grid(row=2, column=1, sticky='w')

        # edit button
        ttk.Button(self.display_frame, text='Delete', width=10, command=lambda:
        self.erase_acctrans(edit_transidCbox.get())).grid(row=2, column=2, sticky='w')
        
    def erase_acctrans(self, selected_transid):
        global trans, acct_bal, all_trans
        bg, fg = 'red', 'white'
  
        self.display_frame = self.make_frame(page_title='RECORD DELETED', background_color=bg)

        sel_trans = self.fetch_transaction(selected_transid)  # customer's transactions
        print(f'Selected Transaction: {sel_trans}')

        self.acctrans_obj.__dict__.update(sel_trans)
        print(f'Instance: {self.acctrans_obj.__dict__}')

        retainer = {'trans_id': [], 'trans_date': [], 'account_id': [], 'trans_type': [], 'amount': []}  # to retain all transactions except the selected transaction

        for ind in range(len(
                [v for k, v in all_trans.items() if k == 'trans_date'][0])):  # fetch all  except that particular transaction
            if all_trans['trans_id'][ind] == selected_transid:
                continue
            retainer['trans_id'].append(all_trans['trans_id'][ind]), retainer['account_id'].append(all_trans['account_id'][ind])
            retainer['trans_type'].append(all_trans['trans_type'][ind]), retainer['amount'].append(all_trans['amount'][ind])
            retainer['trans_date'].append(all_trans['trans_date'][ind])

        print(f"All Transactions: {all_trans}\nRetained Transactions: {retainer}")

        if not (messagebox.askyesno(title='CONFIRM DELETE', message='Do You Want To Delete?')):
            return messagebox.showinfo(message='RECORD NOT DELETED')

        with open(self.acctrans_obj.acctrans_data, 'w', encoding='utf8') as hand:
            retainer_len = [len(v) for k, v in retainer.items() if k == 'trans_id'][0]
            for ind in range(retainer_len):
                curr_dict = {k: v[ind] for k, v in retainer.items()}
                # print(ind, curr_dict)
                hand.writelines(f"{curr_dict}\n")

        self.save_del_acctrans()

        st = scrolledtext.ScrolledText(self.display_frame, bg=bg, fg=fg, font=("Calibri", 14, 'bold'), relief='flat')
        st.insert(index='1.0', chars='TRANSACTIION ID,\tACCOUNT ID,\tTRANSACTION DATE,\tTRANSACTION TYPE,\nAMOUNT\n\n'
                                     f'{self.acctrans_obj.trans_id}, {self.acctrans_obj.account_id}, {self.acctrans_obj.trans_type}, {self.acctrans_obj.amount}, {self.acctrans_obj.trans_date}\n\n'
                                     'HAS BEEN DELETED!!')

        st.grid(row=0, column=0, columnspan=10, sticky='ew')

        tk.Button(self.display_frame, text='Transaction Page', font=("Calibri", 12, 'bold'),
                             fg=bg, bg=fg, height=1, width=15, command=self.acctranspage).grid(row=3, column=3, padx=5, pady=5, stick='se')

        self.display_frame.rowconfigure(list(range(4)), weight=1)
        self.display_frame.columnconfigure(list(range(4)), weight=1)
        self.display_frame.grid(row=1, rowspan=3, column=0, columnspan=4, sticky='nsew')

    def save_del_acctrans(self):
        with open(self.acctrans_obj.acctrans_dels, 'a', encoding='utf8') as hand:
            hand.writelines(f'{self.acctrans_obj.__dict__}\n')

    def custpage(self):
        # frame for customer page containing three rows and one column
        self.sectionFrame = tk.LabelFrame(master=self.master, text='CUSTOMER', font=('arial black', 12), bg='blue',
                                      fg='white')
        self.sectionFrame.rowconfigure([0, 1, 2], weight=1)
        self.sectionFrame.columnconfigure(0, weight=1)

        # display customer options
        tk.Button(self.sectionFrame, text='ADD NEW CUSTOMER', bg='white', fg='blue',
                                font=('arial black', 14), command=self.new_cust).grid(row=1, padx=60, pady=10, sticky='nsew')
        tk.Button(self.sectionFrame, text='UPDATE CUSTOMER RECORD', bg='white', fg='orange',
                              font=('arial black', 14), command=self.edit_cust).grid(row=2, padx=80, pady=10, sticky='nsew')
        tk.Button(self.sectionFrame, text='VIEW CUSTOMER RECORDS', bg='white', fg='green',
                              font=('arial black', 14), command=lambda: self.display_cust()).grid(row=0, padx=40, pady=10, sticky='nsew')
        # tk.Button(self.sectionFrame, text='DELETE CUSTOMER RECORD', bg='white', fg='red',
        #           font=('arial black', 14), command=self.delete_cust).grid(row=3, padx=100, pady=10, sticky='nsew')

        # display inventory page's frame
        if self.display_frame is not None:
            self.display_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()
        if self.homeFrame is not None:
            self.homeFrame.grid_forget()

        self.sectionFrame.grid(row=1, rowspan=4, column=0, columnspan=5, sticky='nsew')

    def new_cust(self):
        bg, fg = 'blue', 'white'

        # frame for input of new inventory
        self.new_frame = tk.LabelFrame(self.master, text='NEW CUSTOMER REGISTRATION', fg=fg, font=('arial black', 12),
                                            bg=bg)
        self.new_frame.rowconfigure(list(range(9)), weight=1)
        self.new_frame.columnconfigure(list(range(5)), weight=1)

        # place new customer form
        # customer Name
        tk.Label(self.new_frame, text='Customer', font=('calibri', 16),
                 bg=bg, fg=fg, height=1).grid(row=0, column=0, padx=10, stick='nsew')
        # first name
        tk.Label(self.new_frame, text='First Name', font=('calibri', 16),
                 bg=bg, fg=fg, height=1).grid(row=0, column=1, stick='nw')
        self.fnameEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'))
        self.fnameEntry.grid(row=0, column=1, padx=2, pady=30, stick='sw')
        # middle name
        tk.Label(self.new_frame, text='Middle Name', font=('calibri', 16),
                 bg=bg, fg=fg, height=1).grid(row=0, column=2, stick='nw')
        self.midnameEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'))
        self.midnameEntry.grid(row=0, column=2, padx=2, pady=30, stick='sw')
        # last name
        tk.Label(self.new_frame, text='Last Name', font=('calibri', 16),
                 bg=bg, fg=fg, height=1).grid(row=0, column=3, stick='nw')
        self.lnameEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'))
        self.lnameEntry.grid(row=0, column=3, padx=2, pady=30, stick='sw')

        # customer Gender
        tk.Label(self.new_frame, text='Gender:', font=('calibri', 16),
                 bg=bg, fg=fg, height=1).grid(row=1, column=0, padx=10, stick='nsew')
        gend = tk.StringVar(value='None')
        # gend.set("")
        maleRadio = tk.Radiobutton(self.new_frame, text='Male', val='Male', variable=gend, font=('calibri', 16),
                                   bg='blue', fg='black', command=lambda: self.sel_gender(gend.get()), state='normal')
        maleRadio.grid(row=1, column=1, padx=2, sticky='w')
        femaleRadio = tk.Radiobutton(self.new_frame, text='Female', val='Female', variable=gend, font=('calibri', 16),
                                     bg='blue', fg='black', command=lambda: self.sel_gender(gend.get()), state='normal')
        femaleRadio.grid(row=1, column=2, padx=2, sticky='w')

        # customer date of birth
        tk.Label(self.new_frame, text='Date of Birth:', font=('calibri', 16),
                 bg=bg, fg=fg, height=1).grid(row=2, column=0, padx=10, stick='nsew')
        # day
        tk.Label(self.new_frame, text='Day', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=2, column=1, padx=5, stick='nw')
        self.bdayCbox = ttk.Combobox(self.new_frame, font=('calibri', 16, 'bold'), value=self.day, 
                                     width=10, state='readonly')
        self.bdayCbox.set(str(datetime.date.today().day))
        self.bdayCbox.grid(row=2, column=1, padx=5, pady=30, stick='sw')
        # month
        tk.Label(self.new_frame, text='Month', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=2, column=2, padx=5, stick='nw')
        self.bmonthCbox = ttk.Combobox(self.new_frame, font=('calibri', 16, 'bold'),
                                       value=[v for k, v in self.month.items()], width=10, state='readonly')
        self.bmonthCbox.set(self.month[datetime.date.today().month])
        self.bmonthCbox.grid(row=2, column=2, padx=5, pady=30, stick='sw')
        # year
        tk.Label(self.new_frame, text='Year', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=2, column=3, stick='nw')
        self.byrCbox = ttk.Combobox(self.new_frame, font=('calibri', 16, 'bold'), value=self.year, 
                                     width=10, state='readonly')
        self.byrCbox.set(str(datetime.date.today().year))
        self.byrCbox.grid(row=2, column=3, pady=30, stick='sw')

        # nationality
        tk.Label(self.new_frame, text='Nationality:', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=3, column=0, padx=10, stick='nsew')
        tk.Label(self.new_frame, text='Country of Origin', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=3, column=1, stick='nw')
        self.natEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'), width=15)
        self.natEntry.grid(row=3, column=1, padx=5, pady=30, stick='sw')

        # state of origin
        tk.Label(self.new_frame, text='State of Origin', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=3, column=2, stick='nw')
        self.stateEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'), width=10)
        self.stateEntry.grid(row=3, column=2, padx=5, pady=30, stick='sw')

        # Office address
        tk.Label(self.new_frame, text='Office Address:', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=4, column=0, padx=5, stick='nsew')
        self.off_addrText = tk.Text(self.new_frame, font=('calibri', 16, 'bold'), width=10, height=3)
        self.off_addrText.grid(row=4, column=1, padx=5, pady=30, sticky='ew')

        # date of registration
        tk.Label(self.new_frame, text='As of Date:', font=('calibri', 16),
                 bg=bg, fg=fg, height=1).grid(row=5, column=0, padx=5, sticky='nsew')
        # day
        tk.Label(self.new_frame, text='Day', font=('calibri', 16),
                 bg=bg, fg=fg, height=1).grid(row=5, column=1, sticky='nw')
        self.regdayCbox = ttk.Combobox(self.new_frame, font=('calibri', 16, 'bold'), value=self.day, 
                                     width=10, state='readonly')
        self.regdayCbox.set(str(datetime.date.today().day))
        self.regdayCbox.grid(row=5, column=1, padx=5, pady=30, sticky='sw')
        # month
        tk.Label(self.new_frame, text='Month', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=5, column=2, sticky='nw')
        self.regmonthCbox = ttk.Combobox(self.new_frame, font=('calibri', 16, 'bold'),
                                         value=[v for k, v in self.month.items()], width=10, state='readonly')
        self.regmonthCbox.set(self.month[datetime.date.today().month])
        self.regmonthCbox.grid(row=5, column=2, padx=5, pady=30, sticky='sw')
        # year
        tk.Label(self.new_frame, text='Year', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=5, column=3, sticky='nw')
        self.regyrCbox = ttk.Combobox(self.new_frame, font=('calibri', 16, 'bold'), value=self.year, 
                                     width=10, state='readonly')
        self.regyrCbox.set(str(datetime.date.today().year))
        self.regyrCbox.grid(row=5, column=3, pady=30, sticky='sw')

        submitButton = tk.Button(self.new_frame, text='Submit', font=("Calibri", 14, 'bold'),
                                 fg='white', bg='green', width=10, height=2, command=self.submitcust)
        submitButton.grid(row=7, column=2, padx=10, sticky='se')

        custpageb = tk.Button(self.new_frame, text='Customer Page', font=("Calibri", 14, 'bold'),
                             fg='blue', bg='white', height=2, width=15, command=self.custpage)
        custpageb.grid(row=7, column=0, padx=15, stick='se')

        # display inventory page's frame
        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.sectionFrame is not None:
            self.sectionFrame.grid_forget()
        self.new_frame.grid(row=1, rowspan=8, column=0, columnspan=3, sticky='nsew')

    def sel_gender(self, selected_gender):
        self.cust_obj.gender = selected_gender
        print(self.cust_obj.gender)

    def submitcust(self):
        # frame for submission status
        self.submit_frame = tk.LabelFrame(self.master, text='DO YOU WANT TO SAVE?', fg='white',
                                          font=('arial black', 12), bg='blue')
        self.submit_frame.rowconfigure(list(range(5)), weight=1)
        self.submit_frame.columnconfigure(list(range(4)), weight=1)

        fname, midname, lname = self.fnameEntry.get(), self.midnameEntry.get(), self.lnameEntry.get()
        gender = self.cust_obj.gender
        bday, bmon, byr = self.bdayCbox.get(), self.bmonthCbox.get(), self.byrCbox.get()
        natn, orig_state = self.natEntry.get(), self.stateEntry.get()
        off_addr = self.off_addrText.get(index1='1.0', index2='end')
        regday, regmon, regyr = self.regdayCbox.get(), self.regmonthCbox.get(), self.regyrCbox.get()

        # collection of entry fields
        mandatory_entries = [fname, lname, gender, natn, orig_state, off_addr]
        str_type_entries = [fname, midname, lname, natn, orig_state, off_addr]
        wspace = string.whitespace
        puncs = string.punctuation

        # check for empty field
        if [True for entry in mandatory_entries if (entry is None) or (entry in wspace)]:
            return messagebox.showerror(title='Blank Field', message='BLANK FIELD(S) DETECTED!')
        # check for fields with punctuations
        if [True for entry in mandatory_entries if (entry in puncs)]:
            return messagebox.showerror(title='Punctuation Error', message='FIELD(S) CANNOT CONTAIN PUNCTUATION MARK(S)!')

        # check for fields with invalid data types
        for entry in str_type_entries:
            try:
                float(entry)
                # figures have been entered, if no error was raised
                return messagebox.showerror(title='Invalid Data Type', message=f'Number {entry} is not allowed here!')
            except ValueError as VE:
                continue

        # string constraints
        if [True for entry in [fname, lname, natn, orig_state] if not(entry.isalnum())] or [True for entry in [fname, lname, natn, orig_state] for char in
                                                                        entry if char in string.punctuation]:
            return messagebox.showerror(title='INVALID CHARACTER',
                                        message=f'INVALID CHARACTER HAS BEEN ENTERED!\n\nPlease Check entries:\nFIRST NAME\nLAST NAME\nNATIONALITY')

        self.cust_obj.customer_id = f'{natn[0].upper()}{orig_state[:2]}{self.ID_gen()}'
        self.cust_obj.first_name, self.cust_obj.last_name = fname.capitalize(), lname.capitalize()
        if midname in wspace:
            self.cust_obj.mid_name = None
        else:
            self.cust_obj.mid_name = midname.capitalize()
        self.cust_obj.gender, self.cust_obj.date_of_birth = gender, f"{byr}-{bmon}-{bday}"
        self.cust_obj.country, self.cust_obj.state_of_origin = natn.title(), orig_state.title()
        self.cust_obj.office_addr, self.cust_obj.date_opened = ' '.join(off_addr.title().split()), f"{regyr}-{regmon}-{regday}"

        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='blue', fg='white',
                 text=f"ID:\n{self.cust_obj.customer_id}").grid(row=0, column=0, sticky='ew')
        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='blue', fg='white',
                 text=f"FIRST NAME\n{self.cust_obj.first_name}").grid(row=0, column=1, sticky='ew')
        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='blue', fg='white',
                 text=f"MIDDLE NAME\n{self.cust_obj.mid_name}").grid(row=0, column=2, sticky='ew')
        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='blue', fg='white',
                 text=f"LAST NAME\n{self.cust_obj.last_name}").grid(row=0, column=3, sticky='ew')
        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='blue', fg='white',
                 text=f"GENDER\n{self.cust_obj.gender}").grid(row=1, column=0, sticky='ew')
        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='blue', fg='white',
                 text=f"DATE OF BIRTH\n{self.cust_obj.date_of_birth}").grid(row=1, column=1, sticky='ew')
        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='blue', fg='white',
                 text=f"NATIONALITY\n{self.cust_obj.country}").grid(row=1, column=2, sticky='ew')
        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='blue', fg='white',
                 text=f"STATE OF ORIGIN\n{self.cust_obj.state_of_origin}").grid(row=1, column=3, sticky='ew')
        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='blue', fg='white',
                 text=f"OFFICE ADDRESS\n{self.cust_obj.office_addr}").grid(row=2, column=0, columnspan=2, sticky='ew')
        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='blue', fg='white',
                 text=f"DATE OPENED\n{self.cust_obj.date_opened}").grid(row=2, column=2, sticky='ew')

        # save and cancel buttons
        tk.Button(self.submit_frame, text='Save', font=("Calibri", 14, 'bold'), bg='green', fg='white',
                  height=3, width=10, command=self.savecust).grid(row=4, column=0, padx=5, stick='ew')
        tk.Button(self.submit_frame, text='Cancel', font=("Calibri", 14, 'bold'), bg='red', fg='white',
                  height=3, width=10, command=self.new_cust).grid(row=4, column=3, padx=5, stick='ew')

        if self.display_frame is not None:
            self.display_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        self.submit_frame.grid(row=1, sticky='nsew')

    def savecust(self):

        with open(self.cust_obj.cust_data, 'a',
                  encoding='utf8') as hand:
            hand.writelines(f"{self.cust_obj.__dict__}\n")

        self.submit_frame = self.make_frame(background_color='blue')

        saved = tk.Label(self.submit_frame, text='NEW CUSTOMER HAS BEEN ADDED!', font=("arial", 14, 'bold'),
                         bg='blue', fg='white')
        saved.grid(row=0, column=0, columnspan=4, sticky='nsew')

        addb = tk.Button(self.submit_frame, text='Add Another', font=("Calibri", 14, 'bold'),
                         fg='blue', bg='white', height=5, width=15, command=self.new_cust)
        addb.grid(row=1, column=0, padx=5, stick='ew')

        custpageb = tk.Button(self.submit_frame, text='Customer Page', font=("Calibri", 14, 'bold'),
                             bg='blue', fg='white', height=5, width=15, command=self.custpage)
        custpageb.grid(row=1, column=3, padx=5, stick='ew')

        self.submit_frame.rowconfigure([0, 1], weight=1)
        self.submit_frame.columnconfigure(list(range(4)), weight=1)
        self.submit_frame.grid(row=1, sticky='nsew')
        
    def read_cust(self):
        with open(self.cust_obj.cust_data, 'r', encoding='utf8') as hand:
            # customer attributes is a list of record strings
            cust_attr = hand.readlines()
        return cust_attr
    
    def cust_fields(self):
        '''
        return (customer_ids, fnames, mnames, lnames, genders, dobs, nationalities, states_of_origin, office_addrs, dates_opened)
        :return: tuple of fields
        '''
        with open(self.cust_obj.cust_data, 'r', encoding='utf8') as hand:
            custdata = hand.readlines()
        customer_ids = [v for line in custdata for k, v in eval(line).items() if k == 'customer_id']
        fnames = [v for line in custdata for k, v in eval(line).items() if k == 'first_name']
        mnames = [v for line in custdata for k, v in eval(line).items() if k == 'mid_name']
        lnames = [v for line in custdata for k, v in eval(line).items() if k == 'last_name']
        genders = [v for line in custdata for k, v in eval(line).items() if k == 'gender']
        dobs = [v for line in custdata for k, v in eval(line).items() if k == 'date_of_birth']
        nationalities = [v for line in custdata for k, v in eval(line).items() if k == 'country']
        states_of_origin = [v for line in custdata for k, v in eval(line).items() if k == 'state_of_origin']
        office_addrs = [v for line in custdata for k, v in eval(line).items() if k == 'office_addr']
        dates_opened = [v for line in custdata for k, v in eval(line).items() if k == 'date_opened']
        
        return customer_ids, fnames, mnames, lnames, genders, dobs, nationalities, states_of_origin, office_addrs, dates_opened

    def fetch_cust(self, selected_custid):
        '''
        fetches the selected customer's details
        :param selected_custid:
        :return: (custid, f_name, m_name, l_name, sex, dbirth, country, state, office, dopened)
        '''
        customer_ids, fnames, mnames, lnames, genders, dobs, nationalities, states_of_origin, office_addrs, dates_opened = self.cust_fields()

        for cid, f, m, l, g, db, n, s, o, do in zip(customer_ids, fnames, mnames, lnames, genders, dobs, nationalities, states_of_origin, office_addrs, dates_opened):
            if cid == selected_custid:
                return cid, f, m, l, g, db, n, s, o, do

    def display_cust(self):
        global edit_custid_entry, cust, lines
        cust = []
        lines = {}

        # setup display frame
        self.display_frame = self.make_frame(page_title='CUSTOMER RECORDS VIEW', background_color='blue')

        # retrieve customer data from file
        # cust is a list of strings containing customer records
        cust_rec = self.read_cust()

        for ind in range(len(cust_rec)):
            # labelled format of saved customer record
            lines['Row_' + str(ind)] = eval(cust_rec[ind])
            # cust is a list of saved customer instances
            cust.append(eval(cust_rec[ind]))

        # display headings for customer records
        # create scrolled text field to display customer records
        st = scrolledtext.ScrolledText(self.display_frame, bg='blue', fg='white', wrap='word',
                                       font=("Calibri", 14, 'bold'), relief='flat')
        st.grid(row=0, column=0, columnspan=8, sticky='nsew')
        # display headings for customer records
        st.insert(index='end',
                  chars='CUSTOMER ID, FIRST NAME, MIDDLE NAME, LAST NAME, GENDER, DATE OF BIRTH, NATIONALITY, STATE OF ORIGIN, OFFICE ADDRESS, DATE OPENED\n\n')

        for ind in range(len(cust)):
            # assign user input from stored customer records to each customer class attribute
            self.cust_obj.__dict__ = cust[ind]

            st.insert(index='end',
                      chars=f"{self.cust_obj.customer_id}, {self.cust_obj.first_name}, {self.cust_obj.mid_name}, {self.cust_obj.last_name}, {self.cust_obj.gender}, {self.cust_obj.date_of_birth}, {self.cust_obj.country}, {self.cust_obj.state_of_origin}, {' '.join(self.cust_obj.office_addr.split())}, {self.cust_obj.date_opened}\n\n")
        # make text field read-only
        st.config(state='disabled')
        # ensure that text can be copied to clipboard
        st.bind('<1>', lambda event: st.focus_set())

        custpageb = tk.Button(self.display_frame, text='Customer Page', font=("Calibri", 12, 'bold'),
                             fg='blue', bg='white', height=1, width=15, command=self.custpage)
        custpageb.grid(row=2, column=3, padx=5, pady=5, stick='se')

        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_frame is not None:
            self.edit_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        self.display_frame.rowconfigure(list(range(3)), weight=1)
        self.display_frame.columnconfigure(list(range(9)), weight=1)
        self.display_frame.grid(row=1, rowspan=2, column=0, columnspan=4, sticky='nsew')

    def edit_cust(self):
        global edit_custid_entry, cust, lines
        cust = []
        lines = {}

        # setup display frame
        self.display_frame = self.make_frame(page_title='UPDATE CUSTOMER RECORDS', background_color='blue')

        # retrieve customer data from file
        # cust is a list of strings containing customer records
        cust_rec = self.read_cust()

        for ind in range(len(cust_rec)):
            # labelled format of saved customer record
            lines['Row_' + str(ind)] = eval(cust_rec[ind])
            # cust is a list of saved customer instances
            cust.append(eval(cust_rec[ind]))

        # display headings for customer records
        # create scrolled text field to display customer records
        st = scrolledtext.ScrolledText(self.display_frame, bg='blue', fg='white', wrap='word', font=("Calibri", 14, 'bold'))
        st.grid(row=0, column=0, columnspan=8, sticky='nsew')
        # display headings for customer records
        st.insert(index='end',
                  chars='CUSTOMER ID, FIRST NAME, MIDDLE NAME, LAST NAME, GENDER, DATE OF BIRTH, NATIONALITY, STATE OF ORIGIN, OFFICE ADDRESS, DATE OPENED\n\n')


        for ind in range(len(cust)):
            # assign user input from stored customer records to each customer class attribute
            self.cust_obj.__dict__ = cust[ind]

            st.insert(index='end', chars=f"{self.cust_obj.customer_id}, {self.cust_obj.first_name}, {self.cust_obj.mid_name}, {self.cust_obj.last_name}, {self.cust_obj.gender}, {self.cust_obj.date_of_birth}, {self.cust_obj.country}, {self.cust_obj.state_of_origin}, {' '.join(self.cust_obj.office_addr.split())}, {self.cust_obj.date_opened}\n\n")
        # make text field read-only
        st.config(state='disabled')
        # ensure that text can be copied to clipboard
        st.bind('<1>', lambda event: st.focus_set())

        # to edit the given row number (at row entry - 1)
        tk.Label(self.display_frame, text='ENTER CUSTOMER ID:', font=("Calibri", 12, 'bold'), bg='blue',
                 fg='white').grid(row=2, column=0, padx=2, sticky='e')
        # custid entry
        edit_custid_entry = tk.Entry(self.display_frame, font=("Calibri", 12, 'bold'), relief='sunken')
        edit_custid_entry.grid(row=2, column=1, padx=2, sticky='ew')
        # edit button
        tk.Button(self.display_frame, text='Edit', font=("Calibri", 12, 'bold'),
                  bg='orange', fg='white', height=1, width=10, command=self.editing_cust).grid(row=2,
                                                                                               padx=5, column=2, sticky='w')

        tk.Button(self.display_frame, text='Customer Page', font=("Calibri", 12, 'bold'), fg='blue', bg='white', 
                  height=1, width=15, command=self.custpage).grid(row=2, column=6, padx=5, pady=5, stick='se')

        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_frame is not None:
            self.edit_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        self.display_frame.rowconfigure(list(range(3)), weight=1)
        self.display_frame.columnconfigure(list(range(9)), weight=1)
        self.display_frame.grid(row=1, rowspan=2, column=0, columnspan=4, sticky='nsew')

    def editing_cust(self):
        global edit_custid_entry, cust, lines, edit_row

        self.display_frame = self.make_frame(page_title='UPDATING CUSTOMER RECORD', background_color='blue')

        customer_ids = []

        for rec in cust:
            # list of all existing customer ids (converted to lower case)
            customer_ids.extend([v.lower() for k, v in rec.items() if k.lower() == 'customer_id'])
        print(customer_ids)

        inp = edit_custid_entry.get()

        if inp.lower() not in customer_ids:
            return messagebox.showerror(title='INVALID ENTRY', message=f'{inp} IS NOT VALID')

        # get the row index of the selected customer id
        for row, rec in lines.items():
            for k, v in rec.items():
                # if valid ID is entered
                if k.lower() == 'customer_id' and v.lower() == inp.lower():
                    edit_row = row
                    # print(f"Found at {edit_row}")

        # assign the selected record to the customer object
        for row, rec in lines.items():
            if row == edit_row:
                self.cust_obj.__dict__ = rec
        print(self.cust_obj.__dict__)

        # entry fields for new data
        tk.Label(self.display_frame, text=f"ENTER NEW DATA BELOW", font=("Calibri", 14, 'bold'),
                 bg='blue', fg='white').grid(row=0, columnspan=3, sticky='ew', padx=50)

        # customer labels and entries
        # customer name labels and entries
        tk.Label(self.display_frame, text="FIRST NAME", font=("Calibri", 10, 'bold'),
                 bg='blue', fg='white').grid(row=1, column=0, sticky='sw', padx=25, pady=15)
        self.fname_entry = tk.Entry(self.display_frame)
        self.fname_entry.insert(0, string=f'{self.cust_obj.first_name}')
        self.fname_entry.grid(row=2, column=0, sticky='w', padx=25, pady=5)

        tk.Label(self.display_frame, text="MIDDLE NAME", font=("Calibri", 10, 'bold'),
                 bg='blue', fg='white').grid(row=1, column=1, sticky='sw', padx=25, pady=15)
        self.mname_entry = tk.Entry(self.display_frame)
        self.mname_entry.insert(0, f'{self.cust_obj.mid_name}')
        self.mname_entry.grid(row=2, column=1, sticky='w', padx=25, pady=5)

        tk.Label(self.display_frame, text="LAST NAME", font=("Calibri", 10, 'bold'),
                 bg='blue', fg='white').grid(row=1, column=2, sticky='sw', padx=25, pady=15)
        self.lname_entry = tk.Entry(self.display_frame)
        self.lname_entry.insert(0, f'{self.cust_obj.last_name}')
        self.lname_entry.grid(row=2, column=2, sticky='w', padx=25, pady=5)
        # gender
        gends = ['Male', 'Female']
        
        tk.Label(self.display_frame, text="GENDER", font=("Calibri", 10, 'bold'),
                 bg='blue', fg='white').grid(row=1, column=3, sticky='sw', padx=25, pady=15)
        self.genderCbox = ttk.Combobox(self.display_frame, font=('calibri', 16, 'bold'), value=gends, 
                                     width=8, state='readonly')
        self.genderCbox.set(f'{self.cust_obj.gender}')
        self.genderCbox.grid(row=2, column=3, sticky='w', padx=25, pady=5)

        # date of birth labels and entries
        tk.Label(self.display_frame, text="DATE OF BIRTH", font=("Calibri", 10, 'bold'),
                 bg='blue', fg='white').grid(row=3, column=0, sticky='sw', padx=25, pady=15)

        tk.Label(self.display_frame, text="BIRTH YEAR", font=("Calibri", 10, 'bold'),
                 bg='blue', fg='white').grid(row=3, column=1, sticky='sw', padx=25, pady=15)
        year = re.findall(r'(\d{2,4})-(\w{3})-(\d{1,2})', self.cust_obj.date_of_birth)[0][0]
        self.byearCbox = ttk.Combobox(self.display_frame, font=('calibri', 16, 'bold'), value=self.year, 
                                     width=10, state='readonly')
        self.byearCbox.set(f'{year}')
        self.byearCbox.grid(row=4, column=1, sticky='w', padx=25, pady=5)

        tk.Label(self.display_frame, text="BIRTH MONTH", font=("Calibri", 10, 'bold'),
                 bg='blue', fg='white').grid(row=3, column=2, sticky='sw', padx=25, pady=15)
        month = re.findall(r'(\d{2,4})-(\w{3})-(\d{1,2})', self.cust_obj.date_of_birth)[0][1]
        self.bmonCbox = ttk.Combobox(self.display_frame, font=('calibri', 16, 'bold'),
                                     value=[v for k, v in self.month.items()], width=10, state='readonly')
        self.bmonCbox.set(f'{month}')
        self.bmonCbox.grid(row=4, column=2, sticky='w', padx=25, pady=5)

        tk.Label(self.display_frame, text="BIRTH DAY", font=("Calibri", 10, 'bold'),
                 bg='blue', fg='white').grid(row=3, column=3, sticky='sw', padx=25, pady=15)
        day = re.findall(r'(\d{2,4})-(\w{3})-(\d{1,2})', self.cust_obj.date_of_birth)[0][2]
        self.bdCbox = ttk.Combobox(self.display_frame, font=('calibri', 16, 'bold'), value=self.day, 
                                     width=10, state='readonly')
        self.bdCbox.set(f'{day}')
        self.bdCbox.grid(row=4, column=3, sticky='w', padx=25, pady=5)

        # nationality
        tk.Label(self.display_frame, text="NATIONALITY", font=("Calibri", 10, 'bold'),
                 bg='blue', fg='white').grid(row=5, column=0, sticky='sw', padx=25, pady=15)
        self.natn_entry = tk.Entry(self.display_frame)
        self.natn_entry.insert(0, f'{self.cust_obj.country}')
        self.natn_entry.grid(row=6, column=0, sticky='w', padx=25, pady=5)

        # state of origin
        tk.Label(self.display_frame, text="STATE OF ORIGIN", font=("Calibri", 10, 'bold'),
                 bg='blue', fg='white').grid(row=5, column=1, sticky='sw', padx=25, pady=15)
        self.ori_state_entry = tk.Entry(self.display_frame)
        self.ori_state_entry.insert(0, f'{self.cust_obj.state_of_origin}')
        self.ori_state_entry.grid(row=6, column=1, sticky='w', padx=25, pady=5)

        # office address
        tk.Label(self.display_frame, text="OFFICE ADDRESS", font=("Calibri", 10),
                 bg='blue', fg='white').grid(row=5, column=2, sticky='sw', padx=25, pady=15)
        self.off_entry = tk.Text(self.display_frame, font=('calibri', 16, 'bold'), width=30, height=3)
        self.off_entry.insert('1.0', f'{self.cust_obj.office_addr}')
        self.off_entry.grid(row=6, column=2, sticky='w', padx=25, pady=5)

        # update and customer page buttons
        tk.Button(self.display_frame, text='Update', font=("Calibri", 12, 'bold'),
                            bg='orange', fg='white', height=1, width=15, command=self.update_cust).grid(row=8, column=1, padx=5, pady=5, stick='sw')

        tk.Button(self.display_frame, text='Customer Page', font=("Calibri", 12, 'bold'),
                             bg='blue', fg='white', height=1, width=15, command=self.custpage).grid(row=8, column=3, padx=5, pady=5, stick='sw')

        # clear the frames before and after this page
        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_frame is not None:
            self.edit_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        # display an adjustible frame containing the selected info
        self.display_frame.rowconfigure(list(range(12)), weight=1)
        self.display_frame.columnconfigure(list(range(12)), weight=1)
        self.display_frame.grid(row=1, rowspan=2, column=0, columnspan=4, sticky='nsew')

    def update_cust(self):
        global lines, edit_row
        # raise error alarm if any of the field is blank
        fname, mname, lname, gender = self.fname_entry.get(), self.mname_entry.get(), self.lname_entry.get(), self.genderCbox.get()
        natn, orig_state, off_addr = self.natn_entry.get(), self.ori_state_entry.get(), self.off_entry.get(index1='1.0', index2='end')
        byr, bmon, bday = self.byearCbox.get(), self.bmonCbox.get(),self.bdCbox.get()

        wspace = string.whitespace
        puncs = string.punctuation

        # collection of entry fields
        mandatory_entries = [fname, lname, gender, natn, orig_state, off_addr]
        punc_entries = [fname, lname, natn, orig_state]
        str_type_entries = [fname, mname, lname, natn, orig_state]


        # check for empty field
        if [True for entry in mandatory_entries if (entry in wspace)]:
            return messagebox.showerror(title='Blank Field', message='BLANK FIELD(S) DETECTED!')

        # check for fields with punctuations (excluding date field)
        if [True for entry in punc_entries if entry in puncs]:
            return messagebox.showerror(title='Punctuation Error',
                                        message='FIELD(S) CANNOT CONTAIN PUNCTUATION MARK(S)!')

        # check for fields with invalid data types
        for entry in str_type_entries:
            try:
                float(entry)
                # figures have been entered, if no error was raised
                return messagebox.showerror(title='Invalid Data Type', message=f'Number {entry} is not allowed here!')
            except ValueError as VE:
                continue

        # string constraints
        if [True for entry in str_type_entries if not (entry.isalnum)] or [True for entry in
                                                                                             str_type_entries for char in
                                                                                             entry if
                                                                                             char in string.punctuation]:
            return messagebox.showerror(title='INVALID CHARACTER',
                                        message=f'INVALID CHARACTER HAS BEEN ENTERED!\n\nPlease Check entries:\nFIRST NAME\nLAST NAME\nNATIONALITY')

        # when confirmation is given by user
        self.display_frame = self.make_frame(background_color='blue')

        # reassign the newly entered values to the inventory object's name, qty, unit and date
        self.cust_obj.first_name, self.cust_obj.last_name, self.cust_obj.gender = fname.capitalize(), lname.capitalize(), gender.capitalize()
        self.cust_obj.date_of_birth, self.cust_obj.country, self.cust_obj.state_of_origin = f'{byr}-{bmon}-{bday}', natn.title(), orig_state.title()
        self.cust_obj.office_addr = ' '.join(off_addr.title().split())
        if mname in wspace:
            self.cust_obj.mid_name = None
        else:
            self.cust_obj.mid_name = mname.capitalize()
        

        # update the retrieved data from file with the changes made
        lines[edit_row] = self.cust_obj.__dict__


        tk.Label(self.display_frame, text=f"ID\n{self.cust_obj.customer_id}", font=("Calibri", 10, 'bold'),
                 bg='blue', fg='white').grid(row=0, column=0, sticky='nsew', padx=25)

        tk.Label(self.display_frame, text=f"CUSTOMER NAME\n{self.cust_obj.first_name} {self.cust_obj.mid_name} {self.cust_obj.last_name}", font=("Calibri", 10, 'bold'),
                 bg='blue', fg='white').grid(row=0, column=1, sticky='nsew', padx=25, pady=15)

        tk.Label(self.display_frame, text=f"GENDER\n{self.cust_obj.gender}",
                 font=("Calibri", 10, 'bold'), bg='blue', fg='white').grid(row=0, column=2, sticky='nsew', padx=25)

        tk.Label(self.display_frame, text=f"DATE OF BIRTH\n{self.cust_obj.date_of_birth}", font=("Calibri", 10, 'bold'),
                 bg='blue', fg='white').grid(row=0, column=3, sticky='nsew', padx=25)

        tk.Label(self.display_frame, text=f"NATIONALITY\n{self.cust_obj.country} ", font=("Calibri", 10, 'bold'),
                 bg='blue', fg='white').grid(row=1, column=0, sticky='nsew', padx=25)

        tk.Label(self.display_frame, text=f"STATE OF ORIGIN\n{self.cust_obj.state_of_origin} ", font=("Calibri", 10, 'bold'),
                 bg='blue', fg='white').grid(row=1, column=1, sticky='nsew', padx=25)

        tk.Label(self.display_frame, text=f"OFFICE ADDRESS\n{self.cust_obj.office_addr}", font=("Calibri", 10, 'bold'),
                 bg='blue', fg='white').grid(row=1, column=2, sticky='nsew', padx=25)

        tk.Label(self.display_frame, text=f"DATE OPENED\n{self.cust_obj.date_opened}", font=("Calibri", 10, 'bold'),
                 bg='blue', fg='white').grid(row=1, column=3, sticky='nsew', padx=25)

        tk.Label(self.display_frame, text="HAS BEEN UPDATED!!", font=("Calibri", 10, 'bold'),
                 bg='blue', fg='white').grid(row=2, column=1, columnspan=2, sticky='NSEW', padx=25)

        tk.Button(self.display_frame, text='Customer Page', font=("Calibri", 12, 'bold'),
                             fg='blue', bg='white', height=1, width=15, command=self.custpage).grid(row=2, column=3, padx=5, pady=5, stick='se')

        if not(messagebox.askyesno(message='Do You Want To Save Changes Made?')):
            messagebox.showinfo(message='No Changes Made')
            return self.edit_cust()

        # save updated version to file
        # print([rec for row, rec in lines.items()])
        with open(self.cust_obj.cust_data, 'w', encoding='utf8') as hand:
            for row, rec in lines.items():
                hand.writelines(f"{rec}\n")

        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_frame is not None:
            self.edit_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        self.display_frame.rowconfigure([0, 1, 2, 3], weight=1)
        self.display_frame.columnconfigure(list(range(4)), weight=1)
        self.display_frame.grid(row=1, rowspan=4, column=0, columnspan=4, sticky='nsew')

    def delete_cust(self):
        global del_custid_entry, cust, lines
        cust = []
        lines = {}

        # setup display frame
        self.display_frame = self.make_frame(page_title='SELECT RECORD TO DELETE', background_color='blue')

        # retrieve customer data from file
        # cust is a list of strings containing customer records
        cust_rec = self.read_cust()

        for ind in range(len(cust_rec)):
            # labelled format of saved customer record
            lines['Row_' + str(ind)] = eval(cust_rec[ind])
            # cust is a list of saved customer instances
            cust.append(eval(cust_rec[ind]))

        # display headings for customer records
        # create scrolled text field to display customer records
        st = scrolledtext.ScrolledText(self.display_frame, bg='blue', fg='white', wrap='word',
                                       font=("Calibri", 14, 'bold'))
        st.grid(row=0, column=0, columnspan=8, sticky='nsew')
        # display headings for customer records
        st.insert(index='end',
                  chars='CUSTOMER ID, FIRST NAME, MIDDLE NAME, LAST NAME, GENDER, DATE OF BIRTH, NATIONALITY, STATE OF ORIGIN, OFFICE ADDRESS, DATE OPENED\n\n')

        for ind in range(len(cust)):
            # assign user input from stored customer records to each customer class attribute
            self.cust_obj.__dict__ = cust[ind]

            st.insert(index='end',
                      chars=f"{self.cust_obj.customer_id}, {self.cust_obj.first_name}, {self.cust_obj.mid_name}, {self.cust_obj.last_name}, {self.cust_obj.gender}, {self.cust_obj.date_of_birth}, {self.cust_obj.country}, {self.cust_obj.state_of_origin}, {str(' '.join(self.cust_obj.office_addr.split()))}, {self.cust_obj.date_opened}\n\n")
        # make text field read-only
        st.config(state='disabled')
        # ensure that text can be copied to clipboard
        st.bind('<1>', lambda event: st.focus_set())

        # to edit the given row number (at row entry - 1)
        tk.Label(self.display_frame, text='ENTER CUSTOMER ID:', font=("Calibri", 12, 'bold'), bg='blue',
                 fg='white').grid(row=2, column=0, padx=2, sticky='e')
        # custid entry
        del_custid_entry = tk.Entry(self.display_frame, font=("Calibri", 12, 'bold'), relief='sunken')
        del_custid_entry.grid(row=2, column=1, padx=2, sticky='ew')

        # delete button
        tk.Button(self.display_frame, text='Delete', font=("Calibri", 12, 'bold'), bg='red', fg='white',
                  height=1, width=10, command=self.erase_cust).grid(row=2, column=2, padx=5, sticky='w')

        tk.Button(self.display_frame, text='Customer Page', font=("Calibri", 12, 'bold'), fg='blue', bg='white',
                  height=1, width=15, command=self.custpage).grid(row=2, column=6, padx=5, pady=5, stick='se')

        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_frame is not None:
            self.edit_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        self.display_frame.rowconfigure(list(range(3)), weight=1)
        self.display_frame.columnconfigure(list(range(9)), weight=1)
        self.display_frame.grid(row=1, rowspan=2, column=0, columnspan=4, sticky='nsew')

    def erase_cust(self):
        global lines, cust_ids, del_row, del_custid_entry
        bg, fg = 'red', 'white'
        # raise error alarm if any of the field is blank

        self.display_frame = self.make_frame(page_title='RECORD DELETED', background_color=bg)

        cust_ids = []

        for row, rec in lines.items():
            cust_ids.extend([v.lower() for k, v in rec.items() if k.lower() == 'customer_id'])

        inp = del_custid_entry.get()

        if inp.lower() not in cust_ids:
            return messagebox.showerror(title='INVALID ENTRY', message=f'{inp} IS NOT VALID')

        if not (messagebox.askyesno(title='CONFIRM DELETE', message='Do You Want To Delete?')):
            return messagebox.showinfo(message='RECORD NOT DELETED')

        for row, rec in lines.items():
            for k, v in rec.items():
                # if valid ID is entered
                if k.lower() == 'customer_id' and v.lower() == inp.lower():
                    del_row = row
                    # print(f"Found at {del_row}")

        with open(self.cust_obj.cust_data, 'w', encoding='utf8') as hand:
            for row, rec in lines.items():
                if row == del_row:
                    # assign the selected row
                    self.cust_obj.__dict__ = rec
                    continue
                hand.writelines(f"{rec}\n")
        
        self.save_del_cust()
        
        st = scrolledtext.ScrolledText(self.display_frame, bg=bg, fg=fg, font=("Calibri", 14, 'bold'), relief='flat')
        st.insert(index='1.0', chars='ID, FIRST NAME, MIDDLE NAME, LAST NAME, GENDER, DATE OF BIRTH, NATIONALITY, STATE OF ORIGIN, OFFICE ADDRESS, DATE OPENED\n\n'
                                     f'{self.cust_obj.customer_id}, {self.cust_obj.first_name}, {self.cust_obj.mid_name}, {self.cust_obj.last_name}, '
                                     f'{self.cust_obj.gender}, {self.cust_obj.date_of_birth}, {self.cust_obj.country}, {self.cust_obj.state_of_origin}'
                                     f'{" ".join(self.cust_obj.office_addr.split())}, {self.cust_obj.date_opened}\n\n'
                                     'HAS BEEN DELETED!!')

        st.grid(row=0, column=0, columnspan=10, sticky='ew')

        tk.Button(self.display_frame, text='Customer Page', font=("Calibri", 12, 'bold'),
                             fg=bg, bg=fg, height=1, width=15, command=self.custpage).grid(row=3, column=3, padx=5, pady=5, stick='se')

        self.display_frame.rowconfigure(list(range(4)), weight=1)
        self.display_frame.columnconfigure(list(range(4)), weight=1)
        self.display_frame.grid(row=1, rowspan=3, column=0, columnspan=4, sticky='nsew')
        
    def save_del_cust(self):
        with open(self.cust_obj.cust_dels, 'a', encoding='utf8') as hand:
            hand.writelines(f'{self.cust_obj.__dict__}\n')
    
    def invenpage(self):
        # frame for inventory page containing three rows and one column
        self.sectionFrame = tk.LabelFrame(master=self.master, text='INVENTORY', font=('arial black', 12), bg='purple',
                                      fg='white')
        self.sectionFrame.rowconfigure([0, 1, 2, 3], weight=1)
        self.sectionFrame.columnconfigure(0, weight=1)

        # display inventory options
        tk.Button(self.sectionFrame, text='ADD NEW PRODUCT TO INVENTORY', bg='white', fg='blue',
                                font=('arial black', 14), command=self.new_inv).grid(row=1, padx=60, pady=10, sticky='nsew')
        tk.Button(self.sectionFrame, text='UPDATE INVENTORY', bg='white', fg='orange',
                              font=('arial black', 14), command=self.edit_inv).grid(row=2, padx=80, pady=10, sticky='nsew')
        tk.Button(self.sectionFrame, text='DELETE RECORD FROM INVENTORY', bg='white', fg='red',
                              font=('arial black', 14), command=self.delete_inv).grid(row=3, padx=100, pady=10, sticky='nsew')
        tk.Button(self.sectionFrame, text='VIEW INVENTORY RECORDS', bg='white', fg='green',
                              font=('arial black', 14), command=lambda: self.display_inv()).grid(row=0, padx=40, pady=10, sticky='nsew')

        # display inventory page's frame
        if self.display_frame is not None:
            self.display_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()
        if self.homeFrame is not None:
            self.homeFrame.grid_forget()

        self.sectionFrame.grid(row=1, rowspan=4, column=0, columnspan=5, sticky='nsew')

    def new_inv(self):
        # frame for input of new inventory
        self.new_frame = tk.LabelFrame(self.master, text='NEW PRODUCT', fg='white', font=('arial black', 12),
                                            bg='purple')
        self.new_frame.rowconfigure(list(range(4)), weight=1)
        self.new_frame.columnconfigure(list(range(3)), weight=1)

        # place new inventory form
        tk.Label(self.new_frame, text='Product Name:', font=('calibri', 16),
                 bg='purple', fg='white', height=1).grid(row=0, column=0, padx=5, pady=50, sticky='ew')
        self.pnameEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'))
        self.pnameEntry.grid(row=0, column=1, padx=5, pady=50, sticky='ew')

        # stock entries
        tk.Label(self.new_frame, text='New Stock:', font=('calibri', 16),
                 bg='purple', fg='white', height=1).grid(row=1, column=0, padx=5, pady=50, sticky='sew')
        tk.Label(self.new_frame, text='Quantity (in figures)', font=('calibri', 16),
                 bg='purple', fg='white', height=1).grid(row=1, column=1, padx=5, sticky='nw')
        self.qtyEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'), width=10)
        self.qtyEntry.grid(row=1, column=1, padx=5, pady=50, sticky='sw')

        tk.Label(self.new_frame, text='Unit of Measurement', font=('calibri', 16),
                 bg='purple', fg='white', height=1).grid(row=1, column=2, padx=0, sticky='nw')
        self.unitEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'), width=10)
        self.unitEntry.grid(row=1, column=2, padx=5, pady=50, sticky='sw')

        # date entries
        tk.Label(self.new_frame, text='As of Date:', font=('calibri', 16),
                 bg='purple', fg='white', height=1).grid(row=2, column=0, padx=5, pady=50, sticky='sew')
        # day
        tk.Label(self.new_frame, text='Day', font=('calibri', 16),
                 bg='purple', fg='white', height=1).grid(row=2, column=1, padx=5, sticky='nw')
        self.dayCbox = ttk.Combobox(self.new_frame, font=('calibri', 16, 'bold'), width=10, value=self.day, state='readonly')
        self.dayCbox.set(str(datetime.date.today().day))
        self.dayCbox.grid(row=2, column=1, padx=5, pady=50, sticky='sw')
        # month
        tk.Label(self.new_frame, text='Month', font=('calibri', 16),
                 bg='purple', fg='white', height=1).grid(row=2, column=2, padx=5, sticky='nw')
        self.monthCbox = ttk.Combobox(self.new_frame, font=('calibri', 16, 'bold'), width=10,
                                      value=[v for k, v in self.month.items()], state='readonly')
        self.monthCbox.set(self.month[datetime.date.today().month])
        self.monthCbox.grid(row=2, column=2, padx=5, pady=50, sticky='sw')
        # year
        tk.Label(self.new_frame, text='Year', font=('calibri', 16),
                 bg='purple', fg='white', height=1).grid(row=2, column=2, sticky='n')
        self.yrCbox = ttk.Combobox(self.new_frame, font=('calibri', 16, 'bold'), width=10, value=self.year, state='readonly')
        self.yrCbox.set(str(datetime.date.today().year))
        self.yrCbox.grid(row=2, column=2, pady=50, sticky='s')

        # submit and inventory page buttons
        tk.Button(self.new_frame, text='Submit', font=("Calibri", 14, 'bold'), fg='white', bg='green', width=3,
                  height=2, command=self.submitinv).grid(row=3, column=2, padx=350, sticky='ew')
        tk.Button(self.new_frame, text='Inventory Page', font=("Calibri", 14, 'bold'), fg='purple', bg='white',
                  height=2, width=15, command=self.invenpage).grid(row=3, column=1, padx=5, stick='w')

        # display inventory page's frame
        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.sectionFrame is not None:
            self.sectionFrame.grid_forget()

        self.new_frame.grid(row=1, rowspan=4, column=0, columnspan=5, sticky='nsew')

    def ID_gen(self):
        # randomly generates a five-character output
        num = random.randint(100, 999)
        al1 = random.choice('ABCDFJKLMNQWERTPOIUY')
        al2 = random.choice('abcdfjklmnqwertpoiuy')
        return f"{num}{al1}{al2}"

    def submitinv(self):
        # frame for submission status
        self.submit_frame = tk.LabelFrame(self.master, text='DO YOU WANT TO SAVE?', fg='white',
                                          font=('arial black', 12), bg='purple')
        self.submit_frame.rowconfigure([0, 1], weight=1)
        self.submit_frame.columnconfigure(list(range(4)), weight=1)

        pname, qty, unit = self.pnameEntry.get(), self.qtyEntry.get(), self.unitEntry.get()
        eyr, emon, eday = self.yrCbox.get(), self.monthCbox.get(), self.dayCbox.get()

        # collection of entry fields
        mandatory_entries = [pname, qty, unit]
        str_type_entries = [pname, unit]
        num_type_entries = [qty]

        # conditionals
        wspace = string.whitespace
        puncs = string.punctuation

        # check for empty field
        if [True for entry in mandatory_entries if (entry in wspace)]:
            return messagebox.showerror(title='Blank Field', message='BLANK FIELD(S) DETECTED!')
        # check for fields with punctuations
        if [True for entry in mandatory_entries if (entry in puncs)]:
            return messagebox.showerror(title='Punctuation Error',
                                        message='FIELD(S) CANNOT CONTAIN PUNCTUATION MARK(S)!')

        # check for fields with invalid data types
        for entry in str_type_entries:
            try:
                float(entry)
                # figures have been entered, if no error was raised
                return messagebox.showerror(title='Invalid Data Type', message=f'Number {entry} is not allowed here!')
            except ValueError as VE:
                continue

        for entry in num_type_entries:
            try:
                float(entry)
            except ValueError as VE:
                # figures have not been entered, if error was raised
                return messagebox.showerror(title='Invalid Data Type',
                                            message=f'{entry} is not a number\n\nPlease Enter a Number')

        # string constraints
        if [True for entry in [pname, unit] if not(entry.isalnum)] or [True for entry in [pname, unit] for char in entry if char in string.punctuation]:
            return messagebox.showerror(title='OUT OF RANGE ENTRY',
                                        message=f'OUT OF RANGE ENTRY(S) DETECTED!\n\nPlease Check entries:\nPRODUCT NAME\nand\or\nUNIT OF MEASUREMENT')

        # assign user input from entry to each inventory class attribute
        self.inv_obj.prod_id = f"{''.join([word[0] for word in pname.title().split()])}{self.ID_gen()}"
        self.inv_obj.prod_name = pname.title()
        self.inv_obj.qty = qty
        self.inv_obj.unit = unit.title()
        self.inv_obj.entry_date = f"{eyr}-{emon}-{eday}"

        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='purple', fg='white',
                                       text=f"ID:\n{self.inv_obj.prod_id}").grid(row=0, column=0, sticky='ew')
        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='purple', fg='white',
                 text=f"PRODUCT:\n{self.inv_obj.prod_name}").grid(row=0, column=1, sticky='ew')
        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='purple', fg='white',
                 text=f"QTY:\n{self.inv_obj.qty} {self.inv_obj.unit}").grid(row=0, column=2, sticky='ew')
        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='purple', fg='white',
                 text=f"DATE:\n{self.inv_obj.entry_date}").grid(row=0, column=3, sticky='ew')

        saveb = tk.Button(self.submit_frame, text='Save', font=("Calibri", 14, 'bold'),
                          bg='green', fg='white', height=5, width=15, command=self.saveinv)
        saveb.grid(row=1, column=0, padx=5, stick='ew')
        cancelb = tk.Button(self.submit_frame, text='Cancel', font=("Calibri", 14, 'bold'),
                            bg='red', fg='white', height=5, width=15, command=self.new_inv)
        cancelb.grid(row=1, column=3, padx=5, stick='ew')

        if self.display_frame is not None:
            self.display_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        self.submit_frame.grid(row=1, sticky='nsew')

    def saveinv(self):
        # return print(self.inv_obj.inv_data)

        with open(self.inv_obj.inv_data, 'a', encoding='utf8') as hand:
            hand.writelines(f"{self.inv_obj.__dict__}\n")

        self.submit_frame = self.make_frame()

        tk.Label(self.submit_frame, text='NEW INVENTORY HAS BEEN ADDED!', font=("arial", 14, 'bold'),
                         bg='purple', fg='white').grid(row=0, column=0, columnspan=4, sticky='nsew')

        tk.Button(self.submit_frame, text='Add Another', font=("Calibri", 14, 'bold'), bg='blue', fg='white',
                  height=5, width=15, command=self.new_inv).grid(row=1, column=0, padx=5, stick='ew')

        tk.Button(self.submit_frame, text='Inventory Page', font=("Calibri", 14, 'bold'), fg='purple',
                  bg='white', height=5, width=15, command=self.invenpage).grid(row=1, column=3, padx=5, stick='ew')

        self.submit_frame.rowconfigure([0, 1], weight=1)
        self.submit_frame.columnconfigure(list(range(4)), weight=1)
        self.submit_frame.grid(row=1, sticky='nsew')

    def read_inv(self):
        with open(self.inv_obj.inv_data, 'r', encoding='utf8') as hand:
            # inventory attributes is a list of record strings
            inv_attr = hand.readlines()
        return inv_attr

    def display_inv(self):
        global inven, lines

        inven = []
        lines = {}

        # setup display frame
        self.display_frame = self.make_frame(page_title='INVENTORY RECORDS VIEW')

        # retrieve inventory data from file
        # inven is a list of strings containing inventory records
        inven_rec = self.read_inv()

        for ind in range(len(inven_rec)):
            # labelled format of saved inventory record
            lines['Row_'+str(ind)] = eval(inven_rec[ind])
            # inven is a list of saved inventory instances
            inven.append(eval(inven_rec[ind]))

        st = scrolledtext.ScrolledText(self.display_frame, bg='purple', fg='white', wrap='word',
                                       font=("Calibri", 14, 'bold'), relief='flat')
        st.grid(row=0, column=1, columnspan=2, sticky='nsew')

        # display headings for customer records
        st.insert(index='end',
                  chars='PRODUCT ID, PRODUCT NAME, QUANTITY, UNIT, DATE\n\n')

        for ind in range(len(inven)):
            # assign user input from stored inventory records to each inventory class attribute
            self.inv_obj.__dict__ = inven[ind]
            # insert each data column into text field one after the other
            st.insert(index='end',
                      chars=f"{self.inv_obj.prod_id}, {self.inv_obj.prod_name}, {self.inv_obj.qty}, {self.inv_obj.unit}, {self.inv_obj.entry_date}\n\n")

        # make the text field read-only
        st.config(state='disabled')
        # ensure that text can be copied to clipboard
        st.bind('<1>', lambda event: st.focus_set())

        invpageb = tk.Button(self.display_frame, text='Inventory Page', font=("Calibri", 12, 'bold'),
                             fg='purple', bg='white', height=1, width=15, command=self.invenpage)
        invpageb.grid(row=1, column=2, padx=5, stick='e')

        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_frame is not None:
            self.edit_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        self.display_frame.rowconfigure(list(range(3)), weight=1)
        self.display_frame.columnconfigure(list(range(3)), weight=1)
        self.display_frame.grid(row=1, rowspan=3, column=0, columnspan=3, sticky='nsew')

    def edit_inv(self):
        global edit_invid_entry, inven, lines

        # setup display frame
        self.display_frame = self.make_frame(page_title='EDIT INVENTORY RECORDS')

        inven = []
        lines = {}

        # retrieve inventory data from file
        # inven is a list of strings containing inventory records
        inven_rec = self.read_inv()
        print(len(inven_rec))

        for ind in range(len(inven_rec)):
            # labelled format of saved inventory record
            lines[ind] = eval(inven_rec[ind])
            # inven is a list of saved inventory instances
            inven.append(eval(inven_rec[ind]))

        st = scrolledtext.ScrolledText(self.display_frame, bg='purple', fg='white', wrap='word',
                                       font=("Calibri", 14, 'bold'))
        st.grid(row=0, column=1, rowspan=2, columnspan=2, sticky='nsew')

        # display headings for customer records
        st.insert(index='end',
                  chars='PRODUCT ID, PRODUCT NAME, QUANTITY, UNIT, DATE\n\n')

        for ind in range(len(inven)):
            # assign user input from stored inventory records to each inventory class attribute
            self.inv_obj.__dict__ = inven[ind]
            # insert each data column into text field one after the other
            st.insert(index='end',
                      chars=f"{self.inv_obj.prod_id}, {self.inv_obj.prod_name}, {self.inv_obj.qty}, {self.inv_obj.unit}, {self.inv_obj.entry_date}\n\n")

        # make the text field read-only
        st.config(state='disabled')
        # ensure that text can be copied to clipboard
        st.bind('<1>', lambda event: st.focus_set())

        # to edit the given row number (at row entry - 1)
        tk.Label(self.display_frame, text='ENTER PRODUCT ID:', font=("Calibri", 14, 'bold'), bg='purple',
                 fg='white').grid(row=2, column=0, padx=2, sticky='e')
        # prodid entry
        edit_invid_entry = tk.Entry(self.display_frame, font=("Calibri", 12, 'bold'), relief='sunken')
        edit_invid_entry.grid(row=2, column=1, pady=0, sticky='w')
        # edit button
        tk.Button(self.display_frame, text='Edit', font=("Calibri", 13, 'bold'), bg='orange', fg='white',
                  height=1, width=10, command=self.editing_inv).grid(row=2, column=2, sticky='w')
        # inventory page button
        tk.Button(self.display_frame, text='Inventory Page', font=("Calibri", 12, 'bold'), fg='purple', bg='white',
                  height=1, width=15, command=self.invenpage).grid(row=2, column=3, padx=5, pady=5, stick='se')

        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_frame is not None:
            self.edit_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        self.display_frame.rowconfigure(list(range(5)), weight=1)
        self.display_frame.columnconfigure(list(range(4)), weight=1)
        self.display_frame.grid(row=1, rowspan=3, column=0, columnspan=4, sticky='nsew')

    def editing_inv(self):
        global edit_invid_entry, inven, lines, edit_row_num

        self.display_frame = self.make_frame(page_title='UPDATING INVENTORY RECORD')

        prod_ids = []

        for rec in inven:
            prod_ids.extend([v.lower() for k,v in rec.items() if k.lower() == 'prod_id'])

        inp = edit_invid_entry.get()

        if inp.lower() not in prod_ids:
            return messagebox.showerror(title='INVALID ENTRY', message=f'{inp} IS NOT VALID')

        # get the row index of the selected product id
        for row, rec in lines.items():
            for k, v in rec.items():
                # if valid ID is entered
                if k.lower() == 'prod_id' and v.lower() == inp.lower():
                    edit_row_num = row
                    # print(f"Found at {edit_row_num}")

        # assign the selected record to the inventory object
        for row, rec in lines.items():
            if row == edit_row_num:
                self.inv_obj.__dict__ = rec
        print(self.inv_obj.__dict__)

        tk.Label(self.display_frame, text=f"ENTER NEW DATA BELOW", font=("Calibri", 14, 'bold'),
                 bg='purple', fg='white').grid(row=0, columnspan=3, sticky='ew', padx=50)

        # product labels and entries
        tk.Label(self.display_frame, text=f"PRODUCT:", font=("Calibri", 14, 'bold'), bg='purple',
                 fg='white').grid(row=1, rowspan=2, column=0, sticky='nse', padx=25, pady=15)

        # product name label and entry
        tk.Label(self.display_frame, text="NAME", font=("Calibri", 12, 'bold'),
                 bg='purple', fg='white').grid(row=1, column=1, sticky='sw', padx=25, pady=15)
        self.pname_entry = tk.Entry(self.display_frame, font=("Calibri", 14, 'bold'))
        self.pname_entry.insert(0, f'{self.inv_obj.prod_name}')
        self.pname_entry.grid(row=2, column=1, sticky='nw', padx=25, pady=5)

        # product quantity label and entry
        tk.Label(self.display_frame, text="QUANTITY", font=("Calibri", 12, 'bold'),
                 bg='purple', fg='white').grid(row=1, column=2, sticky='sw', padx=25, pady=15)
        self.pqty_entry = tk.Entry(self.display_frame, font=("Calibri", 14, 'bold'))
        self.pqty_entry.insert(0, f'{self.inv_obj.qty}')
        self.pqty_entry.grid(row=2, column=2, sticky='nw', padx=25, pady=5)

        # unit of measurement label and entry
        tk.Label(self.display_frame, text="Unit of Measurement", font=("Calibri", 12, 'bold'),
                 bg='purple', fg='white').grid(row=1, column=3, sticky='sw', padx=25, pady=15)
        self.punit_entry = tk.Entry(self.display_frame, font=("Calibri", 14, 'bold'))
        self.punit_entry.insert(0, f'{self.inv_obj.unit}')
        self.punit_entry.grid(row=2, column=3, sticky='nw', padx=25, pady=5)

        # date labels and entries section
        tk.Label(self.display_frame, text="DATE:", font=("Calibri", 14, 'bold'),
                 bg='purple', fg='white').grid(row=3, rowspan=2, column=0, sticky='nse', padx=25, pady=15)
        # Year label and entry
        tk.Label(self.display_frame, text=f"YEAR", font=("Calibri", 12, 'bold'),
                 bg='purple', fg='white').grid(row=3, column=1, sticky='sw', padx=25, pady=15)
        year = re.findall(r'(\d{2,4})-(\w{3})-(\d{1,2})', self.inv_obj.entry_date)[0][0]
        self.yrCbox = ttk.Combobox(self.display_frame, font=('calibri', 12, 'bold'), width=10,
                                   value=self.year, state='readonly')
        self.yrCbox.set(f'{year}')
        self.yrCbox.grid(row=4, column=1, sticky='nw', padx=25, pady=5)
        # Month label and entry
        tk.Label(self.display_frame, text="MONTH", font=("Calibri", 12, 'bold'),
                 bg='purple', fg='white').grid(row=3, column=2, sticky='sw', padx=25, pady=15)
        mont = re.findall(r'(\d{2,4})-(\w{3})-(\d{1,2})', self.inv_obj.entry_date)[0][1]
        self.monCbox = ttk.Combobox(self.display_frame, font=('calibri', 14, 'bold'), width=10,
                                    value=[v for k, v in self.month.items()], state='readonly')
        self.monCbox.set(f'{mont}')
        self.monCbox.grid(row=4, column=2, sticky='nw', padx=25, pady=5)
        # Day label and entry
        tk.Label(self.display_frame, text=f"DAY", font=("Calibri", 12, 'bold'),
                 bg='purple', fg='white').grid(row=3, column=3, sticky='sw', padx=25, pady=15)
        day = re.findall(r'(\d{2,4})-(\w{3})-(\d{1,2})', self.inv_obj.entry_date)[0][2]
        self.dayCbox = ttk.Combobox(self.display_frame, font=('calibri', 14, 'bold'), width=10, value=self.day, state='readonly')
        self.dayCbox.set(f'{day}')
        self.dayCbox.grid(row=4, column=3, sticky='nw', padx=25, pady=5)

        # update and inventory page buttons
        tk.Button(self.display_frame, text='Update', font=("Calibri", 12, 'bold'), bg='orange', fg='white',
                  height=1, width=15, command=self.update_inv).grid(row=5, column=1, padx=5, pady=5, stick='sw')

        tk.Button(self.display_frame, text='Inventory Page', font=("Calibri", 12, 'bold'), fg='purple', bg='white',
                  height=1, width=15, command=self.invenpage).grid(row=5, column=3, padx=5, pady=5, stick='sw')

        # clear the frames before and after this page
        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_frame is not None:
            self.edit_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        # display an adjustible frame containing the selected info
        self.display_frame.rowconfigure(list(range(8)), weight=1)
        self.display_frame.columnconfigure(list(range(4)), weight=1)
        self.display_frame.grid(row=1, rowspan=8, column=0, columnspan=4, sticky='nsew')

    def update_inv(self):
        global lines, edit_row_num
        prn, pq, pu, y, m, d = self.pname_entry.get(), self.pqty_entry.get(), self.punit_entry.get(), self.yrCbox.get(), self.monCbox.get(), self.dayCbox.get()

        # raise error alarm if any of the field is blank
        edited_entries = [prn, pq, pu, y, m, d]
        wspace = string.whitespace

        # when a field is blank
        if [True for entry in edited_entries if entry in wspace]:
            return messagebox.showerror(message="BLANK FIELD(S) DETECTED!")
        # when product name or unit of measurement is given in figures
        if [True for entry in [self.pname_entry.get(), self.punit_entry.get()] if entry.isdigit()]:
            return messagebox.showerror(message="PRODUCT NAME\nUNIT OF MEASUREMENT\n\nCannot contain only numbers")
        # when qty, date fields is/are not given in figures
        if not(pq.isdigit()):
            return messagebox.showerror(message="Product QUANTITY\n\ncan only be numbers")

        if not(messagebox.askyesno(title='CONFIRM UPDATE', message='Do You Want to Continue?')):
            return messagebox.showinfo(message='NO CHANGES MADE TO INVENTORY')

        # when confirmation is given by user
        self.display_frame = self.make_frame()

        self.save_edited_inv()  # save the old record before editing

        # reassign the newly entered values to the inventory object's name, qty, unit and date
        self.inv_obj.prod_name = prn.title()
        self.inv_obj.qty, self.inv_obj.unit = pq, pu.title()
        self.inv_obj.entry_date = f"{y}-{m}-{d}"

        # update the retrieved data from file with the changes made
        lines[edit_row_num] = self.inv_obj.__dict__

        # save updated version to file
        # print([rec for row, rec in lines.items()])
        with open(self.inv_obj.inv_data, 'w', encoding='utf8') as hand:
            for row, rec in lines.items():
                hand.writelines(f"{rec}\n")

        tk.Label(self.display_frame, text=f"PRODUCT\n{self.inv_obj.prod_name}", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=0, sticky='nsew', padx=25, pady=15)
        tk.Label(self.display_frame, text=f"ID\n{self.inv_obj.prod_id}: ", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=1, sticky='nsew', padx=25)
        tk.Label(self.display_frame, text=f"STOCK:\n{self.inv_obj.qty} {self.inv_obj.unit}", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=2, sticky='nsew', padx=25)
        tk.Label(self.display_frame, text=f"DATE:\n{self.inv_obj.entry_date}", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=3, sticky='nsew', padx=25)
        tk.Label(self.display_frame, text="HAS BEEN UPDATED!!", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=1, column=1, columnspan=2, sticky='NSEW', padx=25)

        tk.Button(self.display_frame, text='Inventory Page', font=("Calibri", 12, 'bold'), fg='purple', bg='white',
                  height=1, width=15, command=self.invenpage).grid(row=2, column=3, padx=5, pady=5, stick='se')

        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_frame is not None:
            self.edit_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        self.display_frame.rowconfigure(list(range(4)), weight=1)
        self.display_frame.columnconfigure(list(range(4)), weight=1)
        self.display_frame.grid(row=1, rowspan=4, column=0, columnspan=4, sticky='nsew')

    def save_edited_inv(self):
        with open(self.inv_obj.inv_edits, 'a', encoding='utf8') as hand:
            hand.writelines(f'{self.inv_obj.__dict__}\n')

    def delete_inv(self):
        global lines, inven, del_row, del_prodid_entry

        self.display_frame = self.make_frame("DELETE RECORD")

        inven = []
        lines = {}

        # retrieve inventory data from file
        # inven is a list of strings containing inventory records
        inven_rec = self.read_inv()
        print(len(inven_rec))

        for ind in range(len(inven_rec)):
            # labelled format of saved inventory record
            lines[ind] = eval(inven_rec[ind])
            # inven is a list of saved inventory instances
            inven.append(eval(inven_rec[ind]))

        st = scrolledtext.ScrolledText(self.display_frame, bg='purple', fg='white', wrap='word',
                                       font=("Calibri", 14, 'bold'))
        st.grid(row=0, column=1, rowspan=2, columnspan=2, sticky='nsew')

        # display headings for customer records
        st.insert(index='end', chars='PRODUCT ID, PRODUCT NAME, QUANTITY, UNIT, DATE\n\n')

        for ind in range(len(inven)):
            # assign user input from stored inventory records to each inventory class attribute
            self.inv_obj.__dict__ = inven[ind]
            # insert each data column into text field one after the other
            st.insert(index='end',
                      chars=f"{self.inv_obj.prod_id}, {self.inv_obj.prod_name}, {self.inv_obj.qty}, {self.inv_obj.unit}, {self.inv_obj.entry_date}\n\n")

        # make the text field read-only
        st.config(state='disabled')
        # ensure that text can be copied to clipboard
        st.bind('<1>', lambda event: st.focus_set())

        # user enters the selected row id to delete
        tk.Label(self.display_frame, text='ENTER PRODUCT ID:', font=("Calibri", 10, 'bold'), bg='purple',
                 fg='white').grid(row=2, column=0, padx=2, sticky='e')

        del_prodid_entry = tk.Entry(self.display_frame, font=("Calibri", 10, 'bold'))
        del_prodid_entry.grid(row=2, column=1, padx=2, sticky='w')

        # to edit the given row number (at row entry - 1)
        tk.Button(self.display_frame, text='Delete', font=("Calibri", 12, 'bold'),
                  bg='red', fg='white', height=1, width=10, command=self.erase_inv).grid(row=2, column=1, sticky='e')
        tk.Button(self.display_frame, text='Inventory Page', font=("Calibri", 12, 'bold'), fg='purple', bg='white',
                  height=1, width=15, command=self.invenpage).grid(row=2, column=3, padx=5, pady=5, stick='se')

        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_frame is not None:
            self.edit_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        self.display_frame.rowconfigure(list(range(3)), weight=1)
        self.display_frame.columnconfigure(list(range(4)), weight=1)
        self.display_frame.grid(row=1, rowspan=2, column=0, columnspan=4, sticky='nsew')

    def erase_inv(self):
        global lines, prod_ids, del_row, del_prodid_entry
        # raise error alarm if any of the field is blank

        self.display_frame = self.make_frame(page_title='RECORD DELETED')

        prod_ids = []

        for rec in inven:
            prod_ids.extend([v.lower() for k, v in rec.items() if k.lower() == 'prod_id'])

        inp = del_prodid_entry.get()

        if inp.lower() not in prod_ids:
            return messagebox.showerror(title='INVALID ENTRY', message=f'{inp} IS NOT VALID')

        if not(messagebox.askyesno(title='CONFIRM DELETE', message='Do You Want To Delete?')):
            return messagebox.showinfo(message='RECORD NOT DELETED')

        for row, rec in lines.items():
            for k, v in rec.items():
                # if valid ID is entered
                if k.lower() == 'prod_id' and v.lower() == inp.lower():
                    del_row = row
                    # print(f"Found at {del_row}")

        with open(self.inv_obj.inv_data, 'w', encoding='utf8') as hand:
            for row, rec in lines.items():
                if row == del_row:
                    # assign the selected row
                    self.inv_obj.__dict__ = rec
                    continue
                hand.writelines(f"{rec}\n")

        self.save_del_inv()  # save deleted record

        tk.Label(self.display_frame, text=f"PRODUCT\n{self.inv_obj.prod_name}", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=0, sticky='nsew', padx=25, pady=15)
        tk.Label(self.display_frame, text=f"ID\n{self.inv_obj.prod_id}: ", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=1, sticky='nsew', padx=25)
        tk.Label(self.display_frame, text=f"STOCK:\n{self.inv_obj.qty} {self.inv_obj.unit}", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=2, sticky='nsew', padx=25)
        tk.Label(self.display_frame, text=f"DATE:\n{self.inv_obj.entry_date}", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=3, sticky='nsew', padx=25)
        tk.Label(self.display_frame, text="HAS BEEN DELETED!!", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=1, column=1, columnspan=2, sticky='NSEW', padx=25)

        tk.Button(self.display_frame, text='Inventory Page', font=("Calibri", 12, 'bold'), fg='purple', bg='white',
                  height=1, width=15, command=self.invenpage).grid(row=2, column=3, padx=5, pady=5, stick='se')

        self.display_frame.rowconfigure([0, 1, 2, 3], weight=1)
        self.display_frame.columnconfigure(list(range(4)), weight=1)
        self.display_frame.grid(row=1, rowspan=len(inven) + 2, column=0, columnspan=4, sticky='nsew')

    def save_del_inv(self):
        with open(self.inv_obj.inv_dels, 'a', encoding='utf8') as hand:
            hand.writelines(f'{self.inv_obj.__dict__}\n')

# some functions
def login(event, ta, user):
    global eme, pe
    email, pwd = eme.get(), pe.get()
    mandatory_entries = [email, pwd]

    ta.display_frame = tk.LabelFrame(ta.master, bg='gold')
    ta.display_frame.focus()
    ta.display_frame.bind('<Return>', lambda event: ta.menupage(event))

    wspace = string.whitespace

    # check for empty fields
    if [True for entry in mandatory_entries if (entry in wspace)]:
        return messagebox.showerror(title='Blank Field', message='BLANK FIELD(S) DETECTED!')

    # email constraints
    if not (re.findall(r'(.+)@(.+)[.](.+)', email)):
        return messagebox.showerror(title='INVALID EMAIL', message='Invalid email address'
                                                                     '\n\nPlease check Email for @ or .')
    # password length
    if len(pwd) < 5:
        return messagebox.showerror(title='Password too short',
                                    message='Password Must Contain 5 or more characters')

    # extract username from email address
    stop = email.find("@")
    uname = email[:stop].capitalize()
    # print(email)
    pFound, eFound = False, False

    for path, folders, files in os.walk(user.dir_path):
        for folder in folders:
            if folder != uname:
                continue

            elif folder == uname:
                # print(f"Checking {uname}'s login details")
                with open(f'{path}\\{folder}\\login_data.txt', 'r', encoding='utf8') as hand:
                    data = hand.readlines()
                for line in data:
                    attr = eval(line)
                    # print(type(attr), attr)
                    for k, v in attr.items():
                        # check for matching email address and password
                        if k.lower() == 'email' and v.lower() == email.lower():
                            print(k, v)
                            eFound = True
                        if k.lower() == 'password' and v == pwd:
                            # print(k, v)
                            pFound = True
                            break

    if eFound and pFound:
        user.__dict__ = attr
        # print(f'Found {user.__dict__}')

        tk.Label(ta.display_frame, text=f"{user.username}'s Login Successful",
                 font=("Calibri", 10, 'bold'),
                 bg='gold', fg='black').grid(row=0, column=1, columnspan=2, sticky='NSEW', padx=25)

        btn = ttk.Button(ta.display_frame, text=f"Go to {user.company_name}'s Menu", width=30)
        btn.bind('<Button-1>', lambda event: ta.menupage(event))
        btn.grid(row=1, column=0, columnspan=3, sticky='NSEW', padx=25)

        if ta.display_frame is not None:
            ta.display_frame.grid_forget()

        ta.display_frame.rowconfigure(list(range(3)), weight=1)
        ta.display_frame.columnconfigure(list(range(3)), weight=1)
        ta.display_frame.grid(row=1, sticky='nsew')

    else:
        return messagebox.showwarning(message='Incorrect Email/Password')

def save_obj(user):

    try:
        # create all the necessary app files for current user at their repository
        with open(f'{user.filepath}\\__init__.py', 'w', encoding='utf8') as hand:
            hand.writelines('')
        # user's login data file
        with open(f'{user.filepath}\\login_data.txt', 'w', encoding='utf8') as hand:
            hand.writelines(f'{user.__dict__}\n')

        # inventory data files
        with open(f'{user.filepath}\\Inventory\\inv_data.txt', 'w', encoding='utf8') as hand:
            hand.writelines('')  # for new entries
        with open(f'{user.filepath}\\Inventory\\edited_inv.txt', 'w', encoding='utf8') as hand:
            hand.writelines('')  # for old entries before editing
        with open(f'{user.filepath}\\Inventory\\deleted_inv.txt', 'w', encoding='utf8') as hand:
            hand.writelines('')  # for discarded entries

        # customer data file
        with open(f'{user.filepath}\\Customers\\cust_data.txt', 'w', encoding='utf8') as hand:
            hand.writelines('')
        with open(f'{user.filepath}\\Customers\\edited_cust.txt', 'w', encoding='utf8') as hand:
            hand.writelines('')  # for old entries before editing
        with open(f'{user.filepath}\\Customers\\deleted_cust.txt', 'w', encoding='utf8') as hand:
            hand.writelines('')  # for discarded entries

        # sales data file
        with open(f'{user.filepath}\\Sales\\sales_data.txt', 'w', encoding='utf8') as hand:
            hand.writelines('')
        with open(f'{user.filepath}\\Sales\\edited_sales.txt', 'w', encoding='utf8') as hand:
            hand.writelines('')  # for old entries before editing
        with open(f'{user.filepath}\\Sales\\deleted_sales.txt', 'w', encoding='utf8') as hand:
            hand.writelines('')  # for discarded entries

        # accounts data file
        with open(f'{user.filepath}\\Accounts\\acct_data.txt', 'w', encoding='utf8') as hand:
            hand.writelines('')
        with open(f'{user.filepath}\\Accounts\\edited_acct.txt', 'w', encoding='utf8') as hand:
            hand.writelines('')  # for old entries before editing
        with open(f'{user.filepath}\\Accounts\\deleted_acct.txt', 'w', encoding='utf8') as hand:
            hand.writelines('')  # for discarded entries

        # transactions data file
        with open(f'{user.filepath}\\AccTransactions\\acctrans_data.txt', 'w', encoding='utf8') as hand:
            hand.writelines('')
        with open(f'{user.filepath}\\AccTransactions\\edited_acctrans.txt', 'w', encoding='utf8') as hand:
            hand.writelines('')  # for old entries before editing
        with open(f'{user.filepath}\\AccTransactions\\deleted_acctrans.txt', 'w', encoding='utf8') as hand:
            hand.writelines('')  # for discarded entries

        print(f'New Files Created at {user.filepath}')

    except:
        os.rmdir(f'{user.filepath}')
        print('Error: Something Went wrong')
        quit()

def uniqueid():
    '''
    randomly generates a ten-digits integer
    :return: a generator that increments by 1
    '''
    start = random.getrandbits(32)  # return a random number of ten digits
    while True:
        yield start  # return the random ten-digits
        start += 1  # increment the random ten-digit number by 1

win = tk.Tk()
# selecting system's screen width height
sw, sh = win.winfo_screenwidth(), win.winfo_screenheight()
# app width, app height
aw, ah = int(sw*.70), int(sh*.7)
# starting horizontal and vertical points
x, y = int(sw*(1 - 0.73)), int(sh*(1 - 0.77))
# specifying the size of app frame
win.geometry(f"{aw}x{ah}+{x}+{y}")

# pass inventory object into the transapp
ta = TransApp(win)

ta.setup_frames()
ta.setup_status_bar()
ta.frontpage()

win.rowconfigure(1, weight=1)
win.columnconfigure(0, weight=1)

win.mainloop()