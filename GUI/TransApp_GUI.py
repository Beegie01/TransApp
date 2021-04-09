import tkinter as tk, datetime, random, os, string, re
from tkinter import messagebox, scrolledtext
from inventory_cls import Inventory
from customer_cls import Customer
from sales_cls import Sales
from user_login import User


dir_path = 'C:\\Users\\welcome\\Desktop\\MyFuncs'

if dir_path not in os.sys.path:
    os.sys.path.append(dir_path)

from mydict_funcs import del_item

eme, pe = None, None


class TransApp:
    # create general folder for users' data
    # create initialize file for python at specified path
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
        # create an object of sales
        self.sales_obj = Sales()
        

        # menu bar section
        self.menu_bar = tk.Menu(self.master)
        main_menu = tk.Menu(self.menu_bar, tearoff=0)
        main_menu.add_command(label="HOME", command=lambda: self.menupage())
        main_menu.add_command(label="SIGN OUT", command=lambda: self.firstpage())
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

    def setup_frames(self):
        # status bar frame
        self.status_bar_frame = tk.Frame(master=self.master, bg='gold')
        self.status_bar_frame.rowconfigure(0, weight=1)
        self.status_bar_frame.columnconfigure([0, 1, 2, 3, 4], weight=1)
        self.status_bar_frame.grid(row=0, column=0, columnspan=5, sticky='we')

        # frame for front page containing one row and one column
        self.introFrame = tk.Frame(master=self.master, bg='GOLD')
        self.introFrame.rowconfigure(0, weight=1)
        self.introFrame.columnconfigure(0, weight=1)

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
        self.status_date = tk.Label(master=self.status_bar_frame, font=('arial black', 12), fg='black', bg='gold',
                                    text=f"{datetime.datetime.date(datetime.datetime.today())}")
        self.status_date.grid(row=0, column=4, sticky='ew')
        self.status_appname = tk.Label(master=self.status_bar_frame, font=('arial black', 12), fg='black', bg='gold',
                                       text=f"TransApp March 2021")
        self.status_appname.grid(row=0, column=3, sticky='nsew')
        
    def firstpage(self):

        self.display_frame = tk.LabelFrame(master=self.master, text='SETUP', bg='gold', font=('arial black', 12))
        menu=tk.Menu()

        self.master.config(menu=menu)

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
        # login button
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

        tk.Label(self.display_frame, text='Company Name', fg='black', bg='gold', font=('calibri', 12, 'bold')).grid(row=0,
                                                                                                            sticky='e')
        ce = tk.Entry(self.display_frame, font=('calibri', 12))
        ce.grid(row=0, column=1, sticky='w', padx=3, pady=5)

        tk.Label(self.display_frame, text='Email', fg='black', bg='gold', font=('calibri', 12, 'bold')).grid(row=1, sticky='e')
        eme = tk.Entry(self.display_frame, font=('calibri', 12))
        eme.grid(row=1, column=1, sticky='w', padx=3, pady=5)

        tk.Label(self.display_frame, text='Password', fg='black', bg='gold', font=('calibri', 12, 'bold')).grid(row=2,
                                                                                                        sticky='e')
        pe = tk.Entry(self.display_frame, font=('calibri', 12), show='*')
        pe.grid(row=2, column=1, sticky='w', padx=3, pady=5)

        # radio button to show and hide password entries
        # passw = tk.StringVar(self.display_frame, value=None)
        tk.Radiobutton(self.display_frame, text='Show', fg='black', bg='gold', font=('calibri', 10, 'bold'),
                       command=lambda: self.showpassword(pe)).grid(row=3, column=1, sticky='w')
        tk.Radiobutton(self.display_frame, text='Hide', fg='black', bg='gold', font=('calibri', 10, 'bold'),
                       command=lambda: self.hidepassword(pe)).grid(row=3, column=1, sticky='e')

        tk.Label(self.display_frame, text='Confirm Password', fg='black', bg='gold', font=('calibri', 12, 'bold')).grid(row=4,
                                                                                                                sticky='e')
        cpe = tk.Entry(self.display_frame, font=('calibri', 12), show='*')
        cpe.grid(row=4, column=1, sticky='w', padx=3, pady=5)
        # passw = tk.StringVar(self.display_frame, value=None)
        tk.Radiobutton(self.display_frame, text='Show', fg='black', bg='gold', font=('calibri', 10, 'bold'),
                       command=lambda: self.showpassword(cpe)).grid(row=5, column=1, sticky='w')

        tk.Radiobutton(self.display_frame, text='Hide', fg='black', bg='gold', font=('calibri', 10, 'bold'),
                       command=lambda: self.hidepassword(cpe)).grid(row=5, column=1, sticky='e')

        # submit signup button
        tk.Button(self.display_frame, text='Create User', bg='green', fg='white', command=self.setattr).grid(row=6, column=1,
                                                                                                     sticky='e')

        # front page
        tk.Button(self.display_frame, text='App Menu', fg='gold', bg='white', command=self.firstpage).grid(row=6, column=0,
                                                                                                    sticky='e')

        self.display_frame.rowconfigure(list(range(8)), weight=1)
        self.display_frame.columnconfigure(list(range(3)), weight=1)
        self.display_frame.grid(row=1, rowspan=4, column=0, columnspan=5, sticky='nsew')
        

    def showpassword(self, entry):
        global pe, cpe
        if entry == pe:
            pe.config(show='')
        elif entry == cpe:
            cpe.config(show='')

    def hidepassword(self, entry):
        global pe, cpe
        if entry == pe:
            pe.config(show='*')
        if entry == cpe:
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

        save_obj(self.login_user)

        self.display_frame = tk.LabelFrame(self.master, bg='gold')

        tk.Label(self.display_frame, text=f'New User Created!\n{self.login_user.username}', fg='black', bg='gold',
                 font=('calibri', 12, 'bold')
                 ).grid(row=1, columnspan=3, sticky='NSEW')
        tk.Button(self.display_frame, text="Login Page", command=self.loginpage, fg='blue', bg='white',
                  font=('calibri', 12, 'bold')
                  ).grid(row=4, columnspan=3, sticky='ew')

        self.display_frame.rowconfigure(list(range(8)), weight=1)
        self.display_frame.columnconfigure(list(range(3)), weight=1)
        self.display_frame.grid(row=1, rowspan=4, column=0, columnspan=5, sticky='nsew')

    def loginpage(self):
        global eme, pe
        self.display_frame = tk.LabelFrame(master=self.master, text='LOGIN USER', bg='gold', font=('arial black', 12))

        tk.Label(self.display_frame, text='Email', fg='black', bg='gold', font=('calibri', 12, 'bold')).grid(row=0, sticky='e')
        eme = tk.Entry(self.display_frame, font=('calibri', 12))
        eme.grid(row=0, column=1, sticky='w', padx=3, pady=5)

        tk.Label(self.display_frame, text='Password', fg='black', bg='gold', font=('calibri', 12, 'bold')).grid(row=1,
                                                                                                        sticky='e')
        pe = tk.Entry(self.display_frame, font=('calibri', 12), show='*')
        pe.grid(row=1, column=1, sticky='w', padx=3, pady=5)

        # radio button to show and hide password entries
        # passw = tk.StringVar(self.display_frame, value=None)
        tk.Radiobutton(self.display_frame, text='Show', fg='black', bg='gold', font=('calibri', 10, 'bold'),
                       command=lambda: self.showpassword(pe)).grid(row=3, column=1, sticky='w')
        tk.Radiobutton(self.display_frame, text='Hide', fg='black', bg='gold', font=('calibri', 10, 'bold'),
                       command=lambda: self.hidepassword(pe)).grid(row=3, column=1, sticky='e')

        # login/signin button
        tk.Button(self.display_frame, text="Sign in", command=lambda: login(self, self.login_user), fg='blue', bg='white',
                  font=('calibri', 12, 'bold')
                  ).grid(row=5, column=1, sticky='e')

        # front page
        tk.Button(self.display_frame, text='App Menu', bg='green', fg='white', command=self.firstpage).grid(row=5, column=1,
                                                                                                    sticky='w')

        if self.display_frame is not None:
            self.display_frame.grid_forget()

        self.display_frame.rowconfigure(list(range(6)), weight=1)
        self.display_frame.columnconfigure(list(range(3)), weight=1)
        self.display_frame.grid(row=1, rowspan=4, column=0, columnspan=5, sticky='nsew')

    def frontpage(self):
        # place label on frame
        frontlabel = tk.Label(master=self.introFrame, text='\nTRANSAPP\n\nBY\n\nBEEGIE\n\nMARCH, 2021', fg='black', bg='gold', font=('Arial Black', 20))
        frontlabel.grid(row=0, sticky='nsew')
        menuButton = tk.Button(self.introFrame, text=" CLICK HERE TO START ", fg='white', bg='green',
                                  font=('arial black', 14), command=self.firstpage)
        menuButton.grid(row=1, sticky='sew')

        # place label frame on app frame starting at row 1, column 0
        self.introFrame.grid(row=0, rowspan=4, column=0, columnspan=5, sticky='nsew')

    def menupage(self):
        # frame for menu page containing four rows and one column
        self.homeFrame = tk.LabelFrame(master=self.master, text='HOME', fg='black', font=('arial black', 12))
        self.homeFrame.rowconfigure([0, 1, 2, 3], weight=1)
        self.homeFrame.columnconfigure(0, weight=1)

        self.master.config(menu=self.menu_bar)

        # menu sections
        self.inventoryb = tk.Button(self.homeFrame, text="INVENTORY", fg='white', bg='purple',
                                    font=('arial black', 14), command=lambda: self.invenpage())
        self.customerb = tk.Button(self.homeFrame, text="CUSTOMERS", fg='white', bg='blue',
                                   font=('arial black', 14), command=lambda: self.custpage())
        self.salesb = tk.Button(self.homeFrame, text="SALES", fg='white', bg='brown',
                                font=('arial black', 14), command=lambda: self.salepage())
        self.accountb = tk.Button(self.homeFrame, text="ACCOUNTS", fg='white', bg='green',
                                  font=('arial black', 14), )
        # menu sections
        self.inventoryb.grid(row=0, padx=40, sticky='nsew')
        self.customerb.grid(row=1, padx=30, sticky='nsew')
        self.salesb.grid(row=2, padx=20, sticky='nsew')
        self.accountb.grid(row=3, padx=10, sticky='nsew')

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

        self.homeFrame.grid(row=1, rowspan=4, column=0, columnspan=5, sticky='nsew')

    def salepage(self):
        # frame for customer sales page containing three rows and one column
        self.sectionFrame = tk.LabelFrame(master=self.master, text='SALES', font=('arial black', 12), bg='brown',
                                          fg='white')
        self.sectionFrame.rowconfigure([0, 1, 2, 3], weight=1)
        self.sectionFrame.columnconfigure(0, weight=1)

        # display sales options
        tk.Button(self.sectionFrame, text='ADD NEW ORDER', bg='white', fg='blue',
                                font=('arial black', 14), command=self.new_sale).grid(row=1, padx=60, pady=10, sticky='nsew')
        tk.Button(self.sectionFrame, text='UPDATE TRANSACTION', bg='white', fg='orange',
                              font=('arial black', 14), command=self.edit_sale).grid(row=2, padx=80, pady=10, sticky='nsew')
        tk.Button(self.sectionFrame, text='DELETE TRANSACTION', bg='white', fg='red',
                              font=('arial black', 14), command=self.delete_sale).grid(row=3, padx=100, pady=10, sticky='nsew')
        tk.Button(self.sectionFrame, text='SALES TRANSACTION VIEW', bg='white', fg='green',
                              font=('arial black', 14), command=lambda: self.display_sale()).grid(row=0, padx=40, pady=10, sticky='nsew')

        # display inventory page's frame
        if self.display_frame is not None:
            self.display_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()
        if self.homeFrame is not None:
            self.homeFrame.grid_forget()

        self.sectionFrame.grid(row=1, rowspan=4, column=0, columnspan=5, sticky='nsew')

    def new_sale(self):
        bg, fg = 'brown', 'white'

        # frame for input of new inventory
        self.new_frame = tk.LabelFrame(self.master, text='NEW CUSTOMER ORDER', fg=fg, font=('arial black', 12),
                                       bg=bg)
        self.new_frame.rowconfigure(list(range(9)), weight=1)
        self.new_frame.columnconfigure(list(range(5)), weight=1)

        # place new sale form
        # Order labels and entries
        tk.Label(self.new_frame, text='Orders', font=('calibri', 16),
                 bg=bg, fg=fg, height=1).grid(row=0, column=0, padx=10, stick='nsew')
        
        # ordered quantity
        tk.Label(self.new_frame, text='Ordered Quantity', font=('calibri', 16),
                 bg=bg, fg=fg, height=1).grid(row=0, column=1, stick='nw')
        self.ord_qtyEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'))
        self.ord_qtyEntry.grid(row=0, column=1, padx=2, pady=30, stick='sw')
        
        # rate of order
        tk.Label(self.new_frame, text='Rate of Order', font=('calibri', 16),
                 bg=bg, fg=fg, height=1).grid(row=0, column=2, stick='nw')
        self.ord_rateEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'))
        self.ord_rateEntry.grid(row=0, column=2, padx=2, pady=30, stick='sw')
        
        # amount due
        tk.Label(self.new_frame, text='Amount Due', font=('calibri', 16),
                 bg=bg, fg=fg, height=1).grid(row=0, column=3, stick='nw')
        self.amountEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'))
        self.amountEntry.grid(row=0, column=3, padx=2, pady=30, stick='sw')

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

        # customer order date
        tk.Label(self.new_frame, text='Date of Order', font=('calibri', 16),
                 bg=bg, fg=fg, height=1).grid(row=2, column=0, padx=10, stick='nsew')
        # day
        tk.Label(self.new_frame, text='Day', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=2, column=1, padx=5, stick='nw')
        self.orddayEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'), width=10)
        self.orddayEntry.insert(0, str(datetime.date.today().day))
        self.orddayEntry.grid(row=2, column=1, padx=5, pady=30, stick='sw')
        # month
        tk.Label(self.new_frame, text='Month', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=2, column=2, padx=5, stick='nw')
        self.ordmonthEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'), width=10)
        self.ordmonthEntry.insert(0, str(datetime.date.today().month))
        self.ordmonthEntry.grid(row=2, column=2, padx=5, pady=30, stick='sw')
        # year
        tk.Label(self.new_frame, text='Year', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=2, column=3, stick='nw')
        self.ordyrEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'), width=10)
        self.ordyrEntry.insert(0, str(datetime.date.today().year))
        self.ordyrEntry.grid(row=2, column=3, pady=30, stick='sw')

        # customer amount deposited
        tk.Label(self.new_frame, text='Amount Deposited', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=3, column=0, padx=10, stick='nsew')
        self.depEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'), width=10)
        self.depEntry.grid(row=3, column=0, padx=5, pady=30, stick='sw')

        # customer balance
        tk.Label(self.new_frame, text='Balance', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=3, column=2, stick='nw')
        self.balEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'), width=10)
        self.balEntry.grid(row=3, column=2, padx=5, pady=30, stick='sw')

        # payment status
        tk.Label(self.new_frame, text='Payment Status', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=4, column=0, padx=5, stick='nsew')
        self.off_addrText = tk.Text(self.new_frame, font=('calibri', 16, 'bold'), width=10, height=3)
        self.off_addrText.grid(row=4, column=1, padx=5, pady=30, sticky='ew')

        # date of completion
        tk.Label(self.new_frame, text='Date of Completion', font=('calibri', 16),
                 bg=bg, fg=fg, height=1).grid(row=5, column=0, padx=5, sticky='nsew')
        # day
        tk.Label(self.new_frame, text='Day', font=('calibri', 16),
                 bg=bg, fg=fg, height=1).grid(row=5, column=1, sticky='nw')
        self.compdayEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'), width=10)
        self.compdayEntry.insert(0, str(datetime.date.today().day))
        self.compdayEntry.grid(row=5, column=1, padx=5, pady=30, sticky='sw')
        # month
        tk.Label(self.new_frame, text='Month', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=5, column=2, sticky='nw')
        self.compmonthEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'), width=10)
        self.compmonthEntry.insert(0, str(datetime.date.today().month))
        self.compmonthEntry.grid(row=5, column=2, padx=5, pady=30, sticky='sw')
        # year
        tk.Label(self.new_frame, text='Year', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=5, column=3, sticky='nw')
        self.compyrEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'), width=10)
        self.compyrEntry.insert(0, str(datetime.date.today().year))
        self.compyrEntry.grid(row=5, column=3, pady=30, sticky='sw')

        submitButton = tk.Button(self.new_frame, text='Submit', font=("Calibri", 14, 'bold'),
                                 fg='white', bg='green', width=10, height=2, command=self.submit_sale)
        submitButton.grid(row=7, column=2, padx=10, sticky='se')

        custpageb = tk.Button(self.new_frame, text='Customer Page', font=("Calibri", 14, 'bold'),
                              fg='blue', bg='white', height=2, width=15, command=self.salepage)
        custpageb.grid(row=7, column=0, padx=15, stick='se')

        # display inventory page's frame
        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.sectionFrame is not None:
            self.sectionFrame.grid_forget()
        self.new_frame.grid(row=1, rowspan=8, column=0, columnspan=3, sticky='nsew')


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

    def custpage(self):
        # frame for customer page containing three rows and one column
        self.sectionFrame = tk.LabelFrame(master=self.master, text='CUSTOMER', font=('arial black', 12), bg='blue',
                                      fg='white')
        self.sectionFrame.rowconfigure([0, 1, 2, 3], weight=1)
        self.sectionFrame.columnconfigure(0, weight=1)

        # display customer options
        tk.Button(self.sectionFrame, text='ADD NEW CUSTOMER', bg='white', fg='blue',
                                font=('arial black', 14), command=self.new_cust).grid(row=1, padx=60, pady=10, sticky='nsew')
        tk.Button(self.sectionFrame, text='UPDATE CUSTOMER RECORD', bg='white', fg='orange',
                              font=('arial black', 14), command=self.edit_cust).grid(row=2, padx=80, pady=10, sticky='nsew')
        tk.Button(self.sectionFrame, text='DELETE CUSTOMER RECORD', bg='white', fg='red',
                              font=('arial black', 14), command=self.delete_cust).grid(row=3, padx=100, pady=10, sticky='nsew')
        tk.Button(self.sectionFrame, text='VIEW CUSTOMER RECORDS', bg='white', fg='green',
                              font=('arial black', 14), command=lambda: self.display_cust()).grid(row=0, padx=40, pady=10, sticky='nsew')

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
        self.bdayEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'), width=10)
        self.bdayEntry.insert(0, str(datetime.date.today().day))
        self.bdayEntry.grid(row=2, column=1, padx=5, pady=30, stick='sw')
        # month
        tk.Label(self.new_frame, text='Month', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=2, column=2, padx=5, stick='nw')
        self.bmonthEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'), width=10)
        self.bmonthEntry.insert(0, str(datetime.date.today().month))
        self.bmonthEntry.grid(row=2, column=2, padx=5, pady=30, stick='sw')
        # year
        tk.Label(self.new_frame, text='Year', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=2, column=3, stick='nw')
        self.byrEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'), width=10)
        self.byrEntry.insert(0, str(datetime.date.today().year))
        self.byrEntry.grid(row=2, column=3, pady=30, stick='sw')

        # nationality
        tk.Label(self.new_frame, text='Nationality:', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=3, column=0, padx=10, stick='nsew')
        tk.Label(self.new_frame, text='Country of Origin', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=3, column=1, stick='nw')
        self.natEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'), width=10)
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
        self.regdayEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'), width=10)
        self.regdayEntry.insert(0, str(datetime.date.today().day))
        self.regdayEntry.grid(row=5, column=1, padx=5, pady=30, sticky='sw')
        # month
        tk.Label(self.new_frame, text='Month', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=5, column=2, sticky='nw')
        self.regmonthEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'), width=10)
        self.regmonthEntry.insert(0, str(datetime.date.today().month))
        self.regmonthEntry.grid(row=5, column=2, padx=5, pady=30, sticky='sw')
        # year
        tk.Label(self.new_frame, text='Year', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=5, column=3, sticky='nw')
        self.regyrEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'), width=10)
        self.regyrEntry.insert(0, str(datetime.date.today().year))
        self.regyrEntry.grid(row=5, column=3, pady=30, sticky='sw')

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
        bday, bmon, byr = self.bdayEntry.get(), self.bmonthEntry.get(), self.byrEntry.get()
        natn, orig_state = self.natEntry.get(), self.stateEntry.get()
        off_addr = self.off_addrText.get(index1='1.0', index2='end')
        regday, regmon, regyr = self.regdayEntry.get(), self.regmonthEntry.get(), self.regyrEntry.get()

        # collection of entry fields
        mandatory_entries = [fname, lname, gender, bday, bmon, byr, natn, orig_state, off_addr, regday, regmon, regyr]
        num_type_entries = [bday, bmon, byr, regday, regmon, regyr]
        str_type_entries = [fname, midname, lname, gender, natn, orig_state, off_addr]
        wspace = string.whitespace
        puncs = string.punctuation

        # check for empty field
        if [True for entry in mandatory_entries if (entry in wspace)]:
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

        for entry in num_type_entries:
            try:
                int(entry)
            except ValueError as VE:
                # figures have not been entered, if error was raised
                return messagebox.showerror(title='Invalid Data Type', message=f'Character {entry} is not allowed here!')

        # numerical constraints
        if int(byr) not in range(1900, 2021) or (int(regyr) not in range(2010, 2022)) or [True for mon in [regmon, bmon] if int(mon) not in range(13)] or [True for day in [bday, regday] if int(day) not in range(32)]:
            return messagebox.showerror(title='OUT OF RANGE ENTRY', message=f'OUT OF RANGE VALUE(S) HAS BEEN DETECTED!\n\nPlease Check the REGISTRATION DATE\nDATE OF BIRTH entries')

        # string constraints
        if [True for entry in [fname, lname, natn, orig_state,] if not(entry.isalnum())] or [True for entry in [fname, lname, natn, orig_state] for char in
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
        saveb = tk.Button(self.submit_frame, text='Save', font=("Calibri", 14, 'bold'),
                          bg='green', fg='white', height=3, width=10, command=self.savecust)
        saveb.grid(row=4, column=0, padx=5, stick='ew')
        cancelb = tk.Button(self.submit_frame, text='Cancel', font=("Calibri", 14, 'bold'),
                            bg='red', fg='white', height=3, width=10, command=self.new_cust)
        cancelb.grid(row=4, column=3, padx=5, stick='ew')

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
        st.grid(row=0, column=0, rowspan=len(cust), columnspan=8, sticky='nsew')
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
        custpageb.grid(row=len(cust) + 2, column=3, padx=5, pady=5, stick='se')

        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_frame is not None:
            self.edit_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        self.display_frame.rowconfigure(list(range(len(cust) + 2)), weight=1)
        self.display_frame.columnconfigure(list(range(9)), weight=1)
        self.display_frame.grid(row=1, rowspan=len(cust) + 2, column=0, columnspan=4, sticky='nsew')

    def edit_cust(self):
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
        st = scrolledtext.ScrolledText(self.display_frame, bg='blue', fg='white', wrap='word', font=("Calibri", 14, 'bold'))
        st.grid(row=0, column=0, rowspan=len(cust), columnspan=8, sticky='nsew')
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
                 fg='white').grid(row=len(cust) + 2, column=0, padx=2, sticky='e')
        # custid entry
        edit_custid_entry = tk.Entry(self.display_frame, font=("Calibri", 12, 'bold'), relief='sunken')
        edit_custid_entry.grid(row=len(cust) + 2, column=1, padx=2, sticky='ew')
        # edit button
        tk.Button(self.display_frame, text='Edit', font=("Calibri", 12, 'bold'),
                  bg='orange', fg='white', height=1, width=10, command=self.editing_cust).grid(row=len(cust) + 2,
                                                                                               padx=5, column=2, sticky='w')

        custpageb = tk.Button(self.display_frame, text='Customer Page', font=("Calibri", 12, 'bold'),
                              fg='blue', bg='white', height=1, width=15, command=self.custpage)
        custpageb.grid(row=len(cust) + 2, column=6, padx=5, pady=5, stick='se')

        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_frame is not None:
            self.edit_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        self.display_frame.rowconfigure(list(range(len(cust) + 2)), weight=1)
        self.display_frame.columnconfigure(list(range(9)), weight=1)
        self.display_frame.grid(row=1, rowspan=len(cust) + 2, column=0, columnspan=4, sticky='nsew')

    def editing_cust(self):
        global edit_custid_entry, cust, lines, edit_row

        self.display_frame = self.make_frame(page_title='UPDATING CUSTOMER RECORD', background_color='blue', foreground_color='white')

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
        tk.Label(self.display_frame, text="GENDER", font=("Calibri", 10, 'bold'),
                 bg='blue', fg='white').grid(row=1, column=3, sticky='sw', padx=25, pady=15)
        self.gender_entry = tk.Entry(self.display_frame)
        self.gender_entry.insert(0, f'{self.cust_obj.gender}')
        self.gender_entry.grid(row=2, column=3, sticky='w', padx=25, pady=5)

        # date of birth labels and entries
        tk.Label(self.display_frame, text="DATE OF BIRTH", font=("Calibri", 10, 'bold'),
                 bg='blue', fg='white').grid(row=3, column=0, sticky='sw', padx=25, pady=15)

        tk.Label(self.display_frame, text="BIRTH YEAR", font=("Calibri", 10, 'bold'),
                 bg='blue', fg='white').grid(row=3, column=1, sticky='sw', padx=25, pady=15)
        year = re.findall(r'(\d{2,4})-(\d{1,2})-(\d{1,2})', self.cust_obj.date_of_birth)[0][0]
        self.byear_entry = tk.Entry(self.display_frame)
        self.byear_entry.insert(0, f'{year}')
        self.byear_entry.grid(row=4, column=1, sticky='w', padx=25, pady=5)

        tk.Label(self.display_frame, text="BIRTH MONTH", font=("Calibri", 10, 'bold'),
                 bg='blue', fg='white').grid(row=3, column=2, sticky='sw', padx=25, pady=15)
        month = re.findall(r'(\d{2,4})-(\d{1,2})-(\d{1,2})', self.cust_obj.date_of_birth)[0][1]
        self.bmon_entry = tk.Entry(self.display_frame)
        self.bmon_entry.insert(0, f'{month}')
        self.bmon_entry.grid(row=4, column=2, sticky='w', padx=25, pady=5)

        tk.Label(self.display_frame, text="BIRTH DAY", font=("Calibri", 10, 'bold'),
                 bg='blue', fg='white').grid(row=3, column=3, sticky='sw', padx=25, pady=15)
        day = re.findall(r'(\d{2,4})-(\d{1,2})-(\d{1,2})', self.cust_obj.date_of_birth)[0][2]
        self.bd_entry = tk.Entry(self.display_frame)
        self.bd_entry.insert(0, f'{day}')
        self.bd_entry.grid(row=4, column=3, sticky='w', padx=25, pady=5)

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
        self.display_frame.grid(row=1, rowspan=len(cust) + 2, column=0, columnspan=4, sticky='nsew')

    def update_cust(self):
        global lines, edit_row
        # raise error alarm if any of the field is blank
        fname, mname, lname, gender = self.fname_entry.get(), self.mname_entry.get(), self.lname_entry.get(), self.gender_entry.get()
        natn, orig_state, off_addr = self.natn_entry.get(), self.ori_state_entry.get(), self.off_entry.get(index1='1.0', index2='end')
        byr, bmon, bday = self.byear_entry.get(), self.bmon_entry.get(),self.bd_entry.get()

        wspace = string.whitespace
        puncs = string.punctuation

        # collection of entry fields
        mandatory_entries = [fname, lname, gender, byr, bmon, bday, natn, orig_state, off_addr]
        punc_entries = [fname, lname, natn, orig_state]
        num_type_entries = [byr, bmon, bday]
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

        for entry in num_type_entries:
            try:
                int(entry)
            except ValueError as VE:
                # figures have not been entered, if error was raised
                return messagebox.showerror(title='Invalid Data Type',
                                            message=f'Character {entry} is not allowed here!')

        # numerical constraints
        if int(byr) not in range(1921, 2021) or int(bmon) not in range(13) or int(bday) not in range(32):
            return messagebox.showerror(title='OUT OF RANGE ENTRY',
                                        message=f'OUT OF RANGE VALUE(S) HAS BEEN DETECTED!\n\nPlease Check the REGISTRATION DATE\nDATE OF BIRTH entries')

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
        # print(Inventory.cust_data)
        with open(Customer.cust_data, 'w', encoding='utf8') as hand:
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
        st.grid(row=0, column=0, rowspan=len(cust), columnspan=8, sticky='nsew')
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
                 fg='white').grid(row=len(cust) + 2, column=0, padx=2, sticky='e')
        # custid entry
        del_custid_entry = tk.Entry(self.display_frame, font=("Calibri", 12, 'bold'), relief='sunken')
        del_custid_entry.grid(row=len(cust) + 2, column=1, padx=2, sticky='ew')

        # delete button
        tk.Button(self.display_frame, text='Delete', font=("Calibri", 12, 'bold'),
                  bg='red', fg='white', height=1, width=10, command=self.erase_cust).grid(row=len(cust) + 2,
                                                                                               padx=5, column=2,
                                                                                               sticky='w')

        custpageb = tk.Button(self.display_frame, text='Customer Page', font=("Calibri", 12, 'bold'),
                              fg='blue', bg='white', height=1, width=15, command=self.custpage)
        custpageb.grid(row=len(cust) + 2, column=6, padx=5, pady=5, stick='se')

        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_frame is not None:
            self.edit_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        self.display_frame.rowconfigure(list(range(len(cust) + 2)), weight=1)
        self.display_frame.columnconfigure(list(range(9)), weight=1)
        self.display_frame.grid(row=1, rowspan=len(cust) + 2, column=0, columnspan=4, sticky='nsew')

    def erase_cust(self):
        global lines, cust_ids, del_row, del_custid_entry
        # raise error alarm if any of the field is blank

        self.display_frame = self.make_frame(page_title='RECORD DELETED', background_color='blue')

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

        with open(Customer.cust_data, 'w', encoding='utf8') as hand:
            for row, rec in lines.items():
                if row == del_row:
                    # assign the selected row
                    self.cust_obj.__dict__ = rec
                    continue
                hand.writelines(f"{rec}\n")

        st = scrolledtext.ScrolledText(self.display_frame, bg='blue', fg='white', font=("Calibri", 14, 'bold'), relief='flat')
        st.insert(index='1.0', chars='ID, FIRST NAME, MIDDLE NAME, LAST NAME, GENDER, DATE OF BIRTH, NATIONALITY, STATE OF ORIGIN, OFFICE ADDRESS, DATE OPENED\n\n'
                                     f'{self.cust_obj.customer_id}, {self.cust_obj.first_name}, {self.cust_obj.mid_name}, {self.cust_obj.last_name}, '
                                     f'{self.cust_obj.gender}, {self.cust_obj.date_of_birth}, {self.cust_obj.country}, {self.cust_obj.state_of_origin}'
                                     f'{" ".join(self.cust_obj.office_addr.split())}, {self.cust_obj.date_opened}\n\n'
                                     'HAS BEEN DELETED!!')

        st.grid(row=0, column=0, columnspan=10, sticky='ew')

        tk.Button(self.display_frame, text='Customer Page', font=("Calibri", 12, 'bold'),
                             fg='blue', bg='white', height=1, width=15, command=self.custpage).grid(row=3, column=3, padx=5, pady=5, stick='se')

        self.display_frame.rowconfigure(list(range(4)), weight=1)
        self.display_frame.columnconfigure(list(range(4)), weight=1)
        self.display_frame.grid(row=1, rowspan=3, column=0, columnspan=4, sticky='nsew')
    
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
        self.dayEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'), width=10)
        self.dayEntry.insert(0, str(datetime.date.today().day))
        self.dayEntry.grid(row=2, column=1, padx=5, pady=50, sticky='sw')
        # month
        tk.Label(self.new_frame, text='Month', font=('calibri', 16),
                 bg='purple', fg='white', height=1).grid(row=2, column=2, padx=5, sticky='nw')
        self.monthEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'), width=10)
        self.monthEntry.insert(0, str(datetime.date.today().month))
        self.monthEntry.grid(row=2, column=2, padx=5, pady=50, sticky='sw')
        # year
        tk.Label(self.new_frame, text='Year', font=('calibri', 16),
                 bg='purple', fg='white', height=1).grid(row=2, column=2, sticky='n')
        self.yrEntry = tk.Entry(self.new_frame, font=('calibri', 16, 'bold'), width=10)
        self.yrEntry.insert(0, str(datetime.date.today().year))
        self.yrEntry.grid(row=2, column=2, pady=50, sticky='s')

        # submit and inventory page buttons
        submitButton = tk.Button(self.new_frame, text='Submit', font=("Calibri", 14, 'bold'),
                                 fg='white', bg='green', width=3, height=2, command=self.submitinv)
        submitButton.grid(row=3, column=2, padx=350, sticky='ew')
        invpageb = tk.Button(self.new_frame, text='Inventory Page', font=("Calibri", 14, 'bold'),
                             fg='purple', bg='white', height=2, width=15, command=self.invenpage)
        invpageb.grid(row=3, column=1, padx=5, stick='w')

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
        eyr, emon, eday = self.yrEntry.get(), self.monthEntry.get(), self.dayEntry.get()

        # collection of entry fields
        mandatory_entries = [pname, qty, unit, eyr,
                            emon, eday]
        str_type_entries = [pname, unit]
        num_type_entries = [qty, eyr, emon, eday]

        # conditionals
        wspace = string.whitespace   #['', ' ', '\n', '\t']
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
                int(entry)
            except ValueError as VE:
                # figures have not been entered, if error was raised
                return messagebox.showerror(title='Invalid Data Type',
                                            message=f'Character {entry} is not allowed here!')

        # numeric constraints
        if (int(eyr) not in range(2010, 2022)) or (int(emon) not in range(13)) or (int(eday) not in range(32)):
            return messagebox.showerror(title='OUT OF RANGE ENTRY', message=f'OUT OF RANGE ENTRY(S) DETECTED!\n\nPlease Check the REGISTRATION DATE\nDATE OF BIRTH entries')

        # string constraints
        if [True for entry in [pname, unit] if not(entry.isalnum)] or [True for entry in [pname, unit] for char in entry if char in string.punctuation]:
            return messagebox.showerror(title='OUT OF RANGE ENTRY',
                                        message=f'OUT OF RANGE ENTRY(S) DETECTED!\n\nPlease Check entries:\nPRODUCT NAME\nand\or\nUNIT OF MEASUREMENT')

        # assign user input from entry to each inventory class attribute
        self.inv_obj.prod_id = f"{''.join([word[0] for word in self.pnameEntry.get().title().split()])}{self.ID_gen()}"
        self.inv_obj.prod_name = self.pnameEntry.get().title()
        self.inv_obj.qty = self.qtyEntry.get()
        self.inv_obj.unit = self.unitEntry.get().title()
        self.inv_obj.entry_date = f"{self.yrEntry.get()}-{self.monthEntry.get()}-{self.dayEntry.get()}"

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
        with open(self.inv_obj.inv_data, 'a',
                  encoding='utf8') as hand:
            hand.writelines(f"{self.inv_obj.__dict__}\n")

        self.submit_frame = self.make_frame()

        saved = tk.Label(self.submit_frame, text='NEW INVENTORY HAS BEEN ADDED!', font=("arial", 14, 'bold'),
                         bg='purple', fg='white')
        saved.grid(row=0, column=0, columnspan=4, sticky='nsew')

        addb = tk.Button(self.submit_frame, text='Add Another', font=("Calibri", 14, 'bold'),
                         bg='blue', fg='white', height=5, width=15, command=self.new_inv)
        addb.grid(row=1, column=0, padx=5, stick='ew')

        invpageb = tk.Button(self.submit_frame, text='Inventory Page', font=("Calibri", 14, 'bold'),
                             fg='purple', bg='white', height=5, width=15, command=self.invenpage)
        invpageb.grid(row=1, column=3, padx=5, stick='ew')

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
        invpageb = tk.Button(self.display_frame, text='Inventory Page', font=("Calibri", 12, 'bold'),
                             fg='purple', bg='white', height=1, width=15, command=self.invenpage)
        invpageb.grid(row=2, column=3, padx=5, pady=5, stick='se')

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
        tk.Label(self.display_frame, text=f"PRODUCT:", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=1, column=0, sticky='ew', padx=25, pady=15)

        # product name label and entry
        tk.Label(self.display_frame, text="NAME", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=2, column=1, sticky='nw', padx=25, pady=15)
        self.pname_entry = tk.Entry(self.display_frame)
        self.pname_entry.insert(0, f'{self.inv_obj.prod_name}')
        self.pname_entry.grid(row=3, column=1, sticky='w', padx=25, pady=5)

        # product quantity label and entry
        tk.Label(self.display_frame, text="QUANTITY", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=2, column=2, sticky='nw', padx=25, pady=15)
        self.pqty_entry = tk.Entry(self.display_frame)
        self.pqty_entry.insert(0, f'{self.inv_obj.qty}')
        self.pqty_entry.grid(row=3, column=2, sticky='w', padx=25, pady=5)

        # unit of measurement label and entry
        tk.Label(self.display_frame, text="Unit of Measurement", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=2, column=3, sticky='nw', padx=25, pady=15)
        self.punit_entry = tk.Entry(self.display_frame)
        self.punit_entry.insert(0, f'{self.inv_obj.unit}')
        self.punit_entry.grid(row=3, column=3, sticky='w', padx=25, pady=5)

        # date labels and entries section
        tk.Label(self.display_frame, text="DATE", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=4, column=0, sticky='ew', padx=25, pady=15)
        # Year label and entry
        tk.Label(self.display_frame, text=f"YEAR", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=4, column=1, sticky='nw', padx=25, pady=15)
        year = re.findall(r'(\d{2,4})-(\d{1,2})-(\d{1,2})', self.inv_obj.entry_date)[0][0]
        self.yr_entry = tk.Entry(self.display_frame)
        self.yr_entry.insert(0, f'{year}')
        self.yr_entry.grid(row=5, column=1, sticky='w', padx=25, pady=5)
        # Month label and entry
        tk.Label(self.display_frame, text=f"MONTH", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=4, column=2, sticky='nw', padx=25, pady=15)
        month = re.findall(r'(\d{2,4})-(\d{1,2})-(\d{1,2})', self.inv_obj.entry_date)[0][1]
        self.mon_entry = tk.Entry(self.display_frame)
        self.mon_entry.insert(0, f'{month}')
        self.mon_entry.grid(row=5, column=2, sticky='w', padx=25, pady=5)
        # Day label and entry
        tk.Label(self.display_frame, text=f"DAY", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=4, column=3, sticky='nw', padx=25, pady=15)
        day = re.findall(r'(\d{2,4})-(\d{1,2})-(\d{1,2})', self.inv_obj.entry_date)[0][2]
        self.day_entry = tk.Entry(self.display_frame)
        self.day_entry.insert(0, f'{day}')
        self.day_entry.grid(row=5, column=3, sticky='w', padx=25, pady=5)

        # update and inventory page buttons
        updateb = tk.Button(self.display_frame, text='Update', font=("Calibri", 12, 'bold'),
                            bg='orange', fg='white', height=1, width=15, command=self.update_inv)
        updateb.grid(row=7, column=1, padx=5, pady=5, stick='sw')

        invpageb = tk.Button(self.display_frame, text='Inventory Page', font=("Calibri", 12, 'bold'),
                             fg='purple', bg='white', height=1, width=15, command=self.invenpage)
        invpageb.grid(row=7, column=3, padx=5, pady=5, stick='sw')

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
        # raise error alarm if any of the field is blank
        edited_entries = [self.pname_entry.get(), self.pqty_entry.get(), self.punit_entry.get(), self.yr_entry.get(), self.mon_entry.get(), self.day_entry.get()]
        blanks = ['', ' ', '\n', '\t']
        # when a field is blank
        if [True for entry in edited_entries if entry in blanks]:
            return messagebox.showerror(message="BLANK FIELD(S) DETECTED!")
        # when product name or unit of measurement is given in figures
        if [True for entry in [self.pname_entry.get(), self.punit_entry.get()] if entry.isdigit()]:
            return messagebox.showerror(message="PRODUCT NAME\nUNIT OF MEASUREMENT\n\nCannot contain only numbers")
        # when qty, date fields is/are not given in figures
        if [True for entry in [self.pqty_entry.get(),self.yr_entry.get(), self.mon_entry.get(), self.day_entry.get()] if not(entry.isdigit())]:
            return messagebox.showerror(message="QUANTITY\nDAY\nMONTH\nYEAR\nMust contain numbers only")

        if not(messagebox.askyesno(title='CONFIRM UPDATE', message='Do You Want to Continue?')):
            return messagebox.showinfo(message='NO CHANGES MADE TO INVENTORY')

        # when confirmation is given by user
        self.display_frame = self.make_frame()

        # reassign the newly entered values to the inventory object's name, qty, unit and date
        self.inv_obj.prod_name = self.pname_entry.get().title()
        self.inv_obj.qty, self.inv_obj.unit = self.pqty_entry.get(), self.punit_entry.get().title()
        self.inv_obj.entry_date = f"{self.yr_entry.get()}-{self.mon_entry.get()}-{self.day_entry.get()}"

        # update the retrieved data from file with the changes made
        lines[edit_row_num] = self.inv_obj.__dict__

        # save updated version to file
        # print([rec for row, rec in lines.items()])
        # print(Inventory.cust_data)
        with open(Inventory.inv_data, 'w', encoding='utf8') as hand:
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

        invpageb = tk.Button(self.display_frame, text='Inventory Page', font=("Calibri", 12, 'bold'),
                             fg='purple', bg='white', height=1, width=15, command=self.invenpage)
        invpageb.grid(row=2, column=3, padx=5, pady=5, stick='se')

        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_frame is not None:
            self.edit_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        self.display_frame.rowconfigure(list(range(4)), weight=1)
        self.display_frame.columnconfigure(list(range(4)), weight=1)
        self.display_frame.grid(row=1, rowspan=4, column=0, columnspan=4, sticky='nsew')

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

        # display headings for inventory records
        tk.Label(self.display_frame, text=f"PRODUCT ID", font=("Calibri", 14, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=0, sticky='e')
        tk.Label(self.display_frame, text=f"PRODUCT NAME", font=("Calibri", 14, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=1, sticky='nsew')
        tk.Label(self.display_frame, text=f"STOCK (in units)", font=("Calibri", 14, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=2, sticky='nsew')
        tk.Label(self.display_frame, text=f"DATE OF ENTRY", font=("Calibri", 14, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=3, sticky='nsew')

        for ind in range(len(inven)):
            # assign user input from stored inventory records to each inventory class attribute
            self.inv_obj.__dict__ = inven[ind]

            tk.Label(self.display_frame, text=f"{self.inv_obj.prod_id}", font=("Calibri", 10, 'bold'),
                     bg='purple', fg='white').grid(row=ind + 1, column=0, sticky='e')
            tk.Label(self.display_frame, text=f"{self.inv_obj.prod_name}", font=("Calibri", 10, 'bold'),
                     bg='purple', fg='white').grid(row=ind + 1, column=1, sticky='nsew')
            tk.Label(self.display_frame, text=f"{self.inv_obj.qty} {self.inv_obj.unit}", font=("Calibri", 10, 'bold'),
                     bg='purple', fg='white').grid(row=ind + 1, column=2, sticky='nsew')
            tk.Label(self.display_frame, text=f"{self.inv_obj.entry_date}", font=("Calibri", 10, 'bold'),
                     bg='purple', fg='white').grid(row=ind + 1, column=3, sticky='nsew')

        tk.Label(self.display_frame, text='ENTER PRODUCT ID:', font=("Calibri", 10, 'bold'), bg='purple',
                 fg='white').grid(row=len(inven) + 2, column=0, padx=2, sticky='e')

        del_prodid_entry = tk.Entry(self.display_frame, font=("Calibri", 10, 'bold'))
        del_prodid_entry.grid(row=len(inven) + 2, column=1, padx=2, sticky='w')

        # to edit the given row number (at row entry - 1)
        tk.Button(self.display_frame, text='Delete', font=("Calibri", 12, 'bold'),
                  bg='red', fg='white', height=1, width=10, command=self.erase_inv).grid(row=len(inven) + 2,
                                                                                         column=1,
                                                                                         sticky='e')
        tk.Button(self.display_frame, text='Inventory Page', font=("Calibri", 12, 'bold'),
                             fg='purple', bg='white', height=1, width=15, command=self.invenpage).grid(row=len(inven) + 2, column=3, padx=5, pady=5, stick='se')

        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_frame is not None:
            self.edit_frame.grid_forget()
        if self.new_frame is not None:
            self.new_frame.grid_forget()

        self.display_frame.rowconfigure(list(range(len(inven) + 2)), weight=1)
        self.display_frame.columnconfigure(list(range(4)), weight=1)
        self.display_frame.grid(row=1, rowspan=len(inven) + 2, column=0, columnspan=4, sticky='nsew')

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

        with open(Inventory.inv_data, 'w', encoding='utf8') as hand:
            for row, rec in lines.items():
                if row == del_row:
                    # assign the selected row
                    self.inv_obj.__dict__ = rec
                    continue
                hand.writelines(f"{rec}\n")

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

        invpageb = tk.Button(self.display_frame, text='Inventory Page', font=("Calibri", 12, 'bold'),
                             fg='purple', bg='white', height=1, width=15, command=self.invenpage)
        invpageb.grid(row=2, column=3, padx=5, pady=5, stick='se')

        self.display_frame.rowconfigure([0, 1, 2, 3], weight=1)
        self.display_frame.columnconfigure(list(range(4)), weight=1)
        self.display_frame.grid(row=1, rowspan=len(inven) + 2, column=0, columnspan=4, sticky='nsew')

# some functions
def login(ta, user):
    global eme, pe
    email, pwd = eme.get(), pe.get()
    mandatory_entries = [email, pwd]

    ta.display_frame = tk.LabelFrame(ta.master, bg='gold')

    wspace = string.whitespace

    # check for empty fields
    if [True for entry in mandatory_entries if (entry in wspace)]:
        return messagebox.showerror(title='Blank Field', message='BLANK FIELD(S) DETECTED!')

    # email constraints
    if not (re.findall(r'(.+)@(.+)[.](.+)', email)):
        return messagebox.showerror(title='INCORRECT EMAIL', message='Incorrect email address'
                                                                     '\n\nPlease EMAIL for @ or .')
    # password length
    if len(pwd) < 5:
        return messagebox.showerror(title='Password too short',
                                    message='Password Must Contain 5 or more characters')

    # extract username from email address
    stop = email.find("@")
    uname = email[:stop].capitalize()
    print(email)
    Found = False

    for path, folders, files in os.walk(user.dir_path):
        for folder in folders:
            if folder != uname:
                continue

            elif folder == uname:
                print(f"Checking {uname}'s login details")
                with open(f'{path}\\{folder}\\login_data.txt', 'r', encoding='utf8') as hand:
                    for line in hand.readlines():
                        attr = eval(line)
                        print(type(attr), attr)
                        for k, v in attr.items():
                            # check for matching email address and password
                            if k.lower() == 'email' and v.lower() == email.lower():
                                print(k, v)
                            if k.lower() == 'password' and v == pwd:
                                print(k, v)
                                Found = True
                                break

    if Found:
        user.__dict__ = attr
        print(f'Found {user.__dict__}')

        tk.Label(ta.display_frame, text=f"{user.username}'s Login Successful",
                 font=("Calibri", 10, 'bold'),
                 bg='gold', fg='black').grid(row=0, column=1, columnspan=2, sticky='NSEW', padx=25)

        tk.Button(ta.display_frame, text=f"Go to {user.company_name}'s Menu", command=ta.menupage,
                  font=("Calibri", 10, 'bold'),
                  bg='white', fg='blue').grid(row=1, column=1, columnspan=2, sticky='NSEW', padx=25)

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
        # inventory data file
        with open(f'{user.filepath}\\inv_data.txt', 'w', encoding='utf8') as hand:
            hand.writelines('')
        # customer data file
        with open(f'{user.filepath}\\cust_data.txt', 'w', encoding='utf8') as hand:
            hand.writelines('')
        # sales data file
        with open(f'{user.filepath}\\sales_data.txt', 'w', encoding='utf8') as hand:
            hand.writelines('')
        # accounts data file
        with open(f'{user.filepath}\\acct_data.txt', 'w', encoding='utf8') as hand:
            hand.writelines('')

        print(f'New Files Created at {user.filepath}')

    except:
        os.rmdir(f'{user.filepath}')
        print('Error: Something Went wrong')
        quit()

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